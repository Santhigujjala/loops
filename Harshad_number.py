n=int(input("enter the number:"))
s=n
sum=0
while s>0:
    rem=s%10
    sum=sum+rem
    s=s//10
if n%sum==0:
    print("harshad number")
else:
    print("not a harashad number")
