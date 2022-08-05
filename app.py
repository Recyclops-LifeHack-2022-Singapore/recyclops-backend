import io
import json

import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request

MODEL_TYPE = 0 # 0 -> Image Classification, 1 -> Object Detection
MODEL_PATH = 'models/densenet_full_resize_199_cpu.model'
LABEL_MAP_PATH = 'label_maps/full_label_map.json'
INPUT_SIZE = 224

app = Flask(__name__)

label_map = json.load(open(LABEL_MAP_PATH))
model = torch.load(MODEL_PATH)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

def transform_image(image_bytes):
    data_transforms = {
        'train': transforms.Compose([
            transforms.RandomResizedCrop(INPUT_SIZE),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'val': transforms.Compose([
            transforms.Resize(INPUT_SIZE),
            transforms.CenterCrop(INPUT_SIZE),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return data_transforms['val'](image).unsqueeze(0)


def get_classifcation_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    tensor = tensor.to(device)
    outputs = model.forward(tensor)

    probs = torch.nn.functional.softmax(outputs, dim=1)
    conf, classes = torch.max(probs, 1)
    predicted_idx = str(classes.item())
    conf = conf.item()

    return conf, label_map[predicted_idx]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()

        res = None
        if MODEL_TYPE == 0:
            conf, class_name = get_classifcation_prediction(image_bytes=img_bytes)
            res = jsonify({'confidence': conf, 'class_name': class_name})
        else:
            return jsonify({'message': 'Unknown model type configuration'}), 500
        
        return res


if __name__ == '__main__':
    app.run()