name=["gayathri","sandhiya","kaviya","suji","priya"]
marks=[[67,35,61],[88,54,32],[90,44,89],[76,99,24],[77,55,44]]
for i in range (5):
    total=sum(marks[i])
    per = total/3
    
    if per>90:
        Grade = 'S'
    elif  per>60 and per<90:
        Grade = 'A'
    elif per>40 and  per<60:
        Grade ='B'
    else:
        Grade = 'F'
        
    print("{}.{}-{}%-Grade {}".format(i+1,name[i],per,Grade))
