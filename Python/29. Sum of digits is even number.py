list=[]
for i in range(100,201):
    i=str(i)
    sum=0

    for j in i:
        j=int(j)
        sum=sum+j
    
    if sum%2==0:
        list.append(i)

print('Sum Of Digits :',list)