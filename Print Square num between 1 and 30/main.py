list1 = [item for item in range(1, 31)]
def square_num(item):
    for counter in range(1,6):
        if item / counter == counter:
            return True

    return False


for item in list1:
    if square_num(item):
        print(item)