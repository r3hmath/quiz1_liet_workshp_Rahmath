# q5_StringSimilarityPackage.py
from difflib import SequenceMatcher

def calculate_similarity(str1: str, str2: str) -> float:
    """
    Calculate percentage similarity between two strings.
    Uses SequenceMatcher to compute similarity ratio.
    Returns similarity as a percentage.
    """
    ratio = SequenceMatcher(None, str1, str2).ratio()
    return round(ratio * 100, 2)


def match_report(str1: str, str2: str) -> dict:
    """
    Generate a match report indicating which characters match
    and which do not. Performs alignment if needed.
    Returns a dictionary with details.
    """
    matcher = SequenceMatcher(None, str1, str2)
    matches = []
    mismatches = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            matches.append(str1[i1:i2])
        elif tag in ('replace', 'delete', 'insert'):
            mismatches.append((str1[i1:i2], str2[j1:j2]))

    return {
        "string1": str1,
        "string2": str2,
        "similarity": calculate_similarity(str1, str2),
        "matches": matches,
        "mismatches": mismatches
    }


if __name__ == "__main__":
    # Simple manual test
    s1 = input("Enter first string (6–10 chars): ")
    s2 = input("Enter second string (6–10 chars): ")

    similarity = calculate_similarity(s1, s2)
    report = match_report(s1, s2)

    print(f"\nSimilarity between '{s1}' and '{s2}': {similarity}%")
    print("Match Report:")
    print("  Matches:", report["matches"])
    print("  Mismatches:", report["mismatches"])
