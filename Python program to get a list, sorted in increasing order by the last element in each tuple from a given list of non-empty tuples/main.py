list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

list1.sort(key=lambda item: item[1], reverse=False)
# The sort works on a way that ITEM is used twice here because on the left hand of the colon it
# is the name of a parameter and on the right hand side it is being used in the code block to compute something.

print(list1)
