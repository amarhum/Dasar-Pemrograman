a = 0
b = 1
c = a+b
for i in range(10):
    print(c,end=' ')
    c=a+b
    a = b
    b = c