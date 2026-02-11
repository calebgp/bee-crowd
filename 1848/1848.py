def piscada_binario(g):
    b = g.replace("*", "1").replace("-", "0")
    return int(b, 2)

for i in range(3):
    s = 0
    while True:
        a = input()
        if a == "caw caw":
            print(s)
            break
        s += piscada_binario(a)