# 🔐 CIPHER: Autonomous Fact Intelligence Agent

CIPHER is a PowerShell-native, industrial-grade autonomous agent built using `smolagents`. Designed for high-signal intelligence gathering, it automates the process of fetching, verifying, and distilling web data into decision-ready bullets.

## 🛠 Command-Center Architecture

CIPHER operates as a **Logic-First Agent**, using a strict **Intelligence Pipeline**:

1.  **Intent Parsing**: Recognizes if the objective requires live external awareness.
2.  **Intel Scan**: Executes `web_search` to gather raw snippets from various intelligence sectors.
3.  **Cross-Sector Verification**: Uses `verify_claims` to check consensus. A fact is only "Verified" if confirmed by **at least 2 independent sources**.
4.  **Signal Compression**: Strips background noise and compresses the byproduct into exactly 1-5 bullet points (<18 words each).

## 🏢 Why CIPHER?

| Requirement | Chatbot | CIPHER Agent |
| :--- | :--- | :--- |
| **UX Target** | Web Browser / Casual | PowerShell / Professional |
| **Logic** | Text Prediction | Systematic Code Execution |
| **Trust Layer** | None | Multi-Source Verify & Distill |
| **Constraint** | Verbose | <18 Words / Non-negotiable |

## 🚀 Deployment in PowerShell

1.  **Setup Environment**:
    ```powershell
    # Add your keys to .env
    MODEL_ID=Qwen/Qwen2.5-72B-Instruct
    HF_TOKEN=your_huggingface_token_here
    ```

2.  **Install Requirements**:
    ```powershell
    pip install -r cipher/requirements.txt
    ```

3.  **Launch Mission**:
    ```powershell
    ./cipher.ps1
    ```

## 🧠 Engineering Philosophy

CIPHER behaves like a **Command-Line Intelligence Officer**. It uses the `CodeAgent` architecture to write real-time extraction logic, which is inherently more resistant to hallucination than standard conversational AI. This makes CIPHER suitable for **Competitive Intelligence**, **Compliance Monitoring**, and **Strategic Decision Support**.
