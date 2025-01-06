x = int(input())
integers = [1, 2, 3, 4, 5]
while 1 <= x <= 1000000:
    starting_position = 0
    sum = 0
    if 1 <= x <= 5:
        print(1)
        break
    elif x == 0:
        print(0)
        break
    elif x > 5 and x % 5 == 0:
        sum = int(x / 5)
        print(sum)
        break
    elif x > 5:
        sum = int(x / 5) + 1
        print(sum)
        break
