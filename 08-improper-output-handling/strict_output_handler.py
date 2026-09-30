import re

llm_outputs = [
   "SELECT status FROM research_projects;",
    "DROP TABLE research_projects;",
    "SELECT name FROM research_projects; EXEC dangerous_procedure;"
]


def validate_query(query):
    normalized = query.strip()

    # Allow exactly one simple read-only query:
    # SELECT <column> FROM research_projects;
    pattern = r"^SELECT\s+[A-Za-z_][A-Za-z0-9_]*\s+FROM\s+research_projects;$"

    return bool(re.fullmatch(pattern, normalized, re.IGNORECASE))


def execute_query(query):
    # SIMULATION ONLY
    print(f"[SIMULATED DATABASE EXECUTION] {query}")


print("=== Strict LLM Output Handler ===")

for output in llm_outputs:
    print(f"\nLLM generated: {output}")

    if validate_query(output):
        print("ALLOWED - Output matches approved SQL structure")
        execute_query(output)
    else:
        print("DENIED - Output does not match approved SQL structure")