Good catch — this is a **Markdown nesting issue**, not your fault.

### ❗ Why it happened

Inside your **big code block**, you have **other triple-backtick blocks** like:

````md
```bash
...
````

```env
...
```

````

Markdown **does not allow nested triple-backticks** of the same type.  
So when the renderer sees the inner ```bash or ```env, it **closes the outer block early**, which makes the **last 1–2 sections appear outside** the copied code segment.

That’s why you’re seeing “2 things below” rendered outside.

---

### ✅ The Fix (Correct + Safe)

When you want **ONE giant copy-paste block**, you must:

- Use **tildes `~~~` for the outer block**
- Keep **``` inside** for code examples

This is the **correct, render-safe version**.

---

## ✅ **FINAL — SINGLE COPY-PASTE BLOCK (100% SAFE)**

Paste **this entire thing as-is** 👇

~~~md
🔗 **Live Interactive Demo (Hugging Face Space)**  
https://huggingface.co/spaces/Suryansht21103/prooftrace

ProofTrace is an AI accountability and governance system that converts natural-language rules into **verifiable, replayable decision proofs**.  
Instead of trusting AI outputs blindly, ProofTrace generates structured artifacts that show *what rule was applied, how it was interpreted, what evidence was used, and whether the decision is trustworthy*.

---

## 🚨 The Core Problem

Modern AI systems:
- interpret rules implicitly
- generate answers without verifiable justification
- hallucinate evidence
- cannot be audited or replayed

When AI decisions are questioned (grading disputes, compliance violations, policy enforcement), there is **no machine-checkable proof** explaining *why* a decision was made.

---

## ✅ The ProofTrace Solution

ProofTrace treats AI reasoning as **data**, not text.

For every decision, it produces:
- rule-by-rule **PASS / FAIL / UNVERIFIABLE** outcomes
- exact quoted evidence
- deterministic verification of evidence
- replayable decisions under modified rules
- semantic diffs between decision outcomes

This turns AI decisions into **auditable infrastructure artifacts**.

---

## 🧠 What ProofTrace Does

### 1️⃣ Natural-Language Rule Interpretation
Rules written in plain English are parsed using **Gemini 3** into structured constraints.  
Ambiguous rules are explicitly marked as **non-enforceable**, with surfaced assumptions.

### 2️⃣ Deterministic Validation
Each rule is evaluated against the text and produces:
- status (`PASS / FAIL / UNVERIFIABLE`)
- exact evidence quote
- confidence score

### 3️⃣ Anti-Hallucination Verification
All evidence quoted by Gemini is verified in Python.  
If a quote does not exist in the source text, ProofTrace flags a **hallucination error**.

### 4️⃣ Replay & Semantic Diff
The same text can be re-evaluated under different rules.  
ProofTrace computes **rule-level diffs**, showing exactly what changed and why.

### 5️⃣ PQL (ProofTrace Query Language)
Decision proofs can be queried like data:
- `FAILED_RULES`
- `UNVERIFIABLE`
- `RULE:R1`

---

## 🧪 Technologies Used

- **Google Gemini 3** — reasoning & rule interpretation
- **Python** — deterministic verification layer
- **Gradio** — minimal interactive frontend
- **Hugging Face Spaces** — public demo hosting
- **pytest** — deterministic test suite

---

## ▶️ Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/suryanshbt211/prooftrace.git
cd prooftrace
````

### 2️⃣ Create `.env` File (**REQUIRED**)

Create a file named `.env` in the **ROOT** of the project directory
(the same level where `app.py` and the `app/` folder exist).

The file must contain:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ Notes:

* Do **NOT** place `.env` inside the `app/` folder
* Do **NOT** commit `.env` to GitHub
* The application automatically reads this file at runtime

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Interactive App

```bash
python app.py
```

The application will be available at:

```
http://localhost:7860
```

---

### 5️⃣ Run Deterministic Tests (No API Usage)

```bash
PROOFTRACE_TEST_MODE=1 pytest
```

This validates:

* rule parsing
* validation logic
* replay behavior
* PQL queries
* anti-hallucination detection

---

## 🌍 Live Demo Flow (What Judges See)

1. Paste rules
2. Paste text
3. Click **Run ProofTrace**

Instantly see:

* full decision proof (raw JSON)
* failed rules via PQL
* quoted & verified evidence

🔗 [https://huggingface.co/spaces/Suryansht21103/prooftrace](https://huggingface.co/spaces/Suryansht21103/prooftrace)

---

## 📈 Real-World Use Cases

* AI compliance & governance
* Education & grading audits
* Enterprise policy enforcement
* Content moderation verification
* Model evaluation & debugging
* Regulated AI deployments

---

## 💡 Why This Is Novel

ProofTrace is **not**:

* a chatbot
* a prompt wrapper
* a classifier
* RAG

It is **AI accountability infrastructure**.

Gemini is used as a **reasoning engine**, not a source of truth.
All outputs are **verified, replayable, and auditable** by deterministic code.

This combination does **not exist today as a usable product**.

```

---


```
