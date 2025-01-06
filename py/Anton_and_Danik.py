n = int(input())
results = input()

if 1 <= n <= 10 ** 5:
    Anton_wins = results.count("A")
    Danik_wins = results.count("D")

    if Anton_wins > Danik_wins:
        print("Anton")
    elif Anton_wins < Danik_wins:
        print("Danik")
    else:
        print("Friendship")
