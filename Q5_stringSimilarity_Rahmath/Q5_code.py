import sys

def calculate_similarity(str1, str2):
    """Calculate the percentage similarity between two strings using Levenshtein distance."""
    if not (6 <= len(str1) <= 10 and 6 <= len(str2) <= 10):
        raise ValueError("Strings must be between 6 and 10 characters long.")
    
    # Initialize matrix for dynamic programming
    rows, cols = len(str1) + 1, len(str2) + 1
    matrix = [[0] * cols for _ in range(rows)]
    
    # Fill the first row and column
    for i in range(rows):
        matrix[i][0] = i
    for j in range(cols):
        matrix[0][j] = j
    
    # Compute Levenshtein distance
    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(
                    matrix[i-1][j] + 1,    # deletion
                    matrix[i][j-1] + 1,    # insertion
                    matrix[i-1][j-1] + 1   # substitution
                )
    
    # Calculate similarity percentage
    max_length = max(len(str1), len(str2))
    distance = matrix[rows-1][cols-1]
    similarity = ((max_length - distance) / max_length) * 100
    return similarity, matrix

def align_strings(str1, str2, matrix):
    """Perform alignment and generate match report based on the distance matrix."""
    i, j = len(str1), len(str2)
    aligned_str1, aligned_str2 = [], []
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i-1] == str2[j-1] and matrix[i][j] == matrix[i-1][j-1]:
            aligned_str1.append(str1[i-1])
            aligned_str2.append(str2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i-1][j] + 1:
            aligned_str1.append(str1[i-1])
            aligned_str2.append('-')
            i -= 1
        elif j > 0 and matrix[i][j] == matrix[i][j-1] + 1:
            aligned_str1.append('-')
            aligned_str2.append(str2[j-1])
            j -= 1
        else:
            aligned_str1.append(str1[i-1])
            aligned_str2.append(str2[j-1])
            i -= 1
            j -= 1
    
    # Reverse the aligned strings
    aligned_str1 = ''.join(reversed(aligned_str1))
    aligned_str2 = ''.join(reversed(aligned_str2))
    
    # Generate match report
    match_report = []
    matches = []
    mismatches = []
    for c1, c2 in zip(aligned_str1, aligned_str2):
        if c1 == c2 and c1 != '-':
            matches.append((c1, c2))
        elif (c1 != c2 or (c1 == '-' or c2 == '-')) and c1 != '-' and c2 != '-':
            mismatches.append((c1, c2))
    
    match_report.append(f"Aligned String 1: {aligned_str1}")
    match_report.append(f"Aligned String 2: {aligned_str2}")
    match_report.append(f"Matching characters: {', '.join(f'{m[0]}' for m in matches)}")
    match_report.append(f"Non-matching characters: {', '.join(f'{m[0]} vs {m[1]}' for m in mismatches)}")
    
    return match_report

def main():
    # Get input from command-line arguments or default to interactive input
    if len(sys.argv) == 3:
        str1, str2 = sys.argv[1], sys.argv[2]
    else:
        try:
            str1 = input("Enter the first string (6-10 characters): ").strip()
            str2 = input("Enter the second string (6-10 characters): ").strip()
        except EOFError:
            print("Error: No input provided. Use command-line arguments or run interactively.")
            return
    
    try:
        # Calculate similarity and get alignment matrix
        similarity, matrix = calculate_similarity(str1, str2)
        
        # Generate and display match report
        match_report = align_strings(str1, str2, matrix)
        
        print(f"\nSimilarity Percentage: {similarity:.2f}%")
        for line in match_report:
            print(line)
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()