def Bit(n):
    if 1 <= n <= 150:
        X = 0
        for _ in range(n):
            num = str(input())
            if "X++" in num or "++X" in num:
                X = X + 1
            elif "X--" in num or "--X" in num:
                X = X-1
        return X


n = int(input())
result = Bit(n)
print(result)