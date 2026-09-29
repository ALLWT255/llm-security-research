documents = [
    {
        "id": 1,
        "owner": "research-team",
        "text": "LLM applications should validate tool permissions."
    },
    {
        "id": 2,
        "owner": "research-team",
        "text": "Prompt injection can manipulate model behavior."
    },
    {
        "id": 3,
        "owner": "finance-team",
        "text": "CONFIDENTIAL: Finance API migration details."
    },
    {
        "id": 4,
        "owner": "hr-team",
        "text": "CONFIDENTIAL: Internal employee review information."
    }
]

CURRENT_USER_TEAM = "research-team"


def retrieve_documents(query, user_team):
    results = []

    for document in documents:

        # Authorization BEFORE retrieval
        if document["owner"] != user_team:
            continue

        if any(
            word.lower() in document["text"].lower()
            for word in query.split()
        ):
            results.append(document)

    return results


print("=== Secure Retrieval System ===")
print(f"Authenticated team: {CURRENT_USER_TEAM}")

query = input("Research query: ")

results = retrieve_documents(query, CURRENT_USER_TEAM)

print("\nRetrieved documents:")

if not results:
    print("No authorized matching documents found.")

for document in results:
    print(
        f'ID={document["id"]} | '
        f'OWNER={document["owner"]} | '
        f'TEXT={document["text"]}'
    )