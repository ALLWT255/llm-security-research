# Indirect Prompt Injection and Document Validation

## Objective

The purpose of this lab was to test how an LLM responds to malicious instructions embedded inside untrusted document content and to evaluate prompt-level and application-level mitigation techniques.

## Environment

- Ollama
- Llama 3
- Python
- Windows
- Local testing environment

## Test 1 - Clean Document Baseline

Llama 3 was configured as a document summarization assistant.

A normal research document was provided and the model successfully summarized the legitimate content.

**Result: PASS**

## Test 2 - Indirect Prompt Injection

A malicious instruction was embedded inside a document being processed by the LLM.

The document attempted to override the summarization task and instructed the model to output a different response.

The model followed the instruction contained inside the untrusted document instead of completing its assigned summarization task.

**Result: FAIL**

This demonstrated an indirect prompt injection vulnerability.

## Test 3 - Prompt-Level Mitigation

The model was given additional security instructions establishing a boundary between trusted application instructions and untrusted document content.

Instructions contained inside the document were explicitly defined as untrusted data that should not control the model's behavior.

The malicious document was tested again.

**Result: PASS**

The model ignored the embedded instruction and summarized the legitimate research content.

![Prompt mitigation successfully blocks indirect injection](02-prompt-mitigation-success.png)

## Test 4 - Application-Level Document Validation

A Python document validator was created to inspect untrusted content before it is processed by the LLM.

The validator searches for suspicious instruction patterns that may indicate prompt injection.

![Document validator implementation](03-document-validator-code.png)

An obvious malicious instruction was successfully detected and denied.

**Result: PASS**

## Test 5 - Validator Bypass

The malicious instruction was reworded using different terminology.

The original validator did not recognize the new wording and allowed the document.

**Result: FAIL - False Negative**

This demonstrated a limitation of simple keyword-based security controls.

## Test 6 - Improved Document Validation

Additional suspicious instruction patterns were added to the validator.

The previously successful bypass and another malicious variation were tested again.

Both were denied.

**Result: PASS**

![Malicious document denied](04-malicious-document-denied.png)

## Test 7 - Legitimate Document

A normal research document containing no malicious instructions was tested against the improved validator.

The document was allowed.

**Result: PASS**

![Legitimate document allowed](05-legitimate-document-allowed.png)

## Security Flow

The final design uses multiple security layers:

1. Treat external documents as untrusted data.
2. Separate trusted application instructions from document content.
3. Validate documents before sending them to the LLM.
4. Restrict the LLM to its intended task.
5. Continue testing for alternative prompt injection techniques.

## Key Findings

This lab demonstrated that malicious instructions embedded inside untrusted data can influence an LLM even when the application's intended task is only document summarization.

Prompt-level mitigation improved the model's resistance to the tested indirect injection attacks, but model instructions alone should not be treated as a complete security boundary.

Application-level document validation provided another layer of protection. However, the first validator produced a false negative when the attack was reworded, demonstrating that simple keyword matching can be bypassed.

The experiment reinforces the importance of defense in depth when processing untrusted content with LLM applications.
