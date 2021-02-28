
list1 = [{
    "keys": "key",
    "Jan": "January",
    "Feb": "Feb"

        }, {
    "Mar": "March",
    "Apr": "April",
    "May": "May"
}]
list2 = [{key: value for key, value in item.items() if key != "Jan"} for item in list1]
print(list2)


list3 =[]
for item in list1:
    for k,v in item.items():
        if k != "Jan":
            list3.append({k: v})

print(list3)











