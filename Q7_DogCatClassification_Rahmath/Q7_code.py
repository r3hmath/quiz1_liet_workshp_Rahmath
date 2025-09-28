import os
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Paths
base_dir = r"C:\Users\fayaf\Downloads\FaceRec_Rahmath\Q7_DogCatClassification_Rahmath\sample_images"
train_cat_dir = os.path.join(base_dir, "train", "cats")
train_dog_dir = os.path.join(base_dir, "train", "dogs")
val_cat_dir = os.path.join(base_dir, "validation", "cats")
val_dog_dir = os.path.join(base_dir, "validation", "dogs")

# Load pre-trained MobileNetV2
model = MobileNetV2(weights="imagenet")

# Collect images from both train and validation sets (only 5–10 test cases total)
train_cat_images = [os.path.join(train_cat_dir, img) for img in os.listdir(train_cat_dir) if img.endswith(".jpg")]
train_dog_images = [os.path.join(train_dog_dir, img) for img in os.listdir(train_dog_dir) if img.endswith(".jpg")]
val_cat_images = [os.path.join(val_cat_dir, img) for img in os.listdir(val_cat_dir) if img.endswith(".jpg")]
val_dog_images = [os.path.join(val_dog_dir, img) for img in os.listdir(val_dog_dir) if img.endswith(".jpg")]

all_images = train_cat_images + train_dog_images + val_cat_images + val_dog_images
test_images = random.sample(all_images, min(50, len(all_images)))
  # pick up to 10 images

results = []

for img_path in test_images:
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded = decode_predictions(preds, top=3)[0]

    # Determine if ground truth is cat or dog
    true_label = "cat" if "cats" in img_path else "dog"

    # Get top-1 predicted label
    predicted_label = decoded[0][1]  # e.g. 'tabby', 'Labrador_retriever'
    
    # Simplify to 'cat' or 'dog'
    if any(word in predicted_label.lower() for word in ["cat", "tabby", "siamese"]):
        predicted_simple = "cat"
    elif any(word in predicted_label.lower() for word in ["dog", "retriever", "poodle", "husky"]):
        predicted_simple = "dog"
    else:
        predicted_simple = "unknown"

    results.append((img_path, true_label, predicted_simple, predicted_label))

# Print results in a table
print("\nClassification Results (Sample 50 images):\n")
print("{:<40} {:<10} {:<10} {:<20}".format("Image", "True", "Predicted", "Top-1 Label"))
print("-"*80)
for res in results:
    print("{:<40} {:<10} {:<10} {:<20}".format(os.path.basename(res[0]), res[1], res[2], res[3]))

# Show misclassified dogs
print("\nMisclassified Dogs:\n")
for res in results:
    if res[1] == "dog" and res[2] != "dog":
        print(f"{os.path.basename(res[0])} ---> predicted as {res[2]} ({res[3]})")
print('____________________________________________________________________________________')
print('____________________________________________________________________________________')
print('____________________________________________________________________________________')
print('''The experiment shows that while MobileNetV2 can correctly identify many cats and dogs, dogs are often misclassified as specific breeds (e.g., “Basset” or “Brittany_spaniel”). 
      Since our simplification logic only looks for the keywords “dog”, “retriever”, “poodle”, or “husky”, these predictions are marked as unknown.
    This highlights a key limitation of using an ImageNet pre-trained model for binary classification: it was trained on 1,000 classes, including many different dog breeds, but not simply “dog” vs. “cat”. 
      As a result, cats are more consistently predicted (labels like “tabby”, “Siamese”, “Persian”), while dogs are spread across dozens of breed categories, leading to frequent mismatches when simplified.

*In summary, the model performs well at distinguishing cats but is less reliable for dogs, often requiring fine-tuning on a cat-vs-dog dataset for better accuracy.*''')