def first_non_unique(string):
    string = list(string.lower())

    try:
        for n in string:
            if string.count(n) == 1:
                to_return = n
                break
        return to_return
    except:
        return ""

print(first_non_unique("Google"))
print(first_non_unique("Amazon"))
print(first_non_unique("Aaabbcccc"))