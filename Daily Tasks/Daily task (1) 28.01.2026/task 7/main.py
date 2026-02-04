from lowercase_step import LowercaseStep
from strip_step import StripStep
from pipeline_runner import run_pipeline

steps = [
    StripStep(),
    LowercaseStep()
]

text = "HeLLo WoRLD"
result = run_pipeline(steps, text)

print(result)