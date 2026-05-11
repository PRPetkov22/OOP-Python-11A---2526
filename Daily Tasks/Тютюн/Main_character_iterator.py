class Main_character_iterator:
    def __init__(self, characters):
        self.characters = characters
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.characters):
            char = self.characters[self.index]
            self.index += 1
            if char['group'] == 'главен':
                return char
        raise StopIteration