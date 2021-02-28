list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]




list3 = list1[0:list1.index(3)] + list2[:] + list1[list1.index(3)+1:]


print(list3)