count=0

for x in range(0,17):
    num1=1*17**4+4*17**3+9*17**2+x*17+3
    num2=x*17**3+6*17**2+1*17+2
    num3=x*17**3+5*17**2+4*17+x
    if (num1+num2-num3)%7==0:
        print(x)
print(count)