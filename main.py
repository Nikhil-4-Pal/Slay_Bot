from rich import print
from agents.pipeline_v3 import run_pipeline_v3

topic = "Gen Z budgeting humor"
results = run_pipeline_v3(topic)
print(results)

