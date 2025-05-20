# print(min(max(False,-3,-4), 2,7))
# x = 56.236
# print("%2f%x")
# 5. What will be the output of the following Python code?

# class tester:
#     def __init__(self, id):
#         self.id = str(id)
# temp = tester(12)
# print(temp.id)
# def foo(x):
#     x[0] = ['def']
#     x[1] = ['abc']
#     return id(x)
# q = ['abc', 'def']
# print(id(q) == foo(q))

# list1 = [1,2,3,4]
# list2 = [2,4,5,6]
# list3 = [2,6,7,8]
# result = list()
# result.extend(i for i in list1 if i not in (list2+list3) and i not in result)
# result.extend(i for i in list2 if i not in (list1+list3) and i not in result)
# result.extend(i for i in list3 if i not in (list1+list2) and i not in result)

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 6:
#         break
#     else:
#         print(0)

# my_num : int = 56
# # print(type(my_num),my_num)
# # print(type(my_num),my_num.real)
# # print(type(my_num),my_num.imag)
# print(type(complex(my_num)), complex(my_num))

# x: str = """
# my
# name
# is Naghmana
# Imran
# """

# x : tuple = (1,2,3,"Java",2.4,3+2j)
# print(type(x),x)
# range tuple
# range k ander 3 cheezen hoty he
# star,end,step

# x:range = range(1,10,6)
# print(type(x),x)
# print(x.start)
# print(x.stop)
# print(x.step)
# for i in range(10):
#     print(i)
# x : list =[2,3,5,7,2,7,8]


# print(tuple(x))
# set
# x = {12,2,3,4,5,5}
# print(type(x),x)
# x.remove(4)
# print(x)

# frizenset
# x : frozenset = frozenset([1,2,4,5,6,7,7])
# print(x)
# Mapping type
# x: dict = {
#     "name": "naghma",
#     "age": 23,
#     "religon":"islam",
#     "languages":["python","typscript","java","AI"]
# }
# print(x["languages"][-1])
# print(x["languages"][-3])

# id function
# x =  [1,2,3] #mutable
# y = [1,2,3]

# print(x is y)
# my_string: str = "Hello World"

# modified_string: str = my_string.split("1")
# print(modified_string)
message : str = "Pakistan won all the matches of chamions trophy!,Pakistan"
message = message.replace("pakistan","India")

print(message)