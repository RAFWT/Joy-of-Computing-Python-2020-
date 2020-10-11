a=int(input())
deep=[]
for i in range(1,51):
  deep.append(i)
  
count=0
for i in range(a,50):
  if deep[i]%a==0:
    count=count+1
print(count,end="")
