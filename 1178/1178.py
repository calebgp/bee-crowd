x = float(input())
numbers = [x] * 100
for i in range(1, 100):
    numbers[i] = numbers[i-1] / 2
for i in range(100):
    print(f"N[{i}] = {numbers[i]:.4f}")