file=open('27_B_5142.txt')

n,m=map(int,file.readline().split())
lst=[]

for i in range(n):
    x,y=map(int,file.readline().split())
    lst.append([x,y])
lst.sort()
mx=-1
for i in range(len(lst)):
    if lst[i][0]>=m:
        okrug=[lst[i][1]]
        cur=lst[i][0]
        count=0
        for k in range(i-1,-1,-1):

            if cur-lst[k][0]<=m:
                okrug.append(lst[k][1])
            else:
                break
        for k in range(i+1,len(lst)):
            if lst[k][0]-cur<=m:
                okrug.append(lst[k][1])
            else:
                break
        for k in range(len(okrug)):
            if okrug[k]%50!=0:
                count+=okrug[k]//50+1
            else:
                count+=okrug[k]//50
        mx=max(mx,count)
    print(i)


print(mx)

