def adding_num(item1, item2):

    return item1 + item2

list1 = [2, 4, 7, 0, 5, 8]
list2 = [3, 3, -1, 7]
list3 = []

for item in range(len(list1)):
    if item < len(list2):
        list3.append(adding_num(list1[item], list2[item]))

    else:
        list3.append(adding_num(list1[item], 0))

print(list3)