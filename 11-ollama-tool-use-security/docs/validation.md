# Publication Validation

Validation date: October 19, 2026.

These checks validate the preserved application and publication package. They do not add trials to the historical nine-observation dataset.

- All three Python scripts compile in memory without syntax errors.
- All three scripts, four fictional documents, and nine original screenshots match the source bytes.
- Ten direct file-tool assertions cover four approved reads, unauthorized filename and traversal denials, and four invalid input types.
- Eight deterministic request-guard cases cover malformed structures, unexpected fields, invalid types, unauthorized deletion proposals, and the no-tool case. None dispatches a file read.
- Both unauthorized filenames stop before the summarization call.
- A mocked authorized read reaches summarization with the untrusted-document system instruction. A tool-shaped summary is printed as text, and the policy file remains unchanged.
- The existing `file_tools.py` self-test completes: the authorized policy is read and both unauthorized filenames are denied.
- All nine original/organized screenshot pairs have matching SHA-256 hashes; see the evidence manifest.
- Relative Markdown links are checked against the publication checkout.

The validation runner loads the agent definitions in memory and omits its module-level live example. It substitutes model responses to test Python control flow without contacting Ollama. No production code is changed and no destructive operation is executed. The separate directory-boundary check was inspected in source; the traversal test exercises the earlier filename allowlist, not that boundary check.

The live `test_ollama.py` connectivity script and fresh Llama 3 generation trials were not run during publication. The three-script syntax check and deterministic tests are not evidence of current Ollama availability or model resistance. An automated model experiment harness remains future work.

The source directory contains no Git metadata. Publication uses a separate clone of the existing remote `main` history, with changes scoped to `11-ollama-tool-use-security`. Prior research folders remain unchanged. Local environments, caches, secrets, and temporary validation scripts are excluded from the staged package. No credentials were observed in the reviewed scripts, documents, or screenshots.
