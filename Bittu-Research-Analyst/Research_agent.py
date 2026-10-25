
from google.adk.agents import LlmAgent

researcher = LlmAgent(
    name="Researcher",
    model="gemini-3.5-flash",
    description="Researches a topic and produces structured findings.",
    instruction="""
    Research the topic provided to you.

    Identify:
    1. Key concepts
    2. Important facts
    3. Benefits and challenges
    4. Practical examples

    Return a structured research summary.
    Do not invent facts or statistics.
    """,
)
