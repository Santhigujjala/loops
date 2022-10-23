n=int(input("enter the number"))
i=0
while n>0:
    rem=n%10
    i=i*10+rem
    n=n//10
print(i)