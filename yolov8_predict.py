import argparse
import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--img", type=str, required=True, help="Path to input image")
args = parser.parse_args()

model = YOLO("runs/detect/train/weights/best.pt")
results = model(args.img)

# results[0].plot() returns an annotated image (numpy array)
annotated = results[0].plot()

# Display with OpenCV
plt.imshow(annotated)
plt.axis("off")
plt.show()

# Save prediction
save_path = args.img.split(".")[0] + "_predicted.jpg"
plt.imsave(save_path, annotated)
print("Saved:", save_path)
