s = str(input())
if 1 <= len(s) <= 100:
    total_upper_case = 0
    total_lower_case = 0
    for char in s:
        if char.isupper():
            total_upper_case += 1
        elif char.islower():
            total_lower_case += 1
    if total_upper_case > total_lower_case:
        print(s.upper())
    elif total_upper_case < total_lower_case:
        print(s.lower())
    else:
        print(s.lower())
