Vehicle Attribute Identification and Scene Summary

#Overview
This project develops a program to detect vehicle attributes and provide a comprehensive scene summary from images. The program uses YOLO (You Only Look Once) v8 for object detection and classification to identify vehicles and their attributes such as type, class, color, make, and license plate information. The output includes both a textual summary and annotated images highlighting detected vehicles and details.


#Features

-Detects vehicle attributes:

-Type/Class of vehicle (car, truck, motorcycle, etc.)

-Color

-Make/Company (via logo detection)

-Vehicle bounding box

-Logo bounding box

-License Plate presence and bounding box

-License Plate color

-Lane assignment (Left/Right)

Provides scene summary:

Incoming traffic (Yes/No)

Outgoing traffic (Yes/No)

Total number of vehicles

Generates annotated images with all detected details overlaid.

Supports multiple vehicles per image.


#Requirements
Python 3.8+
Packages:
ultralytics
opencv-python
numpy
Pillow

GPU recommended for faster inference, but CPU is supported.

#Install dependencies:
pip install ultralytics opencv-python numpy Pillow


Verify installation:

import ultralytics
ultralytics.checks()

#Usage

#Import necessary libraries:

import os
import json
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


Load YOLOv8 model:

model = YOLO("yolov8m.pt")  # You can also use yolov8n.pt for faster inference


Run detection on an image:

results = model.predict(source="test_image.jpg", save=True)


Extract vehicle attributes and generate summary:

Vehicle type, color, make, and bounding boxes

License plate presence, color, and bounding box

Lane information

Incoming/outgoing traffic detection

Total vehicle count

Annotated images are automatically saved in the output folder with detected details drawn on the image.

Folder Structure
project_root/
│
├──vehicle_dataset         # Input images
├── Q2_Result              # Annotated output images
├── models/                # YOLO models
├── vehicle_detection.py   # Main detection script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

Notes

Make/Logo Detection: Can be improved by training a custom YOLO model on vehicle logos.

Traffic Direction: Uses vehicle positions and lane info to determine incoming/outgoing traffic.

Performance: Model accuracy depends on image quality and lighting conditions.

Ensure all images are correctly formatted (JPG/PNG) and properly scaled for YOLO inference.

References
YOLOv8 Documentation
OpenCV Documentation
Pillow Documentation
OpenAI
GrokAI