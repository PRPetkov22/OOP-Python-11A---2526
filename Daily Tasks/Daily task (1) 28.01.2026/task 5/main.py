from key_value_parser import KeyValueParser

parser = KeyValueParser()

text = "a=1;b=2"
print(parser.parse(text))