data=[]
d={'0':0}

for s in open('22.txt'):
    data.append(s.replace(';',' ').split())

while len(data)+1!=len(d):
    for s in data:
        if all(sub in d for sub in s[2:]):
            d[s[0]]=int(s[1])+max(d[sub] for sub in s[2:])

print(max(d.values()))