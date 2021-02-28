list1 = [5, 20, 15, 20, 25, 50, 20]

def remove_item(list1,value):
    return [item for item in list1 if item != value]

list2 = remove_item(list1,20)
print(list2)