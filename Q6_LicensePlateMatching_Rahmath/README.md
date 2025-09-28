# Automated Testing of License Plate Matching (Q6)

## Overview

This project implements **automated testing** for license plate matching. It tests 1000 valid and invalid Indian license plate strings against the program developed in **Q5 (String Similarity Package)**. The main goals are:

- Validate the correctness of Indian license plate formats.
- Test the similarity matching logic.
- Summarize test results, including top matches and mismatches.

---

## Project Structure

Q6_LicensePlateMatching_Rahmath/
│
├── Q6_code.py # Main automated test runner
├── Q5_StringSimilarityPackage.py # String similarity functions used in testing
├── result/ # Folder to store any output results (optional)
└── README.md # Project documentation

## Functionality

### 1. License Plate Generation

- **Valid Plates:** Follow the Indian format `XX-00-XX-0000`  
  - `XX` → State code (MH, DL, KA, etc.)  
  - `00` → District code  
  - `XX` → Series code  
  - `0000` → Vehicle number  

- **Invalid Plates:** Malformed plates to test validation:
  - Extra hyphens
  - Missing parts
  - Lowercase letters
  - Too short or too long strings

### 2. Validation Function

`is_valid_plate(plate: str) -> bool`  

- Checks if a plate string matches the standard Indian format.
- Returns `True` if valid, `False` otherwise.

### 3. Similarity Matching

Uses Q5 functions:

- `calculate_similarity(str1, str2)` → Returns similarity percentage.
- `match_report(str1, str2)` → Returns detailed matches/mismatches.

### 4. Test Runner

`run_tests(num_tests=1000, valid_ratio=0.8)`  

- Generates 1000 plates (80% valid, 20% invalid by default)
- Validates each plate and computes similarity to a reference plate.
- Outputs:
  - Number of passed and failed validations
  - Top 5 matching plates
  - Top 5 non-matching plates
- Optionally allows user to validate a custom plate.

---

## Sample Output

Test Summary for 1000 License Plate Matches:
Passed Tests: 890 (89.00%)
Failed Tests: 110 (11.00%)

Top 5 Matching Cases:
Plate: MH-25-AB-1234, Similarity: 97.5%
Plate: DL-12-ZX-5678, Similarity: 96.8%
...

Top 5 Non-Matching Cases:
Plate: MH-25-AB1234, Similarity: 65.2%
Incorrectly accepted as valid
Plate: DL-12--ZX-5678, Similarity: 58.4%
Extra hyphen


## How to Run

1. Ensure Python 3.x is installed.
2. Install dependencies if required (none outside standard library).  
3. Run the automated test:

```bash
python Q6_code.py


Dependencies
Python Standard Library
random
string
Q5 String Similarity Package (Q5_StringSimilarityPackage.py)

Author
Syed Rahmath Ullah Hussaini

References
Indian vehicle registration guidelines: Parivahan
Python difflib module: Python Docs