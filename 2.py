from itertools import *

def f(x,y,z,w):
    return (not(w<=x)) or (y<=z) or (not(y))

for a in product([0,1],repeat=7):
    t=[(0,1,a[0],a[1]),(a[2],0,a[3],1),(a[4],a[5],a[6],0)]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
                print(p)
