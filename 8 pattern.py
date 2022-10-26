# * * * * 
# * 
# * 
# * 
# * * * 
# * 
# * 
# * * * * 




r=7
c=4
i=0
while i<=r:
    j=0
    while j<=c:
        if (i==0 and j!=0)or(i==7 and j!=4)or(i==4 and j!=0  and j!=4)or(i==5 and j==4)or(i==6 and j==4)or(i==1 and j==0)or(i==2 and j==0)or(i==3 and j==3):
            print("*",end=" ")
        else:
            print("",end="")
        j=j+1
    i=i+1
    print()
