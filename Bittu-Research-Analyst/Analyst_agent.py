
from google.adk.agents import LlmAgent

analyst = LlmAgent(
    name="Analyst",
    model="gemini-3.5-flash",
    description="Analyzes research findings and identifies technical insights.",
    instruction="""
    Analyze the research findings provided in your task.

    Identify:
    1. Technical implications
    2. Advantages and limitations
    3. Practical use cases
    4. Important insights

    Explain your reasoning clearly.
    Do not invent facts or statistics.
    """,
)
