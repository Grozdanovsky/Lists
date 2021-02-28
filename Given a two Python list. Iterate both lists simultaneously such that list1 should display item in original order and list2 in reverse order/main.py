list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for item in range(len(list1)):
    list2.reverse()
    print(f"{list1[item]} {list2[item]}")
    