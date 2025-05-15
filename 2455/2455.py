p1, c1, p2, c2 = map(int, input().split())
esquerda = p1 * c1
direita = p2 * c2
equilibrada = esquerda == direita

if equilibrada:
    print(0)
elif esquerda < direita:
    print(1)
else:
    print(-1)