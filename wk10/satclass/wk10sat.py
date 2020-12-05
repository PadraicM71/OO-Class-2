#Exercises

s = 'hello'
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])


my_list = [0,0,0]
my_list1 = []
my_list1 = my_list1 +[0]
my_list1 += [0]
my_list1.append(0)

print(my_list)
print(my_list1)

list3 = [1,2,[3,4,'hello']]
print(list3)
list3[2].pop()
list3[2].append('goodbye')
print(list3)
# print (list3[2][2])

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])




