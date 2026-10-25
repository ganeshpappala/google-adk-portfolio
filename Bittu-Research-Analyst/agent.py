from google.adk.agents import LlmAgent

from .Research_agent import researcher
from .Analyst_agent import analyst
from .Report_agent import report_writer

root_agent = LlmAgent(
    name="Bittu",
    model="gemini-3.5-flash",
    description="Coordinates research, analysis, and report writing.",
    instruction="""
    You are the main coordinator.

    1. Call Researcher to research the user's topic.
    2. Call Analyst to analyze the research findings.
    3. Call ReportWriter to create the final report using
       the research and analysis.

    Return the final report to the user.
    """,
    sub_agents=[
        researcher,
        analyst,
        report_writer,
    ],
)