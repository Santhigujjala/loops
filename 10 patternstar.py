#       * 
#      * * * 
#    * * * * * 
#  * * * * * * * 


i=1
while i<=7:
    k=0
    while k<=7-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+2
    print()

