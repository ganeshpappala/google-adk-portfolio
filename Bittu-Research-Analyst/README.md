Multi-Agent Research and Report Generation System
A multi-agent AI project built with Google Agent Development Kit (ADK) and Gemini. A main coordinator agent works with three specialized sub-agents to research a topic, analyze the findings, and prepare a technical report.
Project Overview
The project separates a complex task into focused responsibilities:
1. Researcher — gathers and organizes key concepts, facts, benefits, challenges, and examples about a topic.
2. Analyst — examines the research findings and identifies technical implications, advantages, limitations, use cases, and insights.
3. ReportWriter — turns the research and analysis into a structured technical report.
4. Main Agent (Bittu) — coordinates the available sub-agents and returns a response to the user.
Note: When the main agent is an LlmAgent with sub_agents, delegation is model-directed. The instructions guide the intended order, but do not by themselves guarantee that every sub-agent will always execute in a strict sequence.

Architecture
User
  |
  v
Main Agent (Bittu)
  |
  +--> Researcher
  |
  +--> Analyst
  |
  +--> ReportWriter
  |
  v
Final Technical Report
Project Structure
The project is organized with a separate Python file for each agent:
Bittu/
├── __init__.py
├── agent.py
├── Research_agent.py
├── Analyst_agent.py
└── Report_agent.py
- agent.py — defines the main agent and registers the sub-agents.
- Research_agent.py — defines the research agent (researcher).
- Analyst_agent.py — defines the analysis agent (analyst).
- Report_agent.py — defines the report-writing agent (report_writer).
- __init__.py — makes the Bittu folder a Python package for ADK to load.
Technologies Used
- Python
- Google Agent Development Kit (ADK)
- Gemini model
- Google AI API key
- Visual Studio Code (recommended editor)
Prerequisites
Before running the project, make sure you have:
- A supported Python version installed.
- Google ADK installed in your Python environment.
- A Google AI API key with access to the Gemini model configured in your code.
- A terminal such as PowerShell or the VS Code integrated terminal.
Setup and Installation
1. Clone the repository
After uploading this project to GitHub, clone it with:
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
Replace YOUR-USERNAME and YOUR-REPOSITORY with your GitHub username and repository name.
2. Create and activate a virtual environment (recommended)
On Windows PowerShell:
python -m venv adk-venv
.\adk-venv\Scripts\Activate.ps1
If PowerShell blocks activation, consult the Python documentation or use a terminal configuration permitted by your system. You can also run the environment's Python and commands directly without activating it.
3. Install Google ADK
python -m pip install --upgrade pip
python -m pip install google-adk
4. Configure your API key
Set your Google AI API key in PowerShell for the current terminal session:
$env:GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
$env:GOOGLE_GENAI_USE_VERTEXAI = "FALSE"
Replace the placeholder with your own key. Never commit your real API key to GitHub. If a key has been exposed publicly, revoke it and create a replacement.
5. Check the model name
The model configured in the agent files must be available to your Google AI account. If your code uses gemini-3.5-flash and the API reports that the model is unavailable, change the model setting to one currently supported by your account.
Run the Project
Run commands from the directory that contains the Bittu package.
Run in the terminal
adk run Bittu
Launch the ADK web interface
adk web --port 8000
Open this address in your browser:
http://127.0.0.1:8000
If port 8000 is already in use, try another port:
adk web --port 8001
Then open http://127.0.0.1:8001.
Example Prompt
Try asking the agent:
Research multi-agent AI systems, analyze the findings, and prepare a detailed technical report.

Other example topics include:
- Applications of generative AI in healthcare
- Benefits and limitations of retrieval-augmented generation (RAG)
- Multi-agent systems in business automation
- Comparing AI agent frameworks
How the Agents Work Together
1. The user submits a topic or report request.
2. The main agent determines which sub-agent to delegate to.
3. The Researcher prepares a structured research summary.
4. The Analyst evaluates the research and develops technical insights.
5. The ReportWriter produces a report using the information made available to it.
6. The main agent responds to the user.
The exact delegation behavior depends on the main agent's instructions, sub-agent descriptions, and the model's decisions. For strict, guaranteed step-by-step execution, consider using ADK's SequentialAgent workflow and passing intermediate results through session state (for example, with output_key).
Security
- Do not upload API keys, passwords, or other secrets.
- Keep local environment files out of version control.
- Consider adding a .gitignore file containing entries such as:
adk-venv/
.venv/
__pycache__/
*.py[cod]
.env
Troubleshooting
WinError 10048 — port already in use
Another process is using the selected port. Stop the other ADK server with Ctrl+C, or start ADK on a different port, for example:
adk web --port 8001
API key or authentication error
Check that GOOGLE_API_KEY is set in the same terminal where you start ADK, and confirm that the key is valid.
Model not found or unavailable
Check the model identifier in your agent files and replace it with a Gemini model supported by your Google AI account.
Import or package error
Check that all four Python files and __init__.py are inside the Bittu directory, and run ADK from the directory containing Bittu.
Learning Resources
- Google ADK documentation
- Google ADK multi-agent workflow patterns
- Google AI Studio
Future Improvements
- Use a deterministic sequential workflow to guarantee the research → analysis → report order.
- Store intermediate outputs using ADK session state.
- Add web-search tools for research that requires current sources.
- Add tests, structured output, and evaluation for report quality.
- Deploy the agent application for access beyond local development.
License
Choose a license before publishing if you want to specify how others may use, modify, and redistribute your project. If you do not add a license, GitHub may display the repository publicly, but that does not automatically grant others the usual open-source permissions to reuse your code. See Choose an open-source license.
