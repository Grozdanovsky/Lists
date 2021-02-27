list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

list1.sort(key=lambda item: item[1], reverse=False)

print(list1)
