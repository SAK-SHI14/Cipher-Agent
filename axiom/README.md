# 🚀 AXIOM: Live Fact-Synthesis Engine

AXIOM is an industrial-grade **Fact-Compression Agent** built using the `smolagents` library. It is designed to navigate the web, extract factual claims, cross-verify them, and compress the signal into high-density, decision-ready answers.

## 🏗 Industrial-Grade Architecture

Unlike traditional chatbots that merely "chat," AXIOM follows a strict **Reasoning Pipeline**:

1.  **Intent Parsing**: Identifies if live data is necessary or can be answered concisely.
2.  **Breadth Search**: Uses `web_search` to gather raw snippets from multiple news/official sources.
3.  **Depth Retrieval**: If snippets are shallow, it uses `fetch_content` for full-page scraping of high-signal URLs.
4.  **Signal Extraction**: Isolates key facts (dates, names, percentages).
5.  **Multi-Source Verification**: Runs claims through `verify_facts`. A common consensus with **minimum 2 independent matches** is required for "Verified" status.
6.  **Fact Compression**: Synthesis into exactly 3-5 bullets, adhering to a strict <20-word-per-line contract.

## 🧠 Why AXIOM is Different From a Chatbot

| Feature | Standard Chatbot | AXIOM Agent |
| :--- | :--- | :--- |
| **Data Source** | Pre-trained Knowledge | Live Web Real-time |
| **Trust Model** | "I believe..." (Hallucination risk) | "Verified via [Source 1, Source 2]" |
| **Output Style** | Conversational / Verbose | High-Signal / Bulleted / Compressed |
| **Processing** | Text Prediction | Systematic Logic Execution (Python) |

## 🛠 Modular Tool Design

-   **`web_search`**: High-performance snippet retrieval via DuckDuckGo.
-   **`fetch_content`**: Deep crawler using BS4/LXML for full-page truth extraction.
-   **`verify_facts`**: A custom validation module for cross-referencing claims across disjoint sources.

## 🚀 Local Installation

1.  Clone the repository and install dependencies:
    ```bash
    pip install -r axiom/requirements.txt
    ```
2.  Set up environment:
    ```bash
    echo "MODEL_ID=Qwen/Qwen2.5-72B-Instruct" > .env
    echo "HF_TOKEN=your_huggingface_token_here" >> .env
    ```
3.  Execute AXIOM:
    ```bash
    python -m axiom.main
    ```

## ⭐ Engineering Philosophy

AXIOM operates under one core principle: **Information should be synthesized, not just retrieved.** By using `CodeAgent`, AXIOM can write and debug its own Python logic to process unstructured web data, making its research output more reliable than any static LLM response.
",
