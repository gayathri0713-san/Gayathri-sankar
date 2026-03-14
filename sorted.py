name=['GAYU','VARUN','KAVIYA','PRIYA']
age=[22,24,20,19]
loc=['CHEENAI','MADURAI','PONDY','TRICHY']
res =list(zip(age,name,loc))
res1=sorted(res)
for i in range(4):
    print("{}.{} age is {} lives in{}".format((i+1),res1[i][1],res1[i][0],res1[i][2]))
