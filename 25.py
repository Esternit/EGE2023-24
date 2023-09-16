from fnmatch import *

num=3200566
i=1
while num<10**10:
    if num%2023==0:
        i=2023
        if fnmatch(str(num),'32?056*6'):
            print(num,num//2023)
    num+=i