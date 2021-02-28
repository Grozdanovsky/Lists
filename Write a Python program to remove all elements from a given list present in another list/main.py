list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2= [2, 4, 6, 8]

list3 = [item for item in list1 if item not in list2]

print(list3)

