a=int(input("Enter amount:"))
coins=[500,200,100,50,20,10,5,2,1]
for i in coins:
    while(i<=a):
        print(i,end=" ")
        a=a-i
    
