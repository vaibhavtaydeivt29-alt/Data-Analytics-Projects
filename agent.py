from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = LlmAgent(
    name = "Data_Analyst_Agent",
    model = "gemini-3-flash-preview",
    description="A data analyst that can write and execute Python code.",
    instruction= """
You are a data analyst. You can:
-Write Python code to analyze data
-Create calculations and statistics
-Solve math problems by runing code
-Generate data visualizations (describe the chart)

Always run code to verify answers before presenting them.
""",
   code_executor=BuiltInCodeExecutor(),
 )