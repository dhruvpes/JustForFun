from functools import reduce

ls = [1, 2, 3, 4, 5, 6, 7]

def add(x, y):

    # print("The result is", x+ y)
    return x+y

x = reduce(add, ls)

print(x)

def isGreaterThanFour(x):

    return x>4

squared_list = list(map(lambda x: x**2 ,  ls))
print(squared_list)

filtered_list = list(filter(lambda x: x%2 != 0 , ls))
print(filtered_list)

greater_list = list(filter(lambda x: isGreaterThanFour(x) == 1, ls))
print("Greater list is", greater_list)