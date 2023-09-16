for n in range(1,1000):
    s='>'+'1'*15+n*'2'+16*'3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s=s.replace('>1','22>',1)
        if '>3' in s:
            s=s.replace('>3','13>',1)
        if '>2' in s:
            s=s.replace('>2','1000>3',1)
    if (s.count('1')+s.count('2')*2+s.count('3')*3)%len(s)==0:
        print(n)
        break