#      1
#     12
#    123
#   1234
#  12345


i=1
while i<=5:
    k=0
    while k<=5-i:
        print("",end=" ")
        k=k+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i+1
    print()