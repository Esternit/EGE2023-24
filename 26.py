file=open('26.txt')
n=int(file.readline())
m=int(file.readline())
lst=[]
for i in range(n):
    lst.append(int(file.readline()))

lst.sort()
s=0
alr=[]
last=-1
for i in range(len(lst)):
    if s+lst[i]<m:
        s+=lst[i]
        alr.append(lst[i])
        last=i
    else:
        break
print(lst)
print(len(alr),sum(alr),alr)
num=m-(sum(alr)-alr[-1])
if num in lst:
    print(num)