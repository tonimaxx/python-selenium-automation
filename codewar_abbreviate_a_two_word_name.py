# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    x = name.split()
    return x[0][0].upper()+'.'+x[1][0].upper()

print(abbrev_name("Sam Harris"))
print(abbrev_name("Jarus Soontornsing"))
