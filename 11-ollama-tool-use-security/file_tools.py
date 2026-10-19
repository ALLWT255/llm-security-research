
from pathlib import Path

# Our approved test directory
SANDBOX = (Path(__file__).resolve().parent / "sandbox").resolve()

# Files the agent is allowed to read
ALLOWED_FILES = {
    "company_policy.txt",
    "spanish_test.txt",
    "french_test.txt",
    "german_test.txt"
}

def read_file(filename):
    # Check 1: The filename must be a string
    if not isinstance(filename, str):
        return "DENIED - Invalid filename"

    # Check 2: Only approved filenames are permitted
    if filename not in ALLOWED_FILES:
        return "DENIED - File is not authorized"

    # Check 3: Resolve the path and enforce directory boundary
    file_path = (SANDBOX / filename).resolve()

    if not file_path.is_relative_to(SANDBOX):
        return "DENIED - File is outside approved directory"

    # Read the actual test file
    try:
        return file_path.read_text(encoding="utf-8")
    except OSError:
        return "ERROR - Unable to read file"


# Test our tool directly
if __name__ == "__main__":
    print("=== Python File Tool Test ===")

    print("\nTEST 1 - Authorized file")
    print(read_file("company_policy.txt"))

    print("\nTEST 2 - Unauthorized file")
    print(read_file("private_records.txt"))

    print("\nTEST 3 - Directory traversal")
    print(read_file("../test_ollama.py"))
