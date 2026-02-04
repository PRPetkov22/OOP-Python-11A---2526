from command import Command

class AddTextCommand(Command):
    def __init__(self, document, text_to_add):
        self.document = document
        self.text_to_add = text_to_add
        self._prev_text = None

    def execute(self):
        self._prev_text = self.document[0]
        self.document[0] = self.document[0] + self.text_to_add

    def undo(self):
        if self._prev_text is not None:
            self.document[0] = self._prev_text