# FIX
i = 1
while not all(i % j == 0 for j in range(1, 21)):
    i += 1
print(i)
