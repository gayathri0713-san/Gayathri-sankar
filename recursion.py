def abc(n):
    if(n==1):
        return  n 
    else:
        return n*abc(n-1)
x=abc(5)
print(x)
