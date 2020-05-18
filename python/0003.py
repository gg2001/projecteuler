import math
q = 600851475143


def p(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


a = max([x for x in range(2, int(math.sqrt(q))) if (p(x) and q % x == 0)])
print(a)
