"""
https://www.codewars.com/kata/5583090cbe83f4fd8c000051
"""

def digitize(n):
    arr = list(str(n))
    reverse = arr[::-1]
    for i in range(0, len(reverse)):
        reverse[i] = int(reverse[i])
    return reverse

print(digitize(123456789))