import re

pattern = r"Colour"
text = "red Colour is my favourite and green Colour is my love"

match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

