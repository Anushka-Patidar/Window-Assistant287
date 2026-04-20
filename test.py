import re
text = "notepad,"
result = re.sub(r'(?!-\d)[!"#$%&\'()*+,\-./:;<=>?@\[\\\\]^_`{|}~]', "", text)
print(result)