file=open('9.txt')
count=0
for i in range(6400):
    lst=file.readline().split()
    for k in range(len(lst)):
        lst[k]=int(lst[k])
    rep=[]
    nonrep=[]
    f=True
    for k in range(len(lst)):
        if lst.count(lst[k])>1:
            if lst.count(lst[k])==3:
                rep.append(lst[k])
            else:
                f=False
                break
        else:
            nonrep.append(lst[k])
    if f and len(rep)==3:
        if (sum(nonrep)/len(nonrep))<=sum(rep):
            print(lst)
            count+=1

print(count)