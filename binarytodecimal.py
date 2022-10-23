n=int(input("enter the number"))
a=0
i=1
while n>0:
    r=n%10
    a=a+(r*i)
    i=i*2
    n=int(n/10)
print(a)



# n=int(input("eter the binary values"))  
# a=0
# i=1
# while n>0:
#     r=n%2
#     a=a+(r*i)
#     i=i+2
#     n=(n/2)
# print(a)   