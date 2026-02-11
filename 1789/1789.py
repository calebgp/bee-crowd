while True:
    try:
        n = int(input())
        lesmas = list(map(int, input().split()))
        lesmamr = max(lesmas)
        print(3 if lesmamr >= 20 else 1 if lesmamr < 10 else 2)
    except EOFError:
        break