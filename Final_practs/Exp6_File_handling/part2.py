# Read contents of file and sort the data lexicographically and put it in another file.

# create and Enter 10 numbers in file1
print("Enter 10 numbers : ")
List1 = list()
fileWrite = open('file_2a.txt','w')
for i in range(10):
    List1.append(int(input("Enter number : ")))
    fileWrite.write(str(List1[i]))
    fileWrite.write("\n")
fileWrite.close()

#read from the file1 followed by sorting and printing
fileRead = open('file_2a.txt','r')
List2 = list()
for line in fileRead:
    List2.append(int(line))
    # List2.sort(key = len)
    List2.sort(key=lambda x: len(str(x)))  # imp change
List2.sort()
print(List2)

# Write in file 2 by looping new list iin file 1
fileWrite1 = open('file_2b.txt','w')
for i in range(len(List2)):
    fileWrite1.write(str(List2[i]))
    fileWrite1.write("\n")