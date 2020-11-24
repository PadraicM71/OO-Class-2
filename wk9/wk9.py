# wk 9


# def fahrenheit(celsius):
#     return (9/5)*celsius + 32

# temps = [0, 22.5, 40, 100]

# print (temps)

# F_temps = map(fahrenheit, temps)

# #Show
# print (list(F_temps))



# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [9,10,11,12]

# print(list(map(lambda x,y:x+y,a,b)))

# # Now all three lists
# print(list(map(lambda x,y,z:x+y+z,a,b,c)))




# from functools import reduce

# lst =[47,11,42,13]
# print (lst)



# # print(reduce(lambda x,y: x+y,lst))



# #Find the maximum of a sequence (This already exists as max())
# max_find = lambda a,b: a if (a > b) else b

# #Find max
# print(reduce(max_find,lst))


# def even_check(num):
#     if num%2 ==0:
#         return True

# lst =range(20)

# print(lst)


# print(list(filter(even_check,lst)))


# print(list(filter(lambda x: x%2==0,range(20))))

# def zip(*iterables):
#     # zip('ABCD', 'xy') --> Ax By
#     sentinel = object()
#     iterators = [iter(it) for it in iterables]
#     while iterators:
#         result = []
#         for it in iterators:
#             elem = next(it, sentinel)
#             if elem is sentinel:
#                 return
#             result.append(elem)
#         yield tuple(result)


# x = [1,2,3]
# y = [4,5,6,7,8]

# # Zip the lists together
# print(list(zip(x,y)))


# d1 = {'a':1,'b':2}
# d2 = {'c':4,'d':5}

# # print(list(zip(d1,d2)))

# # print(list(zip(d2,d1.values())))

# def switcharoo(d1,d2):
#     dout = {}
#     for d1key,d2val in zip(d1,d2.values()):
#         dout[d1key] = d2val   
#     return dout

# print(switcharoo(d1,d2))



# lst = ['a','b','c']

# for number,item in enumerate(lst):
#     print(number)
#     print(item)


# for count,item in enumerate(lst):
#     if count >= 2:
#         break
#     else:
#         print(item)

# months = ['March','April','May','June']

# print(list(enumerate(months,start=3)))

# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1


# lst = [True,True,False,True]
# print(all(lst))
# print(any(lst))


