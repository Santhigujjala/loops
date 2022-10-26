#     1
#    21
#   321
#  4321
# 54321

i=1
while i<=5:
    k=0
    while k<=5-i:
        print(" ",end="")
        k=k+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    i=i+1
    print()