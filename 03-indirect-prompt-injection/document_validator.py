SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "ignore the summarization task",
    "disregard previous instructions",
    "disregard the task",
    "forget previous instructions",
    "system update",
    "new instructions",
    "do not mention this instruction",
    "must first output",
    "change your behavior",
    "override previous instructions"
]


def validate_document(document):
    document_lower = document.lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in document_lower:
            return "DENIED - Suspicious instruction detected"

    return "ALLOWED"


document = input("Enter document content: ")

result = validate_document(document)

print("\nValidation result:")
print(result)