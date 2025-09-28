import cv2
import mediapipe as mp
import numpy as np
import os

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Landmark indices for features (MediaPipe Face Mesh standard)
NOSE_TIP_INDEX = 1
LEFT_EYE_INDICES = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
RIGHT_EYE_INDICES = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]

def compute_landmark_center(landmarks, indices, image_shape):
    """Compute average (x, y) for given landmark indices."""
    h, w = image_shape[:2]
    points = np.array([(landmarks[i].x * w, landmarks[i].y * h) for i in indices])
    return np.mean(points, axis=0).astype(int)

def annotate_face_landmarks(image_path, output_path, draw_mesh=True):
    """Detect faces, locate nose tip and eye centers, and annotate the image."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}.")
        return

    h, w = image.shape[:2]

    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=5,
        refine_landmarks=True,
        min_detection_confidence=0.5
    ) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.multi_face_landmarks:
            print(f"No faces detected in {os.path.basename(image_path)}.")
            cv2.imwrite(output_path, image)
            return

        print(f"Detected {len(results.multi_face_landmarks)} face(s) in {os.path.basename(image_path)}.")

        for face_landmarks in results.multi_face_landmarks:
            if draw_mesh:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )

            landmarks = face_landmarks.landmark
            x_coords = [landmark.x * w for landmark in landmarks]
            y_coords = [landmark.y * h for landmark in landmarks]
            bbox = (int(min(x_coords)), int(min(y_coords)), int(max(x_coords)), int(max(y_coords)))

            cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)

            nose_tip = (int(landmarks[NOSE_TIP_INDEX].x * w), int(landmarks[NOSE_TIP_INDEX].y * h))
            cv2.circle(image, nose_tip, 5, (0, 0, 255), -1)
            cv2.putText(image, "Nose Tip", (nose_tip[0] + 10, nose_tip[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

            left_eye_center = compute_landmark_center(landmarks, LEFT_EYE_INDICES, image.shape)
            cv2.circle(image, tuple(left_eye_center), 5, (255, 0, 0), -1)
            cv2.putText(image, "Left Eye", (left_eye_center[0] + 10, left_eye_center[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

            right_eye_center = compute_landmark_center(landmarks, RIGHT_EYE_INDICES, image.shape)
            cv2.circle(image, tuple(right_eye_center), 5, (255, 0, 0), -1)
            cv2.putText(image, "Right Eye", (right_eye_center[0] + 10, right_eye_center[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imwrite(output_path, image)
    print(f"Annotated image saved to {output_path}")


if __name__ == "__main__":
    input_folder = r"C:\Users\fayaf\Downloads\FaceRec_Rahmath\Q3_FaceRec_Rahmath\testImage"
    output_folder = r"C:\Users\fayaf\Downloads\FaceRec_Rahmath\Q3_FaceRec_Rahmath\result"

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"annotated_{filename}")
            annotate_face_landmarks(input_path, output_path, draw_mesh=True)
