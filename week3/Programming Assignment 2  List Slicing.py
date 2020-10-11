a,b=input().split()
a=int(a)
b=int(b)
list=[]
for i in range(1,51):
   list.append(i)
for i in list[a:b]:
   print(i,end="\n")