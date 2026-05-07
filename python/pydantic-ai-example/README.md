# Haruna Reasoning Overlay - Pydantic AI Example

This is a self-contained example demonstrating the Haruna reasoning overlay using Pydantic AI.

## What is Haruna?

Haruna is a reasoning framework that encourages LLMs to follow a structured thinking process before providing answers, including:
- Context sufficiency checks
- Explicit assumptions
- Trade-off analysis
- Impact assessment
- Response modulation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

Alternatively, you can use other LLM providers supported by Pydantic AI (Anthropic, Gemini, etc.) by changing the model parameter in the script.

## Usage

Run the example:
```bash
python haruna_example.py
```

The script will:
1. Load the Haruna reasoning overlay system prompt
2. Ask a test question: "give me weather info in Limburg"
3. Display the agent's response following the Haruna reasoning framework

## Customization

You can modify the query in `haruna_example.py` to test different questions and see how the Haruna overlay affects the reasoning process.

To use a different model, change the model parameter:
```python
# For Claude
agent = Agent('anthropic:claude-3-5-sonnet-20241022', system_prompt=HARUNA_SYSTEM_PROMPT)

# For Gemini
agent = Agent('gemini-1.5-pro', system_prompt=HARUNA_SYSTEM_PROMPT)
```
