def count_circles(array):
    s = 0
    for i in range(len(array)):
        if i == n-1:
            s += 1
            break
        if array[i+1] == array[i]:
            continue
        s += 1
    return s
n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
print(count_circles(arr))