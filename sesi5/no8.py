a = 0 
b = 1
c = 2
d = a + b + c
for i in range(10):
    print(b, end=' ')
    d = a + b + c
    a = b
    b = c
    c = d