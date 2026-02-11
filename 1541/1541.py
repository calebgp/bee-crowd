import math
def calc_lado(x, y, z):
    area_casa = x * y
    area_necessaria = area_casa * (100/z)
    lado = int(math.sqrt(area_necessaria))
    return lado
while True:
    inp = input()
    if inp == "0":
        break
    x, y, z = map(int, inp.split())
    print(calc_lado(x, y, z))