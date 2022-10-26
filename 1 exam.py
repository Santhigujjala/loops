n=int(input("enter the number...."))
i=1
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
if sum%2!=0:
    print("odd number")
else:
    print("even number")
