n=int(input("enter the number"))
a=n
p=len(str(n))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**p
    n=n//10
if sum==a:
    print("armstron number")
else:
    print("not armstron number")
