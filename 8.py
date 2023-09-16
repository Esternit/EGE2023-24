from itertools import *

count=0
for a in product('0123456',repeat=5):
    j=''.join(a)
    if j[0]!='0' and j.count('5')==1:
        if j.index('5')!=len(j)-1 and j.index('5')!=0:
            if int(j[j.index('5')-1])%2!=0 and int(j[j.index('5')+1])%2!=0:
                print(j)
                count+=1
        elif j.index('5')==len(j)-1:
            if int(j[j.index('5')-1])%2!=0:
                print(j)
                count += 1
        elif j.index('5')==0:
            if int(j[j.index('5')+1])%2!=0:
                print(j)
                count += 1
print(count)

