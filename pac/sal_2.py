from pac import sal

a = 1
b = 2
number = sal.sun_number(a, b)
assert number == a+b
print(f'{number} == {a+b}')