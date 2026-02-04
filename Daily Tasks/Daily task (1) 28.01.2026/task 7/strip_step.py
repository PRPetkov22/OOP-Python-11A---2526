from step import Step

class StripStep(Step):
    def run(self, data):
        return data.strip()