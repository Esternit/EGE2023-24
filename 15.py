import math

for a in range(1,1000):
    f=1
    for x in range(1,1000):
        f*=(((math.gcd(x,42)!=1)<=(math.gcd(x,7)==1)) or (x+a>=25))
        if f==0:
            break
    if f==1:
        print(a)
        break