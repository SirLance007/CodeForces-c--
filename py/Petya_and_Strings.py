string_1 = str(input()).lower()
string_2 = str(input()).lower()
while len(string_1) == len(string_2):
    if string_1 > string_2:
        print("1")
        break
    elif string_1 < string_2:
        print("-1")
        break
    else:
        print("0")
        break
