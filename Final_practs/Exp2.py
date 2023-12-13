#sqrt
a = int(input("Enter number : "))
sqrt = int(a**(1/2))
print(sqrt)

#perimeter
a = float(input("Enter legnth"))
b = float(input("Enter breadth"))
per = (a + b)
area = a*b
print(f"Perimeter is : {per}")
print(f"Area is : {area}")

#swapping of 2var using 3rd
a = input("enter name : ")
b = input("enter sirname : ")

print("without swap : "+ a + " " + b)
c= ""
c = a
a = b
b = c

print("with swap : "+ a + " " + b)

#swap using 2 var
a = int(input("enter name : "))
b = int(input("enter sirname : "))

print(f"without swap : {a} and {b}")
a = a+b #1+2 ...a=3
b = a-b #3-2 ...b=1
a = a-b #3-1 ....a=2

print(f"withswap : {a} and {b}")


#add elements in list [1, 2]['1', '2']
List = list()
List2 = list()
n = int(input("Enter number of elements you want to enter: "))
for i in range(n):
    List.append(int(input("Enter element int: ")))
    # List.append(input("Enter element : "))
    List2.append(input("Enter element str: "))
print(List)
print(List2)


#Add elements in Set {'we', '12'}
Set =set()
n = int(input("Enter number of elements"))
for i in range(n):
    Set.add(input("Enter element : "))
print(Set)

#Add elements in Tuple 
T = (1,2,3,4)
List =list(T)
n = int(input("Enter number of elements"))
for i in range(n):
    List.append(input("Enter element : "))
T = tuple(List)
print(T)

#Print the give triangle pattern using for loop.
h = int(input("Height of triangle : "))
for i in range(1,h+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    

#Print the give triangle pattern using for loop.
h = int(input("Height of triangle : "))
for i in range(1,h+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Print factorial of a number using for loop.
n = int(input("enter number : "))
fact =1
for i in range(1,n+1):
    fact = fact * i
print(fact)

# Print the Fibonacci sequence up to given 'n' value using for loop - wrong code
n = int(input("Enter number : "))
sum = 0 
first = 0
second = 1
for i in range(1,n-1):
    if(i<=2):
        print(sum,end=" ")
    sum = first + second
    print(sum, end=" ")
    first = second
    second = sum
# print(sum)

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example: Generate the first 10 Fibonacci numbers
n = 4
result = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {result}")

#Demonstrate 'while' loop with one example 

timer = int(input("enter timer : "))
while timer >0:
    print(timer,end=" ")
    timer-=1

n = int(input("enter number : "))
fact = 1
i = 1
while(i<n+1):
    fact = fact * i
    i+=1
print(fact)
    

    
# Demonstrate 'if...elif...else' loop with one exampl
# . Demonstrate 'continue', 'break' and 'pass' with one example each 
