i=1
while i<=6:
    j=1
    while j<=6:
       if i==1:
        print("s",end="")
       elif j==1:
           print("k",end="")
       elif (j==5 and i==2)  or (j==4 and i==3) or (j==3 and i==4 ) or (j==2 and i==5) or (j==1 and  i==6):
           print("j",end="")
       else:
        print(" ",end="")
       j=j+1
    i=i+1
    print()
