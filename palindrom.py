n=int(input("enter the number"))
palindram=n
a=0
while n>0:
    rem=n%10
    a=a*10+rem
    n=n//10
if palindram==a:
    print("palindram number")
else:
    print("not a palindram number")   