def can_divide_watermelon(weight):
    if weight > 2 and weight % 2 == 0:
        return "YES"
    else:
        return "NO"


w = int(input())

result = can_divide_watermelon(w)

print(result)
