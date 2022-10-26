# 1 
# 0 0 
# 1 1 1 
# 0 0 0 0 
# 1 1 1 1 1 

i=1
a=1
while i<=5:
    j=1
    while j<=i:
        if(i%2==0):
            print("0",end=" ")
        else:
            print(a,end=" ")
        j=j+1
    i=i+1
    print()