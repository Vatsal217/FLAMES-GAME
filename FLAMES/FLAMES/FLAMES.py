n1=input('ENter First Name: ')
n2=input('Enter Second Name: ')
count=0
for i in n1:
    for j in n2:
       if i==j:
           count=count+2

if count>0:
   list1=["F","L","A","M","E","S"]
   while len(list1)>1:
       c = count%len(list1)
       s = c-1
       if s>=0:
           l=list1[:s]
           r=list1[s+1:]
           list1=r+l
       else:
            list1=list1[:len(list1)-1]
   
   print(list1[0])
else:
    print('PLease try with other name')