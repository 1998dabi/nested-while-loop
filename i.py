a=int(input("enter number"))
r=1
while r<=a:
    j=1
    while j<=a-r:
        print(" ",end=" ")
        j=j+1
    c=1
    while c<=r:
        print(r,end=" ")
        c=c+1
    print()
    r=r+1