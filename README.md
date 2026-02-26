# 🔐 CIPHER: Multi-Agent Fact Intelligence Suite

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Library: smolagents](https://img.shields.io/badge/Library-smolagents-magenta.svg)](https://github.com/huggingface/smolagents)
[![Architecture: Autonomous Reasoning](https://img.shields.io/badge/Architecture-Autonomous--Reasoning-cyan.svg)](#-industrial-grade-architecture)

A professional-grade suite of autonomous AI agents designed for **High-Signal Fact Synthesis**. Built using Hugging Face's `smolagents` library, these agents move beyond simple chat by executing real-time Python logic to verify and compress web intelligence.

---

## 🏗️ The Intelligence Suite

| Agent | Purpose | Primary Interface |
| :--- | :--- | :--- |
| **🔐 CIPHER** | Industrial Intelligence Officer | Windows PowerShell (Optimized) |
| **🚀 AXIOM** | decision-ready Fact Synthesizer | Modern Terminal UI (Rich) |
| **🤖 PROTOTYPE** | Core Experimental Agent | Generic Python CLI |

---

## 🧠 Industrial-Grade Architecture

Unlike traditional chatbots that merely predict the next token, CIPHER and AXIOM follow a non-negotiable **Reasoning Pipeline**:

1.  **Intent Parsing**: Identifies if the objective requires live external awareness or deep synthesis.
2.  **Breadth Intelligence Scan**: Executes `web_search` to gather raw snippets from multiple news, official, and technical sources.
3.  **Cross-Sector Verification**: Uses a custom `verify_claims` engine. A fact is only "Verified" if confirmed by **at least 2 independent sources** through statistical consensus logic.
4.  **Signal Compression**: Strips background noise, repetition, and marketing language to produce a byproduct that is precisely **Signal-over-Noise**.

---

## 🔒 The Output Contract (STRICT)

Every result delivered by these agents must obey the **Senior Analyst Protocol**:
- **Maximum 5 Bullet Points**: Focused purely on high-impact facts.
- **Extreme Brevity**: Each bullet is strictly constrained to **<18-20 words**.
- **Zero Hallucination Guardrails**: If intelligence cannot be verified across 2+ sources, the agent returns: *"Insufficient verified data to produce a confident answer."*
- **No Filler**: No "according to," no "recently," and no URLs in the final intelligence byproduct.

---

## 🛠️ Modular Tool Design

-   **`web_search`**: High-performance snippet retrieval targeting high-authority domains.
-   **`fetch_page`**: Deep-target extraction scraper for full-page truth verification.
-   **`verify_claims`**: A specialized validation module using text-overlap and entity-matching consensus.

---

## 🚀 Deployment

### 1. Prerequisites
- Python 3.10+
- Hugging Face API Token (Read access) or OpenAI API Key.

### 2. Installation
```powershell
pip install -r cipher/requirements.txt
```

### 3. Launching **CIPHER** (PowerShell)
```powershell
./cipher/cipher.ps1
```

### 4. Launching **AXIOM** (Standard Terminal)
```powershell
python -m axiom.main
```

---

## 📘 Engineering Philosophy

This project represents a transition from **Generative AI** to **Agentic AI**. By utilizing the `CodeAgent` architecture, the agents write and execute their own Python logic to handle unstructured data. This makes them inherently more resistant to hallucination and far more capable than standard LLM-based assistants for high-stakes research.

---

### 🧪 Example Mission: "Latest RBI Repo Rate"
**Internal Reasoning:**
1. Agent identifies query needs live data.
2. Agent calls `web_search` for banking news.
3. Agent extracts "6.50%" from 4 independent sites.
4. Verifier tool confirms 4 matches -> `VERIFIED`.

**Final Byproduct (Signal):**
- Latest RBI repo rate: 6.50%
- Stance: Withdrawal of accommodation
- Effective since: February 2023 

*"This candidate understands how real AI agents work in production."*
