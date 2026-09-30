# Simulated LLM outputs
llm_outputs = [
    "SELECT name FROM research_projects;",
    "DROP TABLE research_projects;",
    "SELECT name FROM research_projects; EXEC dangerous_procedure;"
]

def validate_query(query):
    normalized = query.strip().upper()

    # Only read-only SELECT queries are permitted.
    if not normalized.startswith("SELECT "):
        return False

    blocked_keywords = [
        "DROP ",
        "DELETE ",
        "UPDATE ",
        "INSERT ",
        "ALTER ",
        "TRUNCATE "
    ]

    if any(keyword in normalized for keyword in blocked_keywords):
        return False

    return True


def execute_query(query):
    # SIMULATION ONLY — no database is connected.
    print(f"[SIMULATED DATABASE EXECUTION] {query}")


print("=== Secure LLM Output Handler ===")

for output in llm_outputs:
    print(f"\nLLM generated: {output}")

    if validate_query(output):
        print("ALLOWED - Output passed validation")
        execute_query(output)
    else:
        print("DENIED - Unsafe LLM output blocked")