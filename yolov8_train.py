from ultralytics import YOLO

model = YOLO("yolov8n.pt")   # n=nanomodel, fastest for practice
model.train(
    data="mydata.yaml",
    epochs=50,
    imgsz=1024,
    batch=16,
)
