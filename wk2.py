





list1 = [1,2,3]
list1.append(4)
print (type(list1))
print(list1[3])



dict = {"name":"John Doe", "age": 21, "net worth": 5213.4}
#essentially a JSON file - can pretty up if like on different lines.
print (dict)
print(dict ["net worth"]) #refer to name of variable - whats inside sq brackets is a predicate



dict2 = [
        {"name":"Jack", "age": 24, "net worth": 2345},
        {"name":"paul", "age": 34, "net worth": 5645}
        ]
print (dict2[1]["name"])

