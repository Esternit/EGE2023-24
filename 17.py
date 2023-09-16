file=open('17.txt')
lst=file.readlines()
mx=-1
for i in range(len(lst)):
    f=False
    if len(lst[i])>1 and lst[i][-2]=='0' and lst[i][-3]=='1':
        f=True
    lst[i]=int(lst[i])
    if f==True:
        mx=max(mx,lst[i])

mn=10**20
count=0
for i in range(len(lst)-1):
    if (lst[i]%2023)*(lst[i+1]%2023)>=mx:
        count+=1
        mn=min(mn,lst[i]+lst[i+1])

print(count,mn)