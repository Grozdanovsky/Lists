list1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
list2 = []
#list2 = [item for item in list1  if isinstance(item,list)   ]


for item in list1:
    if isinstance(item, list):
        for item2 in item:
            list2.append(item2)
    else:
        list2.append(item)

print(list2)

