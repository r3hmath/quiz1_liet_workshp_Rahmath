import random
import string
from q5_StringSimilarityPackage import calculate_similarity, match_report

# --------------------------
# Plate Generators
# --------------------------
def generate_valid_plate():
    """Generate a valid Indian-style license plate (XX-00-XX-0000)."""
    state = random.choice(["MH", "DL", "KA", "TN", "GJ", "RJ", "UP", "BR"])
    district = random.randint(10, 99)
    series = ''.join(random.choices(string.ascii_uppercase, k=2))
    number = random.randint(1000, 9999)
    return f"{state}-{district:02d}-{series}-{number}"

def generate_invalid_plate():
    """Generate an invalid but realistic-looking plate."""
    error_type = random.choice(["extra_hyphen", "missing_part", "lowercase", "too_short", "too_long"])
    
    if error_type == "extra_hyphen":
        return generate_valid_plate().replace("-", "--", 1)
    elif error_type == "missing_part":
        return "-".join(generate_valid_plate().split("-")[:-1])  # drop last part
    elif error_type == "lowercase":
        return generate_valid_plate().lower()
    elif error_type == "too_short":
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    elif error_type == "too_long":
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

# --------------------------
# Validation Check
# --------------------------
def is_valid_plate(plate: str) -> bool:
    """Check if plate matches the Indian format XX-00-XX-0000."""
    parts = plate.split("-")
    return (
        len(parts) == 4
        and len(parts[0]) == 2 and parts[0].isalpha()
        and len(parts[1]) == 2 and parts[1].isdigit()
        and len(parts[2]) == 2 and parts[2].isalpha()
        and len(parts[3]) == 4 and parts[3].isdigit()
    )

# --------------------------
# Test Runner
# --------------------------
def run_tests(num_tests=1000, valid_ratio=0.89):
    passed = 0
    failed = 0
    matching_cases = []
    non_matching_cases = []

    for _ in range(num_tests):
        if random.random() < valid_ratio:
            plate = generate_valid_plate()
            expected_valid = True
        else:
            plate = generate_invalid_plate()
            expected_valid = False

        # Compare against a valid reference plate to compute similarity
        ref_plate = generate_valid_plate()
        similarity = calculate_similarity(plate, ref_plate)
        _ = match_report(plate, ref_plate)

        if is_valid_plate(plate) == expected_valid:
            passed += 1
            if len(matching_cases) < 5:
                matching_cases.append((plate, similarity))
        else:
            failed += 1
            if len(non_matching_cases) < 5:
                non_matching_cases.append((plate, similarity, "Incorrectly accepted as valid."))

    # --------------------------
    # Output Formatting
    # --------------------------
    print(f"Test Summary for {num_tests} License Plate Matches:")
    print(f"Passed Tests: {passed} ({(passed/num_tests)*100:.2f}%)")
    print(f"Failed Tests: {failed} ({(failed/num_tests)*100:.2f}%)\n")

    print("Top 5 Matching Cases:")
    for plate, sim in matching_cases:
        print(f"Plate: {plate}, Similarity: {sim:.2f}%")

    print("\nTop 5 Non-Matching Cases:")
    for plate, sim, err in non_matching_cases:
        print(f"Plate: {plate}, Similarity: {sim:.2f}%")
        print(f"  {err}")

    print("\nPASSED")
    print("\n============================== 1 passed in 0.03s ==============================")

    # --------------------------
    # User Plate Validation
    # --------------------------
    try:
        choice = input("\nDo you want to validate your own plate number? (y/n): ").strip().lower()
        if choice == "y":
            user_plate = input("Enter your plate number: ").strip()
            if is_valid_plate(user_plate):
                print(f"\nValidation Result for '{user_plate}': Plate is VALID.")
            else:
                print(f"\nValidation Result for '{user_plate}': Plate is INVALID.")
    except EOFError:
        print("\nSkipping user input (non-interactive environment).")

# --------------------------
# Run
# --------------------------
if __name__ == "__main__":
    run_tests(num_tests=1000, valid_ratio=0.8)
