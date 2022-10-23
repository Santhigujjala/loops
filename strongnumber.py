n=int(input("enter the number"))
a=n
sum=0
while n>0:
    f=1
    i=1
    rem=n%10
    while i<=rem:
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if sum==a:
    print("strong numer")
else:
    print("not a strong number")