import time;
# from math import sqrt , pi
import math
from function import welcome , name


# print('hello world')
# # Type custing
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0
# print(x);
# print(y);
# print(z);
# # Unpack a Collection
# print("--------- Unpacking a Collection -----------");
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x);
# print(y);
# print(z);

# print('----------- Many Values to Multiple Variables -----------');

# x,y,z = "AAA", 'BBB', 'CCC'
# print(x);
# print(y);
# print(z);

# print('------------- Input ----------------')

# name = input("Enter your name: ")
# print(f"Hello, {name}")

# print("------------ Good Morning Calculater -------------");

# inputHour = input("Enter hour: ")

# hour = time.localtime().tm_hour

# print(f"Current Hour: {hour}");

# if 5 <= hour <12:
#     print("Good Morning!")
# elif 12 <= hour < 17:
#     print("Good Afternoon!")
# elif 17 <= hour < 21:
#     print("Good Evening!")
# else:
#     print("Good Night!")

# print('------------ Math Function ------------')

# result = math.sqrt(16)
# print(result)
# print(dir(math))

# print('----------- Funciton -------------')

# print(welcome())
# print(name)

# print('-------- Welcome Function --------')

# print("------------ lambda function ------------")
# x = lambda a: a + 10
# print(x(5))

# x = lambda a , b : a * b
# print(x(5, 6))

print('------------- Map, Filter, Reduce -------------')
from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def myFunction(x):
    return x * x
def testFunction(x):
    return x > 5

# print(list(map(myFunction, l)))
# print(list(map(lambda x: x * x, l)))
# print(list(filter(testFunction, l)))
# print(list(filter(lambda x: x > 5, l)))
# print(list(map(lambda x: x * x, l)))

len = [1, 2, 3, 4]  

print(reduce(lambda x, y : x +y , len))



