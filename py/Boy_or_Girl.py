user_name = str(input())
distinct_numbers = set(user_name)
while len(distinct_numbers) <= 100:
    if len(distinct_numbers) % 2 == 0:
        print("CHAT WITH HER!")
        break
    else:
        print("IGNORE HIM!")
        break
