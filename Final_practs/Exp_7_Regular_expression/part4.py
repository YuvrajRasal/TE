import re
file = open('sample.txt','r')
text = file.read()
pattern = r'\d{1,5}.\d{1,3}.\d{1,5}'
phone = re.findall(pattern,text)
print(phone)