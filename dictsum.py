a='ABCDSER'
sum=0
d={'A':1 ,'B':10 , 'C':100, 'D':1000}
for i in a:
    if(i in d.keys()):
        sum=sum+d[i]
print(sum)
