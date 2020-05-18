a = 0
x, y = 0, 1
while x <= 4000000:
    if x % 2 == 0:
        a += x
    x, y = y, x + y
print(a)
