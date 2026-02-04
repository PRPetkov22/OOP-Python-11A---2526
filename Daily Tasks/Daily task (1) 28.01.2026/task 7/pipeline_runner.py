def run_pipeline(steps, text):
    data = text
    for step in steps:
        data = step.run(data)
    return data
