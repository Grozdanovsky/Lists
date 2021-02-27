list1 = [1,1,2,4,5,6,7,8,9,9,9,1,1]
list2 = []

for item in list1:
    if item not in list2:
        list2.append(item)

print(list2)
