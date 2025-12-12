# Hands on Yolov8 with pytorch

yolov8 repository cloned from ultralytics.
## Dataset
Airplanes Detection Dataset from Kaggler mrcsgh.
Annotations in Yolo format: One text file per image, One line per object.

```class_id center_x center_y width height```

## Requirements
Python 3.10 venv.  
```pip install -r requirements.txt
```
## Run prediction
```python yolov8_predict.py --img <image_path>```

## convert to tflight
When converting to tflite, tf saved model will also be created. It can later be used for conversion to tf.js.
```pip install tensorflow==2.12.0 'onnx2tf>=1.15.4,<=1.17.5' 'sng4onnx>=1.0.1' 'onnx_graphsurgeon>=0.3.26' tflite_support```

**Note:** If having timeout issue, pip install with flag `--default-timeout=500`.

```python yolov8_to_tflite.py```

## convert to tf.js
Conversion [tutorial](https://github.com/Hyuto/yolov8-tfjs).
```pip install tensorflowjs==3.17.0```
```python yolov8_to_tfjs.py```

### use tf.js

