ALLOWED_ACTIONS = {"delete_document"}
ALLOWED_FILES = {"temporary-notes.txt"}

def authorize_action(action, filename, human_approved=False):

    # Layer 1: Tool allowlist
    if action not in ALLOWED_ACTIONS:
        return "DENIED - Tool is not authorized"

    # Layer 2: Resource allowlist
    if filename not in ALLOWED_FILES:
        return "DENIED - File is not authorized for deletion"

    # Layer 3: Human approval for destructive action
    if not human_approved:
        return "DENIED - Destructive action requires human approval"

    return f'ALLOWED - {action}("{filename}")'


print("=== Excessive Agency Authorization Test ===")

print(
    authorize_action(
        "delete_document",
        "research-report-1.txt",
        human_approved=False
    )
)

print(
    authorize_action(
        "delete_document",
        "temporary-notes.txt",
        human_approved=False
    )
)

print(
    authorize_action(
        "delete_document",
        "temporary-notes.txt",
        human_approved=True
    )
)
print("\n=== Bulk Deletion Attack Test ===")

for i in range(1, 101):
    filename = f"research-report-{i}.txt"

    result = authorize_action(
        "delete_document",
        filename,
        human_approved=False
    )

    print(filename, "->", result)
print("\n=== Legitimate Action Retest ===")

result = authorize_action(
    "delete_document",
    "temporary-notes.txt",
    human_approved=True
)

print(result)