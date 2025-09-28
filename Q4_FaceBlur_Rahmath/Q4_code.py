import cv2
import mediapipe as mp
import numpy as np
import time

# --------------------------#
# Initialize Face Detection  #
# --------------------------#
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Haar Cascade fallback
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
use_haar = not face_cascade.empty()

# Initialize MediaPipe detector once
face_detection = mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5
)

# --------------------------#
# Video Capture Setup       #
# --------------------------#
cap = cv2.VideoCapture(0)  # 0 for webcam
if not cap.isOpened():
    print("Error: Could not open video feed.")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 20.0

# Video writer setup
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # AVI codec
output_file = 'blurred_faces_output.avi'
out = None
recording = False

# --------------------------#
# Performance Tracking      #
# --------------------------#
prev_time = 0

print("Press 'r' to start/stop recording, 'q' to quit.")

# --------------------------#
# Helper Functions          #
# --------------------------#
def apply_mosaic_blur(face_roi, blocks=15):
    """Apply mosaic/pixelated blur effect."""
    h, w = face_roi.shape[:2]
    x_steps = max(1, w // blocks)
    y_steps = max(1, h // blocks)
    # Resize down
    small = cv2.resize(face_roi, (x_steps, y_steps), interpolation=cv2.INTER_LINEAR)
    # Resize up
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces_detected = False

        # --------------------------#
        # MediaPipe Face Detection  #
        # --------------------------#
        results = face_detection.process(rgb_frame)
        if results.detections:
            faces_detected = True
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y = int(bboxC.xmin * iw), int(bboxC.ymin * ih)
                w, h = int(bboxC.width * iw), int(bboxC.height * ih)
                
                # Clamp values
                x, y = max(0, x), max(0, y)
                w, h = min(w, iw - x), min(h, ih - y)
                
                face_roi = frame[y:y+h, x:x+w]
                if face_roi.size > 0:
                    # Apply mosaic texture
                    textured_face = apply_mosaic_blur(face_roi, blocks=20)
                    frame[y:y+h, x:x+w] = textured_face

                    # Draw pink bounding box
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 105, 180), 2)  # Hot pink

        # --------------------------#
        # Haar Cascade Fallback     #
        # --------------------------#
        if not faces_detected and use_haar:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                face_roi = frame[y:y+h, x:x+w]
                if face_roi.size > 0:
                    textured_face = apply_mosaic_blur(face_roi, blocks=20)
                    frame[y:y+h, x:x+w] = textured_face
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 105, 180), 2)

        # --------------------------#
        # Overlay Info              #
        # --------------------------#
        curr_time = time.time()
        fps_display = 1 / (curr_time - prev_time) if prev_time != 0 else 0
        prev_time = curr_time

        cv2.putText(frame, f'FPS: {fps_display:.2f}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        face_count = len(results.detections) if results.detections else 0
        cv2.putText(frame, f'Faces: {face_count}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if recording:
            cv2.circle(frame, (frame_width-30, 30), 10, (0, 0, 255), -1)
            cv2.putText(frame, 'REC', (frame_width-90, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display
        cv2.imshow('Blurred & Textured Faces Feed', frame)

        # --------------------------#
        # Key Controls              #
        # --------------------------#
        delay = max(1, int(1000 // fps))
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('q'):
            print("Quitting...")
            break
        elif key == ord('r'):
            if recording:
                if out is not None:
                    out.release()
                    out = None
                recording = False
                print(f"Recording stopped: {output_file}")
            else:
                out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
                if out.isOpened():
                    recording = True
                    print("Recording started...")
                else:
                    print("Error: Could not start recording.")

        if recording and out is not None:
            out.write(frame)

finally:
    face_detection.close()
    cap.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()
