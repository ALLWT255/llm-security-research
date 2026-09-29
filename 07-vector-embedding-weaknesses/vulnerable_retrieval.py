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

def retrieve_documents(query):
    results = []

    for document in documents:
        if any(word.lower() in document["text"].lower()
               for word in query.split()):
            results.append(document)

    return results


print("=== Vulnerable Retrieval System ===")

query = input("Research query: ")

results = retrieve_documents(query)

print("\nRetrieved documents:")

for document in results:
    print(
        f'ID={document["id"]} | '
        f'OWNER={document["owner"]} | '
        f'TEXT={document["text"]}'
    )