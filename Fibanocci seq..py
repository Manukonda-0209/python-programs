n=int(input())
a=0
b=1
c=a+b
print(a,"",b,end=" ")
while c<n:
    print(c,end=" ")
    a=b
    b=c
    c=a+b
