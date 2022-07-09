# Recyclops Backend

The backend which serves the pytorch model for image inference 

## Technologies

|Tech|Version|
|:-:|:-:|
|Python|3.9.5|
|Flask|2.1.2|
|PyTorch|1.12.0|

## Usage

The server only exposes a single __POST__ request on `{hostname}/predict`  

Using Curl
```sh
curl -X POST -F file=@"<path to img>" {hostname}/predict
```

## Setup (Local)

This setup was only tested on `python 3.9.5`

1. Install python dependencies
```sh
pip install -r requirements.txt
```

2. (Optional) edit model & label maps in `app.py`
```python
MODEL_PATH = 'models/resnet_large_resize_150_cpu.model'
LABEL_MAP_PATH = 'label_maps/full_label_map.json'
```

Note: Label maps must correspond to the model used (specified in the file name)

3. Run server
```sh
flask run
```

## Deployment (Heroku)

Do use the `heroku` branch if you're following this steps

1. Setup new heroku
```sh
heroku login -i
heroku create <app name>
```

2. Setup heroku remote and push
```sh
heroku git:remote -a <app name>
git push heroku heroku:master
```

3. Setup environments for model & label map
```sh
heroku config:set MODEL_PATH=models/resnet_large_resize_150_cpu.model
heroku config:set LABEL_MAP_PATH=label_maps/full_label_map.json
```
The server should be up by now

Note: Feel free to change the model path and label map path, however as mentioned above do make sure they __correspond__ to each other