list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = []
for item in range(len(list1)):
    list3.append(list1[item]+list2[item])

print(list3)