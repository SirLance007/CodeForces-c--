k, n, w = map(int, input().split())
if 1 <= k and w <= 1000 and 0 < n < 10 ** 9:
    total_dollars_needed = k * (w * (w + 1)) // 2  # Sum of arithmetic series
    dollars_needed_to_borrow = max(0, total_dollars_needed - n)
    print(dollars_needed_to_borrow)
else:
    print(0)
