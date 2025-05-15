def print_pares(arr):
    for x in range(len(arr)):
        print(f"par[{x}] = {arr[x]}")
def print_impares(arr):
    for x in range(len(arr)):
        print(f"impar[{x}] = {arr[x]}")
numbers = [int(input()) for x in range(15)]
par = []
impar = []
for x in numbers:
    if len(par) == 5:
        print_pares(par)
        par.clear()
    if len(impar) == 5:
        print_impares(impar)
        impar.clear()
    if x % 2 == 0:
        par.append(x)
        continue
    impar.append(x)
print_impares(impar)
print_pares(par)