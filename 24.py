file=open('24.txt')
line=file.readline()

gl=['A','E','U']
mx=-1
for i in range(len(line)):
    if line[i] not in gl:
        k=i
        count=0
        while k<len(line)-2:
            if line[k] not in gl and line[k+1] in gl and line[k+2] not in gl:
                count+=1
                k+=3
                mx=max(mx,count)
            else:
                break
print(mx)
