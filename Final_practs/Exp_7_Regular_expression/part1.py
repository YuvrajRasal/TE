# 1. Names of the User.
import re
file = open('sample.txt','r')
text = file.read()
pattern = r'M(?:r\.|rs\.|s\.) [a-zA-Z]+'
names = re.findall(pattern,text)
print(names)