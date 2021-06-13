import re

pattern = r"Colour"
text1 = "I love red Colour and I hate yellow Colour"
text2 = re.sub(pattern, "color", text1)

print(text2)