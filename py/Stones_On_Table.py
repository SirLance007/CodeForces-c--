n = int(input())
s = list(str(input()))
while 1 <= n <= 50:
    if "R" in s or "G" in s or "B" in s:
        selected_number = 0
        for i in range(len(s)-1):
            if s[i] == s[i + 1]:
                selected_number = selected_number + 1

        print(selected_number)
        break
