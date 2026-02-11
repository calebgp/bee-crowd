M = [[0.0 for _ in range(12)] for _ in range(12)]
t = input().strip()
soma = 0.0

for i in range(12):
    for j in range(12):
        M[i][j] = float(input())

count = 0

for i in range(5):
    for j in range(i+1, 11-i):
        soma += M[11 - i][j]
        count += 1

if t == 'S':
    print(f"{soma:.1f}")
else:
    media = soma / count
    print(f"{media:.1f}")