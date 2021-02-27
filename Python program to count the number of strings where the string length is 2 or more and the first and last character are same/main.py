list1 = ['abc', 'xyz', 'aba', '1221']
final = 0
for item in list1:
    if len(item) > 2 and  item[0] == item[-1]:
            final += 1


print(final)
