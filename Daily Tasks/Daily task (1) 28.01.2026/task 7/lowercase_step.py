from step import Step

class LowercaseStep(Step):
    def run(self, data):
        return data.lower()