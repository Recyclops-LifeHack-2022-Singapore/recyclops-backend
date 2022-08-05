import io
import json

import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request

data_transforms = lambda input_size : {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(input_size),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(input_size),
        transforms.CenterCrop(input_size),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

#### CONFIGURATIONS ####

## OBJECT DETECTION
MODEL_TYPE = 1 # 0 -> Image Classification, 1 -> Object Detection
MODEL = fasterrcnn_resnet50_fpn_v2(weights=FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT, box_score_thresh=0.9)
TRANSFORM = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT.transforms() 
LABEL_MAP = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT.meta["categories"] 

## IMAGE CLASSIFICATION
# INPUT_SIZE = 224
# MODEL_TYPE = 0
# MODEL = 'models/densenet_full_resize_199_cpu.model'
# TRANSFORM = data_transforms(INPUT_SIZE)['val']
# LABEL_MAP = 'label_maps/full_label_map.json' 

#### CONFIGURATIONS ####

label_map = json.load(open(LABEL_MAP)) if type(LABEL_MAP) == str else LABEL_MAP
model = torch.load(MODEL) if type(MODEL) == str else MODEL
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

app = Flask(__name__)

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')

    return TRANSFORM(image).unsqueeze(0)


def get_classifcation_prediction(image_bytes):
    tensor = preprocess_image(image_bytes=image_bytes)
    tensor = tensor.to(device)
    outputs = model.forward(tensor)

    probs = torch.nn.functional.softmax(outputs, dim=1)
    conf, classes = torch.max(probs, 1)
    predicted_idx = str(classes.item())
    conf = conf.item()

    return conf, label_map[predicted_idx]

def get_object_detection_prediction(image_bytes):
    tensor = preprocess_image(image_bytes=image_bytes)

    tensor = tensor.to(device)
    outputs = model.forward(tensor)[0]
    boxes, labels, scores = outputs['boxes'], outputs['labels'], outputs['scores']
    
    objects = []
    for i in range(len(boxes)):
        objects.append({
            'box': boxes[i].tolist(),
            'class_name': label_map[labels[i].item()],
            'confidence': scores[i].item()
        })

    return objects

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()

        res = None
        if MODEL_TYPE == 0:
            conf, class_name = get_classifcation_prediction(image_bytes=img_bytes)
            res = jsonify({'confidence': conf, 'class_name': class_name})
        elif MODEL_TYPE == 1:
            objects = get_object_detection_prediction(image_bytes=img_bytes)
            res = jsonify({'result': objects})
        else:
            return jsonify({'message': 'Unknown model type configuration'}), 500
        
        return res


if __name__ == '__main__':
    app.run()