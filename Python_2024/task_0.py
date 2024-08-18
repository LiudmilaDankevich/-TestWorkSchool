# array = [50, 1000, 3, 75, -45, 223, -500]
# array_copy = array[:]
# array.sort()
# print(array)
# print(array_copy)
# print(sorted(array_copy))
#
# array = [100, 300, 750, 430, 230, 555, 970]
# # print("max()", max(array))
# max_1 = max(array)
# print(max_1)
# print("min()", min(array))
# print("sum()", sum(array))

# a = [10, 20, 30, 40]
# for i in enumerate(a):
#     print(i)
# b = "hello"
# for i in enumerate(b):
#     print(i)
# c = {1: 'a', 2: 'b', 3: 'c'}
# for i in enumerate(c):
#     print(i)

# row = [[0] * 3]
# matrix = row * 2
#
# print('Полный список:', matrix)
#
# for row in matrix:
#     print(row)
#
# l = [0, [0,1,2], 5]
# print(l)
# l[2] = 6
# print(l)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
#
# print(all([True, 5, 3.5, 'String']))
#
# print(any([False, None, 0, ""]))
#
# d = {}
# print(d)
# d = {'dict': 1, 'dictionary': 2}
# print(d)
#
# fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
# dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
# fishdog = {**fish, **dog}
# fd = {*fish, *dog}
# print(fd)

# a = {'Honey': 10, 'Flour': 200, 'Eggs': 2, 'Mustard': None}
# print(a)
# a['Water'] = 200  # Добавление элемента в словарь
# print(a)

# a = {'Honey': 10, 'Flour': 200, 'Eggs': 2, 'Mustard': None}
# del a['Mustard']
# h = a.pop('Honey')
# print(a)
# print(h)

fib1 = 0
fib2 = 1
i = 4
while i < 20:
    sum = fib1 + fib2
    print(sum)
    fib1 = fib2
    fib2 = sum
    i +=1

fib1 = 0
fib2 = 1
i = 1
while i < 20:
    sum = fib1 + fib2
    if i > 5:
        print(sum)
    # print(sum)
    fib1 = fib2
    fib2 = sum
    i +=1

