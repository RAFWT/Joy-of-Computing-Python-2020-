n=int(input())
list_1=[]
for i in range(n):
    list_1.append(int(input()))
list_2=[] 
while list_1:
    minimum =list_1[0]
    for x in list_1:
      if x < minimum:
          minimum=x
    list_2.append(minimum)
    list_1.remove(minimum)
sarr = [str(a) for a in list_2]
print(' '.join(sarr),end='')
