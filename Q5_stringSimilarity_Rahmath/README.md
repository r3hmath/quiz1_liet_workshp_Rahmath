# String Similarity Matching (Q5)

## Overview

This project implements a **string similarity matching program** that:

- Accepts **two strings (6–10 characters)**.
- Calculates the **percentage similarity** between the strings.
- Generates a **match report** highlighting which characters match and which do not.
- Performs **alignment** to improve the comparison visually.

---

## Project Structure

Q5_stringSimilarity_Rahmath/
│
├── init.py
├── Q5_code.py # Main Python program
├── Result     # Optional output visualization
└── README.md # Project documentation


## Functionality

### 1. Similarity Calculation

- Uses **Levenshtein distance** to compute the minimum number of edits (insertions, deletions, substitutions) needed to transform one string into another.
- Similarity percentage is calculated as:

Similarity (%) = ((max_length - Levenshtein_distance) / max_length) * 100


---

### 2. String Alignment

- Aligns the two strings using the distance matrix.
- Visualizes insertions, deletions, and substitutions using `-` for missing characters.
- Ensures accurate match reporting.

---

### 3. Match Report

- **Aligned strings**: Shows both strings after alignment.
- **Matching characters**: Characters that are identical in both strings.
- **Non-matching characters**: Characters that differ, displayed as `char1 vs char2`.

---

## Sample Output

Enter the first string (6-10 characters): HELLO123
Enter the second string (6-10 characters): H3LLO12

Similarity Percentage: 87.50%
Aligned String 1: HELLO123
Aligned String 2: H-3LLO12
Matching characters: H, L, L, O, 1, 2
Non-matching characters: E vs 3, 3 vs -


## How to Run

1. Make sure you have **Python 3.x** installed.  
2. Navigate to the project directory:

```bash
cd Q5_stringSimilarity_Rahmath
Run the program interactively:

bash
python Q5_code.py

bash
python Q5_code.py HELLO123 H3LLO123

Dependencies
Python Standard Library:

sys

No external packages are required.

Applications
License plate comparison

Spell checking

OCR error correction

DNA or protein sequence comparison

Author
Syed Rahmath Ullah Hussai

References
Levenshtein distance: https://en.wikipedia.org/wiki/Levenshtein_distance

Python sys module documentation: https://docs.python.org/3/library/sys.html

Dynamic programming in string comparison: Cormen et al., Introduction to Algorithms, 3rd Edition