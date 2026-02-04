class VowelsToStar:
    def transform(self, text):
        vowels = "aeiouAEIOU"
        result = ""
        for ch in text:
            if ch in vowels:
                result += "*"
            else:
                result += ch
        return result