n=int(input("enter the n number="))
x=int(input("enter the power number="))
def power(x,n):
    if(n==0):
        return 1
    else:
        return(x*power(x,n-1))
print(power(x,n))
    
