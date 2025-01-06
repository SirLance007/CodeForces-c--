string = str(input())
if len(string) < 1000:
    word = [letter for letter in string]
    print(f"{word[0].upper()}{string[1:len(word)]}")

