from ultralytics import YOLO

# Load the model weights
model = YOLO("runs/detect/train/weights/best.pt")

# Export directly to TFLite format
# Use 'int8' or 'float32' as needed. 'float32' is safest for TF.js.
# The model will be saved as 'best.tflite'
model.export(format="tflite", int8=False, dynamic=False) 

print("Successfully exported to best.tflite")