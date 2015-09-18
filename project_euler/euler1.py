three_array = []
five_array = []
three_array_add = 0
five_array_add = 0

for x in range(0, 1000):
        if x % 3 == 0:
            three_array.append(x)

for x in three_array:
    three_array_add += x

for x in range(0, 1000):
        if x % 5 == 0 and x % 3 != 0:
            five_array.append(x)

for x in five_array:
    five_array_add += x

final = three_array_add + five_array_add

print final
