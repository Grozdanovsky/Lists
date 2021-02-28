list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
# expected output ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

for item in list1:
    for item2 in list2:
        list3.append(item+item2)


print(list3)


