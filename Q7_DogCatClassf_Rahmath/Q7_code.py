import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import cv2

# -----------------------------
# SETTINGS
# -----------------------------
input_folder = r"C:\Users\fayaf\Downloads\FaceRec_Rahmath\Q7_DogCatClassf_Rahmath\dataset"
output_folder = r"C:\Users\fayaf\Downloads\FaceRec_Rahmath\Q7_DogCatClassf_Rahmath\results"
os.makedirs(output_folder, exist_ok=True)

# Load pre-trained ImageNet MobileNetV2 model
model = MobileNetV2(weights="imagenet")

# -----------------------------
# FUNCTION TO CLASSIFY IMAGE
# -----------------------------
def classify_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    preds = model.predict(x)
    decoded = decode_predictions(preds, top=3)[0]
    return decoded

# -----------------------------
# PROCESS IMAGES
# -----------------------------
results = []

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        decoded_preds = classify_image(img_path)
        
        # Get top-1 prediction
        top_label = decoded_preds[0][1]
        
        # Simplify dogs only; cats keep full breed
        if "dog" in top_label.lower() or any(d in top_label.lower() for d in ["retriever", "poodle", "husky", "beagle"]):
            simplified = "dog"
        elif "cat" in top_label.lower() or any(c in top_label.lower() for c in ["tabby", "siamese", "persian"]):
            simplified = top_label
        else:
            simplified = "other"

        results.append((filename, top_label, simplified, decoded_preds))
        
        # -----------------------------
        # ANNOTATE IMAGE
        # -----------------------------
        img_cv = cv2.imread(img_path)
        text = f"Top-1: {top_label} | Simplified: {simplified}"
        cv2.putText(img_cv, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 255), 2)
        output_path = os.path.join(output_folder, f"annotated_{filename}")
        cv2.imwrite(output_path, img_cv)

# -----------------------------
# DISPLAY RESULTS
# -----------------------------
print("\nClassification Results:")
print("{:<20} {:<25} {:<15}".format("Image", "Top-1 Label", "Simplified"))
print("-"*70)
for res in results:
    print("{:<20} {:<25} {:<15}".format(res[0], res[1], res[2]))

# -----------------------------
# SHOW MISCLASSIFIED DOGS
# -----------------------------
print("\nDogs misclassified as other animals:")
for res in results:
    if "dog" in res[1].lower() and res[2] != "dog":
        print(f"{res[0]} ---> predicted as {res[2]} ({res[1]})")

print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("Reason for Innacuracy: ")
print(''' the reason for inaccuracy is basically a mismatch between the model’s fine-grained breed prediction and your simplified class labels. 
      Cats are easier because the breeds are recognized exactly. 
      Dogs are trickier because there are so many breeds, and not all are mapped to “dog” in your simplification rules.''')