n, k = map(int, input().split())
# k = int(input())
if 2 <= n <= 10 ** 9 and 1 <= k <= 50:
    for i in range(k):
        if n % 10 == 0:
            n = n / 10
        elif n % 10 != 0:
            n = n - 1

print(int(n))