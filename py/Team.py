n = int(input())
if 1 <= n <= 1000:
    for _ in range(n):
        x = 0
        for _ in range(n):
            a = int(input())
            b = int(input())
            c = int(input())
            print(f"{a} {b} {c}")
            if a and b == 1 or b and c == 1 or c and a:
                x = x + 1
        print(x)
