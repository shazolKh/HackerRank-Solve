n, k = map(int, input().strip().split())
M = []
for i in range(n):
    # L = list(input())
    M.append(input())
count = 0

for i in range(n):
    for j in range(k):
        if M[i][j] == 'W':
            if i + 1 < n and M[i + 1][j] == 'P':
                count += 1
            elif j + 1 < k and M[i][j + 1] == 'P':
                count += 1
            elif i - 1 >= 0 and M[i - 1][j] == 'P':
                count += 1
            elif j - 1 >= 0 and M[i][j - 1] == 'P':
                count += 1
print(count)