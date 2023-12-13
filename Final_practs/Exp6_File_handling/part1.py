# create and Enter 10 numbers in file1
print("Enter 10 numbers")
List1 = list()
fileWrite = open("file1.txt", "w")
for i in range(10):
    List1.append(int(input("Enter number : ")))
    fileWrite.write(str(List1[i]))
    fileWrite.write("\n")
fileWrite.close()

#read from the file1 followed by sorting and printing
fileRead = open("file1.txt", "r")
List = list()
print(fileRead)
print(List)
for line in fileRead:
    List.append(int(line))
    List.sort()
print(List)

# Write in file 2 by looping new list iin file 1
fileWrite1 = open("file2.txt", "w")
for i in range(len(List)):
 fileWrite1.write(str(List[i]))
 fileWrite1.write("\n")

