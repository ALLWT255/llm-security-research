# Simulated LLM outputs
llm_outputs = [
    "SELECT name FROM research_projects;",
    "DROP TABLE research_projects;"
]


def execute_query(query):
    # SIMULATION ONLY — no real database is connected.
    print(f"[SIMULATED DATABASE EXECUTION] {query}")


print("=== Vulnerable LLM Output Handler ===")

for output in llm_outputs:
    print(f"\nLLM generated: {output}")

    # Vulnerability:
    # The application trusts the LLM output and sends it
    # directly to the downstream database handler.
    execute_query(output)