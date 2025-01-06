def count_lucky_digits(n):
    # Count the occurrences of lucky digits (4s and 7s) in the number
    count = str(n).count('4') + str(n).count('7')
    return count


def is_lucky_number(num):
    # Check if a number is a lucky number
    return all(digit in ('4', '7') for digit in str(num))


def is_nearly_lucky_number(n):
    # Check if a number is nearly lucky
    count = count_lucky_digits(n)
    return is_lucky_number(count)


# Example usage
n = int(input())
if is_nearly_lucky_number(n):
    print("YES")
else:
    print("NO")
