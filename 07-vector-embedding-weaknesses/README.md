\# Attack 07 – Vector and Embedding Weaknesses



\## Objective



This lab demonstrates security weaknesses that can occur in retrieval and RAG-style systems when authorization and source trust are not enforced before documents are retrieved.



Two scenarios were tested:



1\. Cross-team retrieval leakage

2\. Retrieval poisoning



The goal was to reproduce each weakness, implement application-layer controls, and verify that legitimate retrieval continued to function.



All documents and data used in this lab were simulated.



\---



\## Part 1 – Cross-Team Retrieval Leakage



\### Normal Retrieval Baseline



A simplified retrieval system was created containing documents belonging to multiple teams:



\- Research team

\- Finance team

\- HR team



The simulated user belonged to the research team.



A normal research query was executed:



`LLM applications`



The system successfully returned a research-team document.



!\[Authorized Retrieval Baseline](01-authorized-retrieval-baseline.png)



\### Cross-Team Retrieval Test



The vulnerable retrieval function searched all available documents based on query matches without checking the owner of each document.



While operating as a research-team user, the following query was submitted:



`CONFIDENTIAL`



The retrieval system returned documents belonging to both the finance and HR teams.



This demonstrated that relevance-based retrieval without authorization filtering can expose information belonging to another user, group, or security context.



!\[Cross-Team Retrieval Leakage](02-cross-team-retrieval-leakage.png)



\### Authorization Mitigation



A secure retrieval function was implemented.



Before a document could be considered for retrieval, the application checked whether the document owner matched the authenticated user's team.



Unauthorized documents were excluded before query matching occurred.



The same `CONFIDENTIAL` query was executed again as the research-team user.



The system returned:



`No authorized matching documents found.`



Finance and HR documents were no longer exposed.



!\[Cross-Team Retrieval Blocked](03-cross-team-retrieval-blocked.png)



\### Authorized Retrieval Retest



The original legitimate query was executed against the secured retrieval system:



`LLM applications`



The authorized research-team document was still successfully returned.



This demonstrated that authorization filtering prevented cross-team leakage without breaking legitimate retrieval functionality.



!\[Authorized Retrieval Retest](04-authorized-retrieval-retest.png)



\---



\## Part 2 – Retrieval Poisoning



\### Vulnerable Retrieval Ranking



A second retrieval simulation was created containing trusted security documentation and an untrusted uploaded document.



The vulnerable retriever ranked documents based on query relevance without considering source trust.



The following query was submitted:



`Cloud credential reset procedure`



The untrusted uploaded document received the highest relevance score and ranked above the approved security documentation.



The poisoned document contained misleading credential-reset instructions.



!\[Retrieval Poisoning Success](05-retrieval-poisoning-success.png)



\### Source Trust Mitigation



The retrieval pipeline was modified so that untrusted documents were rejected before relevance ranking.



The same query was executed again.



The untrusted uploaded document was excluded, while only documents from the approved security guide were returned.



!\[Retrieval Poisoning Blocked](06-retrieval-poisoning-blocked.png)



\### Trusted Retrieval Retest



A legitimate query was then executed:



`Cloud credentials`



The system successfully retrieved the trusted security-guide documents while continuing to exclude the untrusted uploaded source.



!\[Trusted Retrieval Retest](07-trusted-retrieval-retest.png)



\---



\## Implementation



The lab contains three Python programs:



\### `vulnerable\_retrieval.py`



Demonstrates retrieval based on query relevance without enforcing document ownership.



\### `secure\_retrieval.py`



Adds authorization filtering so documents must belong to the authenticated user's team before they can be retrieved.



\### `retrieval\_poisoning.py`



Demonstrates source-trust filtering by rejecting untrusted documents before relevance ranking.



\---



\## Security Controls Demonstrated



The lab demonstrates several defensive principles:



\- Authorization before retrieval

\- Tenant/team isolation

\- Source trust validation

\- Filtering before relevance ranking

\- Separation of authorization from model behavior

\- Legitimate-functionality retesting after mitigation



\---



\## Key Finding



Retrieval relevance should not be treated as authorization or trust.



A document can be highly relevant to a user's query while still being unauthorized or originating from an untrusted source.



Access-control and trust decisions should therefore be enforced by the application before retrieved information is supplied to an LLM.



This demonstrates a defense-in-depth approach for RAG and retrieval-based AI applications.



\---



\## OWASP Mapping



This lab was developed while studying:



\*\*OWASP Top 10 for LLM Applications 2026 – LLM09: Vector and Embedding Weaknesses\*\*



The exercises focus on risks associated with cross-context retrieval leakage and retrieval-time poisoning in systems that use vector stores, embeddings, or retrieval-augmented generation.

