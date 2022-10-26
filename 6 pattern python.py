from zlib import Z_DEFAULT_STRATEGY


# p 
# p y 
# p y t 
# p y t h 
# p y t h o 
# p y t h o n 


user="python" 
v=len(user)
i=0
while i<v:
    j=0
    while j<=i:
        print(user[j],end=" ")
        j=j+1
    i=i+1
    print()
