def GCD(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


A = int(input())
s = 0
for i in range(2, A):
    t = A
    while t > 0:
        s += t % i
        t /= i
gcd = GCD(s, A - 2)
print('%d/%d' % (s / gcd, (A - 2) / gcd))
