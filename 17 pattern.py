    #       *
    #     * * *
    #   * * * * *
    #     * * *
    #       *


i=1
while i<=5-1:
    k=0
    while k<=5-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+2
    print()
i=5
while i>=1:
    k=0
    while k<=5-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i-2
    print()
