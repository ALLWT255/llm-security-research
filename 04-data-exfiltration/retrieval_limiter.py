MAX_DOCUMENTS_PER_REQUEST = 5
MAX_DOCUMENTS_PER_SESSION = 10

session_total = 0


def authorize_retrieval(document_count):
    global session_total

    # Layer 1: Per-request limit
    if document_count > MAX_DOCUMENTS_PER_REQUEST:
        return "DENIED - Per-request retrieval limit exceeded"

    # Layer 2: Session limit
    if session_total + document_count > MAX_DOCUMENTS_PER_SESSION:
        return "DENIED - Session retrieval limit exceeded"

    session_total += document_count

    return f"ALLOWED - Session total: {session_total}"


while True:
    user_input = input(
        "Enter number of documents requested (or type exit): "
    )

    if user_input.lower() == "exit":
        break

    document_count = int(user_input)

    result = authorize_retrieval(document_count)

    print(result)