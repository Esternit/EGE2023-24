def conv(n):
    b=''
    while n>0:
        b=str(n%2)+b
        n=n//2
    if b.count('1')%2==0:
        b='10'+b[2:]+'1'
    else:
        b='1'+b[2:]+'11'
    return int(b,2)
for n in range(6,1000):
    r=conv(n)
    if r>100:
        print(n)
        break