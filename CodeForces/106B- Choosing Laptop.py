n = int(input())
li = []
f = []
p = []
for i in range(n):
    l1 = list(map(int, input().split()))
    li.append(l1)

pr = [li[i][3] for i in range(n)]

for i in range(n):
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1] and li[i][2] < li[j][2]:
            pr[i] = 0
            break

for i in range(n):
    if pr[i] > 0:
        f.append(i)
        p.append(pr[i])

print(f[p.index(min(p))] + 1)
