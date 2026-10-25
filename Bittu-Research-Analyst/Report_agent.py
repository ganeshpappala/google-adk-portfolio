
from google.adk.agents import LlmAgent

report_writer = LlmAgent(
    name="ReportWriter",
    model="gemini-3.5-flash",
    description="Creates a final technical report from research and analysis.",
    instruction="""
    Use the research and analysis provided in your task
    to create a professional technical report.

    Include:
    1. Title
    2. Introduction
    3. Research findings
    4. Technical analysis
    5. Benefits and challenges
    6. Practical use cases
    7. Conclusion

    Do not invent facts or statistics.
    Mention uncertainties when appropriate.
    """,
)
