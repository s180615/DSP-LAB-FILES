## Factorial of a number using functions
n=int(input("enter the number="))
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        print(f)
        fact()
