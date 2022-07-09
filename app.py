import io
import json

import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request

MODEL_PATH = 'models/densenet_full_resize_199_cpu.model'
LABEL_MAP_PATH = 'label_maps/full_label_map.json'
INPUT_SIZE = 224

app = Flask(__name__)

imagenet_class_index = json.load(open(LABEL_MAP_PATH))
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


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    tensor = tensor.to(device)
    outputs = model.forward(tensor)

    probs = torch.nn.functional.softmax(outputs, dim=1)
    conf, classes = torch.max(probs, 1)
    predicted_idx = str(classes.item())
    conf = conf.item()

    return conf, imagenet_class_index[predicted_idx]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        conf, class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'confidence': conf, 'class_name': class_name})


if __name__ == '__main__':
    app.run()