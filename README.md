# 🧾 ProofTrace — Verifiable AI Decision Proofs

🔗 **Live Interactive Demo**  
https://huggingface.co/spaces/Suryansht21103/prooftrace  

ProofTrace is an AI governance and auditing system that converts natural-language rules into **verifiable, replayable, and auditable decision proofs**. Instead of trusting AI outputs blindly, ProofTrace produces structured artifacts that show *what rule was applied, what evidence was used, and whether the decision can be trusted*.

---

## 🚨 The Problem

Large Language Models are powerful but opaque. When asked to follow rules like:

- “Must not include personal data”
- “Do not hallucinate facts”
- “Ensure policy compliance”

models may *appear* compliant while producing:
- hallucinated evidence
- unverifiable reasoning
- non-replayable decisions

This makes AI unsafe for **regulated, enterprise, and high-stakes environments**.

---

## ✅ The Solution: ProofTrace

ProofTrace treats AI reasoning as **data**, not text.

It produces:
- rule-level decisions (PASS / FAIL / UNVERIFIABLE)
- exact quoted evidence
- deterministic verification
- replayable and diffable outcomes

Every AI decision becomes an **audit artifact**.

---

## 🧠 Core Capabilities

### 1️⃣ Natural-Language Rule Interpretation
Rules written in plain English are converted into structured constraints using **Gemini 3**, with explicit assumptions when ambiguity exists.

### 2️⃣ Deterministic Validation
Each rule is evaluated against the text and produces:
- status (PASS / FAIL / UNVERIFIABLE)
- exact evidence quote
- confidence score

### 3️⃣ Anti-Hallucination Verification
All evidence quoted by Gemini is **verified in Python**.  
If the quote does not exist in the source text, ProofTrace flags a hallucination.

### 4️⃣ Replay & Semantic Diff
The same text can be re-evaluated under new rules, and ProofTrace computes:
- what changed
- which rules changed
- why the decision differs

### 5️⃣ PQL (Proof Query Language)
Decision proofs can be queried like data:
- `FAILED_RULES`
- `UNVERIFIABLE`
- `RULE:R1`

---

## 🧪 Technologies Used

- **Google Gemini 3** — reasoning and interpretation
- **Python** — deterministic verification layer
- **Gradio + Hugging Face Spaces** — public interactive demo
- **pytest** — full deterministic test suite

---

## 📍 Live Demo (What Judges See)

1. Paste rules  
2. Paste text  
3. Click **Run ProofTrace**  
4. Instantly see:
   - decision proof JSON
   - failed rules
   - verified evidence

🔗 https://huggingface.co/spaces/Suryansht21103/prooftrace

---

## 📈 Real-World Use Cases

- AI compliance & governance
- Policy enforcement pipelines
- Education & grading audits
- Enterprise content moderation
- Model debugging & evaluation
- Regulated AI deployments

---

## 💡 Why This Is Novel

ProofTrace is **not**:
- a prompt wrapper
- a chatbot
- a classifier
- RAG

It is **AI accountability infrastructure**.

Gemini is used as a *reasoning engine*, not a source of truth.  
All outputs are verified, replayable, and auditable by code.

---

## 🧪 Testing

All core logic is fully testable without model calls:

```bash
PROOFTRACE_TEST_MODE=1 pytest


