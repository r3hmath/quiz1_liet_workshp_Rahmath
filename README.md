Syed Rahmath Ullah Hussaini - AI & Computer Vision Projects

Welcome to my repository containing various AI and computer vision projects completed as part of my coursework and personal learning. Each project is organized in its own folder with properly commented code, sample outputs, and supporting files.

---

## 📂 Projects Overview

###1. Q2 - Vehicle Attribute Identification and Scene Summary
**Folder:** `Q2_Rahmath` 
Overview:
This project uses YOLOv8 to detect vehicles in images and extract their attributes, including type/class, color, make/logo, and license plate details. It also generates a scene summary, identifying incoming/outgoing traffic, total vehicles, and lane assignments. Annotated images with bounding boxes and labels are produced automatically.

Key Features:
-Detects multiple vehicle attributes: type, class, color, make/logo, license plate presence and color.
-Identifies lane assignment and traffic direction (incoming/outgoing).
-Produces scene summaries: total vehicle count, traffic flow.
-Generates annotated images highlighting all detected details.

Requirements:
Python 3.8+
Packages: ultralytics, opencv-python, numpy, Pillow
GPU recommended for faster inference (CPU supported)

### 2. **Q3 - Face Landmark Detection**
**Folder:** `Q3_FaceRec_Rahmath`  
**Description:**  
This project uses MediaPipe Face Mesh to detect faces in images and annotate key landmarks such as the nose tip and eye centers. The output images include the face mesh, bounding boxes, and labeled landmarks.  
**Features:**  
- Detect multiple faces in an image.  
- Annotate nose tip and eyes with visual markers.  
- Save annotated images for analysis.  

**Usage:** Run `Q3_code.py` and check the `result/` folder for annotated images.

---

### 3. **Q4 - Face Blurring in Video Feeds**
**Folder:** `Q4_FaceBlurVideo_Rahmath`  
**Description:**  
Captures live video from a webcam or CCTV and automatically detects faces to apply a textured blur. Faces are highlighted with pink bounding boxes. Video recording functionality is included.  
**Features:**  
- Live video feed processing.  
- Face detection with MediaPipe (fallback to Haar Cascade).  
- Custom pink bounding boxes and textured blur.  
- Start/stop recording with `r`, quit with `q`.  

**Usage:** Run `Q4_code.py` and follow on-screen instructions to record or view the processed video.

---

### 4. **Q5 - String Similarity Matching**
**Folder:** `Q5_stringSimilarity_Rahmath`  
**Description:**  
Calculates the similarity between two strings (6–10 characters) using Levenshtein distance. Generates a detailed match report including aligned strings, matching characters, and non-matching characters.  
**Features:**  
- String similarity percentage calculation.  
- Alignment for optimal comparison.  
- Detailed report of matches and mismatches.  

**Usage:** Run `Q5_code.py` and input two strings interactively or via command-line arguments.

---

### 5. **Q6 - Automated License Plate Matching**
**Folder:** `Q6_LicensePlate_Rahmath`  
**Description:**  
Simulates license plate validation for Indian-style plates and generates similarity reports. Runs automated tests on 1000 valid and invalid plates.  
**Features:**  
- Valid/invalid plate generation.  
- Similarity computation against reference plates.  
- Top matching and non-matching cases summarized.  
- Optional interactive plate validation.  

**Usage:** Run `Q6_code.py` and view test summary in the console.

---

### 6. **Q7 - Cat vs. Dog Classification**
**Folder:** `Q7_DogCatClassification_Rahmath`  
**Description:**  
Uses a pre-trained MobileNetV2 model (ImageNet) to classify images of cats and dogs. Misclassified dogs are recorded and analyzed for accuracy.  
**Features:**  
- Pre-trained deep learning model for image classification.  
- Simplified cat vs dog labeling.  
- Analysis of misclassified dog images.  
- Sample outputs stored in `results/`.  

**Usage:** Run `Q7_code.py` to classify images in `sample_images/` and review results in the console and `results/` folder.

---

## 📌 How to Use
1. Clone this repository:
```bash
git clone https://github.com/r3hmath/quiz1_liet_workshop_Rahmath
