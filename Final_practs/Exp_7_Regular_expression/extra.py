import re
file = open('sample.txt','r')
text = file.read()

# for names
pattern_names = r'M\w*.\s*\w*\s*\w*[\n]'
pattern_email = r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+'
names1 = re.findall(pattern_names, text)
names = []
for i in names1:
 names.append(i[:-1])
print("Names are:")
for i in names:
 print(i)
print()

emails = re.findall(pattern_email, text)
print("Email addresses are:")
for i in emails:
 print(i)
print()

pattern_username = r'\S+.@'
pattern_domain = r'@\S+.'
usernames = re.findall(pattern_username, ' '.join(emails))
domains = re.findall(pattern_domain, ' '.join(emails))
print("Usernames and domains of each of the email addresses are:")
for i, j in zip(usernames, domains):
 print("User Id.: ", i[:-1], "; Domain: ", j[1:], sep="")
print()

# for numbers
pattern_number = r'[0-9]+[#\-*]*[0-9]+[#\-*]*[0-9]+'
numbers = re.findall(pattern_number, text)
print("Phone numbers are:")
for i in numbers:
 print(i)