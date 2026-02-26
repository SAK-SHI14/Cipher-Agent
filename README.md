# 🤖 Smol-Agents Industrial Autonomous System

A production-ready prototype of an AI agent that fetches, verifies, and reasons over live web data using the `smolagents` library.

## 🏗 Architecture Overview

The system follows a modular, tool-centric architecture:

```mermaid
graph TD
    A[User Request] --> B[Autonomous Agent]
    B --> C{Reasoning & Control}
    C -->|Search Snippets| D[Web Search Tool]
    C -->|Full Content Scrape| E[Web Fetcher Tool]
    C -->|Cross-validation| F[Fact Verifier Tool]
    D --> G[Live Web (DuckDuckGo/Tavily)]
    E --> H[Web Pages (BS4/LXML)]
    F --> I[Verdict & Confidence Score]
    I --> B
    B --> J[Grounded Factual Answer]
```

### 🧠 Core Components

1.  **Autonomous Agent (`agent.py`)**: Built with `CodeAgent`. Unlike traditional JSON-based tool callers, it writes and executes Python code to process data, which is more robust for multi-step reasoning.
2.  **Custom Tools (`agent/tools/`)**:
    *   `WebSearchTool`: Fetches real-time snippets from the web.
    *   `WebFetcherTool`: Performs deep content extraction to avoid shallow reasoning.
    *   `FactVerifierTool`: A specialized logic module to calculate consistency across multiple sources.
3.  **Config Management (`config.py`)**: Decouples model parameters and API keys from logic.

## 🧪 Demo Scenarios

The agent can answer complex, time-sensitive queries like:
- **RBI Interest Rates**: "Latest interest rate announced by RBI"
- **OpenAI Leadership**: "Current CEO of OpenAI"
- **Indian AI Policy**: "Recent AI regulation updates in India"

### Step-by-Step Tool Usage Example: `Current CEO of OpenAI`
1.  **Intent Identification**: Agent recognizes the need for current, real-time data.
2.  **Web Search**: Calls `web_search(query="Current CEO of OpenAI 2024")`.
3.  **Cross-Validation**: Scans 5+ snippets. If there's ambiguity (e.g., Nov 2023 drama), it calls `fetch_page_content` on a reliable source like `openai.com/news`.
4.  **Verification**: Calls `fact_verifier` with the gathered text to confirm "Sam Altman".
5.  **Final Response**: Returns the confirmed name with internal citations.

## 🎯 Design Decisions & Tradeoffs

- **Why `smolagents`?**: It's lightweight, extremely fast, and the `CodeAgent` approach reduces hallucination by requiring the model to write explicit extraction logic.
- **Why BS4 over simple search snippets?**: Snippets are often outdated or SEO-polluted. Fetching the full page ensures we reason over the actual source text.
- **Why a separate Verifier tool?**: Outsourcing verification to a tool with specific thresholds (keyword overlap, entity matching) provides a consistent "ground truth" metric for the agent.

## 🚀 Getting Started

1.  **Install dependencies**:
    ```bash
    pip install smolagents requests beautifulsoup4 duckduckgo-search python-dotenv lxml
    ```
2.  **Configure environment**: Rename `.env.example` to `.env` and add your `OPENAI_API_KEY`.
3.  **Run the demo**:
    ```bash
    python main.py
    ```
