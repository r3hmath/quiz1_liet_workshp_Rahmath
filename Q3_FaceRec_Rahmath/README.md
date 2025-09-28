Q3: Face Landmark Detection and Annotation

## Project Overview
This project uses **MediaPipe Face Mesh** to detect faces in images and annotate facial landmarks, including the **nose tip**, **left eye center**, and **right eye center**. Each detected face is also highlighted with a bounding box, and optional mesh visualization can be added for better clarity.

The goal is to process a folder of images and output annotated versions showing the detected facial features.

---

## Features
- Detect multiple faces in a single image.
- Highlight the face with a **green bounding box**.
- Mark and label key facial landmarks:
  - Nose tip (red circle)
  - Left eye center (blue circle)
  - Right eye center (blue circle)
- Optional **face mesh visualization** for detailed landmark structure.
- Save annotated images to a specified output folder.

---

## Requirements
- Python 3.8+
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

Install dependencies via pip:
```bash
pip install opencv-python mediapipe numpy
Directory Structure
bash
Copy code
Q3_FaceRec_Rahmath/
├── testImage/          # Input images for face annotation
├── result/             # Annotated images output
├── Q3_code.py          # Main script for processing images
├── README.md
How to Run
Update the input_folder and output_folder paths in Q3_code.py:

python
Copy code
input_folder = "path_to_your_input_images"
output_folder = "path_to_save_results"
Run the script:

bash
Copy code
python Q3_code.py
Annotated images will be saved in the result/ folder with the prefix annotated_.

How It Works
Face Detection

Uses MediaPipe Face Mesh to detect facial landmarks.

Falls back to standard landmark detection if no faces are detected.

Landmark Computation

Computes average coordinates for eyes using predefined landmark indices.

Marks nose tip directly using MediaPipe landmark.

Annotation

Draws bounding boxes around detected faces.

Draws circles and labels for nose tip and eyes.

Optionally, overlays face mesh for detailed visualization.

Sample Output
Annotated images will look like this:

Green rectangle: Face bounding box

Red circle: Nose tip

Blue circles: Eye centers

Optional mesh: Tesselated face landmarks

Notes
Handles multiple faces per image.

Supports .jpg, .jpeg, and .png file formats.

Ensure input images are clear and well-lit for optimal detection accuracy.

Author
Syed Rahmath Ullah Hussai