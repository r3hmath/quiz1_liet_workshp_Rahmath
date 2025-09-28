# Q7 – Cat vs. Dog Classification Using Pre-trained MobileNetV2

**Author:** Syed Rahmath Ullah Hussai  
**Project Directory:** `Q7_DogCatClassification_Rahmath/`  

---

## Project Overview
This project demonstrates the use of a pre-trained ImageNet model, **MobileNetV2**, to classify images of cats and dogs. The main goals are:  

1. Load a pre-trained MobileNetV2 model.  
2. Classify sample images of cats and dogs.  
3. Identify misclassified dogs and analyze the reasons for inaccuracies.  

> Note: The ImageNet model was trained for 1,000 classes, including multiple dog breeds, not just the binary "cat vs dog". This can lead to misclassifications when simplifying predictions.

---

## Directory Structure

Q7_DogCatClassification_Rahmath/
│
├── results/
│ ├── missclassified_dogs.png # Sample images of misclassified dogs
│ ├── reason_For_inaccuracy.png # Analysis of misclassification reasons
│ ├── results_classification.png # Summary of classification results
│ └── results_classification2.png # Additional visual results
│
├── sample_images/
│ ├── train/
│ │ ├── cats/
│ │ └── dogs/
│ └── validation/
│ ├── cats/
│ └── dogs/
│
├── Q7_code.py # Python script for classification
└── README.md # Project documentation

---

## Dependencies

- Python 3.8+
- TensorFlow 2.x
- NumPy
- Keras (comes with TensorFlow)
- Pillow (for image preprocessing)

#Install dependencies using:

```bash
pip install tensorflow numpy pillow

How to Run
Place your cat and dog images in the sample_images/train and sample_images/validation folders.

#Execute the script:
bash
python Q7_code.py


The script will:
Load up to 50 sample images randomly from the dataset.

Classify each image using MobileNetV2.

Simplify the predictions to "cat", "dog", or "unknown".

Print a table of results.

Highlight misclassified dogs and the likely reasons.

Results
Classification results are stored in the results/ folder as images:

results_classification.png and results_classification2.png: visual representation of predicted vs true labels.

missclassified_dogs.png: sample dog images that were misclassified.

reason_For_inaccuracy.png: explanation of why some dogs were misclassified (ImageNet model limitation).

Observations:

Cats are generally classified correctly (labels like "tabby", "Siamese", "Persian").

Dogs are often misclassified due to ImageNet's multiple breed categories.

Some dogs are labeled as "unknown" when the breed keyword is not recognized in the simplification logic.

Key Takeaways
Pre-trained ImageNet models are excellent for multi-class classification but may require fine-tuning for binary tasks like "cat vs dog".

Misclassification occurs primarily because MobileNetV2 predicts specific dog breeds instead of the general "dog" category.

Fine-tuning the model on a binary cat-vs-dog dataset would improve accuracy.

References
TensorFlow Keras Applications – MobileNetV2
ImageNet Dataset