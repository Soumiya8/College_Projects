#To write a program to display the first n terms of the fibonacci sequence usinf function
'''
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)


n = int(input("Enter the number of end limit : "))
for i in range (1,n+1):
    print(fib(i),end=",")'''
    
    
    
# Program to print the first n terms of the Fibonacci series using for loop

'''n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
'''

#sum of all even numbers
'''
n = int(input("Enter the number of terms: "))
sum = 0
for i in range(1,n+1):
    if i % 2 :
        sum += i
    else:
        sum += 0
print("The sum of all even numbers : ",sum)
'''

    
