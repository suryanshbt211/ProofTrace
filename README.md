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

Clone the ProofTrace repository from GitHub and navigate into the project directory.

Repository URL:  
https://github.com/suryanshbt211/prooftrace.git

---

### 2️⃣ Create `.env` File (REQUIRED)

Create a file named `.env` in the ROOT of the project directory  
(the same level where `app.py` and the `app/` folder exist).

The file must contain the following line:

GEMINI_API_KEY=your_gemini_api_key_here

Important notes:
- Do NOT place the `.env` file inside the `app/` folder
- Do NOT commit the `.env` file to GitHub
- The application automatically reads this file at runtime

---

### 3️⃣ Install Dependencies

Install all required Python dependencies listed in the `requirements.txt` file.

---

### 4️⃣ Run the Interactive App

Run the application using Python.

After startup, the app will be available at:  
http://localhost:7860

---

### 5️⃣ Run Deterministic Tests (No API Usage)

ProofTrace supports a deterministic test mode that does not use the Gemini API.

Enable test mode and run the test suite to validate:
- rule parsing
- validation logic
- replay behavior
- PQL queries
- anti-hallucination detection

---

## 🌍 Live Demo Flow

1. Paste rules  
2. Paste text  
3. Click **Run ProofTrace**

Instantly see:
- full decision proof (raw JSON)
- failed rules via PQL
- quoted and verified evidence

Live demo:  
https://huggingface.co/spaces/Suryansht21103/prooftrace

## 🛠️ Built With

### Languages
- **Python 3.13** — core implementation and deterministic verification layer

### AI & APIs
- **Google Gemini 3 (Gemini API)** — natural-language rule interpretation and reasoning
- **Gemini Flash** — lightweight reasoning for fast rule evaluation

### Frameworks & Libraries
- **Gradio** — minimal interactive frontend for public demonstration
- **pytest** — deterministic test suite for validation and replay logic
- **python-dotenv** — environment variable management
- **Pydantic** — structured data models for decision proofs

### Platforms
- **Hugging Face Spaces** — public interactive demo hosting
- **Local Python Runtime** — development and testing environment

### Architecture & Concepts
- **Hybrid AI + Deterministic Verification**
- **Replayable AI Decision Artifacts**
- **Anti-Hallucination Evidence Verification**
- **Semantic Diffing of AI Decisions**
- **AI Governance & Accountability Design**

### Tooling
- **Git** — version control
- **VS Code** — development environment


