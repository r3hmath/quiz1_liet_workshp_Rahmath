# Face Blurring in Video Feeds (Q4)

## Overview

This project captures live video from a **webcam or CCTV** and automatically **detects and blurs all faces** in the feed. It also provides functionality to **save video clips** on demand.  

Key features:

- Real-time face detection using **MediaPipe**.
- **Fallback to Haar Cascade** if MediaPipe fails or detects no faces.
- Strong **Gaussian blur** applied to face regions.
- Display processed video feed in real-time.
- Option to **record video clips** by pressing a key.

---

## Project Structure

Q4_FaceBlurring_Rahmath/
│
├── Q4_code.py # Main Python program
├── output.avi # Saved video (generated during recording)
└── README.md # Project documentation

---

## How It Works

1. **Video Capture**: Captures frames from webcam (`cv2.VideoCapture(0)`), or an RTSP URL for CCTV.
2. **Face Detection**:
   - **Primary**: MediaPipe Face Detection for higher accuracy.
   - **Fallback**: Haar Cascade (OpenCV) if MediaPipe fails.
3. **Face Blurring**:
   - Extracts the face region.
   - Applies a **strong Gaussian blur** using `cv2.GaussianBlur`.
4. **Display**:
   - Shows the real-time processed video with blurred faces.
5. **Video Recording**:
   - Press **`r`** to start/stop recording.
   - Press **`q`** to quit the application.

---

## Usage

1. Ensure you have **Python 3.x** installed.
2. Install dependencies:

```bash
pip install opencv-python mediapipe numpy

Run the program:
python Q4_code.py

Controls:
r: Start/stop recording video clip (output.avi saved automatically)

q: Quit the program

Adjust video capture by replacing 0 with a CCTV RTSP URL if needed:

python
Copy code
cap = cv2.VideoCapture("rtsp://username:password@ip_address:port/stream")
Dependencies
OpenCV – Video capture, display, blurring

MediaPipe – Face detection

NumPy – Array operations

Notes
MediaPipe requires RGB images; OpenCV uses BGR by default.

Video writer is configured for .avi using MJPG codec. You can change the codec to XVID or MP4V for broader compatibility.

Gaussian blur kernel (99, 99) ensures strong anonymization; adjust for different blur strength.

Applications
Privacy protection in CCTV feeds.

Automatic face anonymization for live streams.

Data collection for video analytics without exposing personal identity.

Author
Syed Rahmath Ullah Hussai