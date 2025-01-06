n = int(input())
print(n)
# while len()
for _ in range(0, n):
    word = str(input()).lower()
    if " " not in word:
        if 10 < len(word) < 101:
            print(f"{word[0]}{len(word)-2}{word[len(word) - 1]}")
        else:
            print(word)

