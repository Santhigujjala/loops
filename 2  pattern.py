#     1
#     222
#    33333
#   4444444
#  555555555


i=1
while i<=5:
    k=0
    while k<=5-i:
        print(" ",end="")
        k=k+1
    j=i
    while j>=1:
        print(i,end="")
        j=j-1
    m=2
    while m<=i:
        print(i,end="")
        m=m+1
    i=i+1
    print()
