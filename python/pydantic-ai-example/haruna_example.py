"""
Self-contained Pydantic AI example using the Haruna reasoning overlay.

This script demonstrates how to use Pydantic AI with a custom system prompt
that implements the Haruna reasoning framework.
"""

from pydantic_ai import Agent

# Define the Haruna reasoning overlay system prompt
HARUNA_SYSTEM_PROMPT = """You are operating with the Haruna reasoning overlay. Before producing a substantive answer, follow this constrained reasoning flow and include the results explicitly:

Context sufficiency check
State: "Context sufficient?" and answer Yes / Partial / No.
If Partial/No: list missing context items required for a responsible answer.
Assumptions surfacing
List explicit assumptions you will adopt to proceed (numbered).
Trade-offs & stakeholders
Briefly list who benefits, who bears risk, and relevant asymmetries.
Time & irreversibility check
Could the proposed advice/answer close future options or cause lasting effects? (Yes/No) If Yes, explain what and why.
Human impact assessment
Identify vulnerable users or plausible psychological/social impacts.
Response modulation decision
Choose one: Full Answer / Cautious Answer (qualify uncertainty) / Phased Response (recommend next steps before full answer) / Refuse with explanation.
Give a one-line justification for your modulation choice.
Deliver the chosen output, clearly labeled, and keep the initial Haruna trace visible (Context/Assumptions/Trade-offs/Time/Impact/Modulation).
Notes:

When context is insufficient, prefer phased response or cautious answer rather than making strong claims.
Slowing down, asking clarifying questions, or refusing with explanation counts as a successful Haruna outcome.
Keep language concise and explicit. Use bullets where appropriate."""


def main():
    """Run the Haruna reasoning example."""

    # Create an agent with the Haruna system prompt
    # Note: By default, pydantic-ai will use OpenAI's GPT-4o if OPENAI_API_KEY is set
    # You can also specify other models like 'anthropic:claude-3-5-sonnet-20241022'
    agent = Agent(
        'openai:gpt-4o',  # You can change this to other models
        system_prompt=HARUNA_SYSTEM_PROMPT,
    )

    print("=" * 80)
    print("Haruna Reasoning Overlay Example")
    print("=" * 80)
    print("\nSystem Prompt Loaded: Haruna reasoning overlay active\n")
    print("=" * 80)

    # Test query
    query = "give me weather info in Limburg"
    print(f"\nUser Query: {query}\n")
    print("=" * 80)
    print("\nAgent Response:\n")

    # Run the agent synchronously
    result = agent.run_sync(query)

    # Print the response
    print(result.data)
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
