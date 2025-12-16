def f(n):
    if n <2:
        return n
    else:
        return n*f(n-1)
x = int(input("Enter the number"))
n = int(input("Enter the number 2"))
s=1
while n!=0:
    s += (x**n)/f(n)
    n = n-1
print(s)