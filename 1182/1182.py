M = [[0.0 for _ in range(12)] for _ in range(12)]
I = int(input())
t = input().strip()
soma = 0.0

for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
        if j == I:
            soma += M[i][j]

if t == 'S':
    print(f"{soma:.1f}")
else:
    print(f"{soma / 12:.1f}")
    