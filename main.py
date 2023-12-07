import time

y = 2.5
x = "2"
print(int(y))
print(int(x))
# [start:stop:step]
name = "parsa pakdaman"
print(name[::3])
name2 = "alibabaparsa.comcom"

name2_2 = name2.split(".")
x = 7
print(name2_2[0][x:])
for i in range(10, 101, 5):
    print(i)
for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)
print("time for jerk off")
for i in range(10):
    for j in range(10):
        print("X", end="")
    print()

phone = "0902-206-6728"

for i in phone:
    if i == "-":
        pass
    else:
        print(i, end="")


# keyword argument
def hello(first_name, last_name):
    print("\n" + first_name + " " + last_name)


hello(last_name="pakdaman", first_name="parsa")


def show(*args):  # tuple
    x = 0
    for i in args:
        x += i
    return x


print(show(333, 32131, 312313, 3213123))


def show2(**kwargs):  # dictionary
    print("hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


show2(first_name="pakdaman", last_name="ali", middle_name="parsa")

# str.format()
number = 1000
print("number : {:,}".format(number))
print("number : {:b}".format(number))
print("number : {:x}".format(number))
print("number : {:o}".format(number))

# random methods 1-choice 2-random 3-randint 4-shuffle

# try except else finally

# os , os.path, open and read file, write, with open("text.txt,"append,write,read")as file , os.replace , os.remove
# shutil for copying file
# method chaining with using return self
# super function used to access to method of the parents class
# from abc import ABC, abstractmethod
# example : class X(ABC)
#                @abstractmethod
#                def z(self):
# we should overwrite the method of abstractmethod
foods = list()
while food := input("type food:") != "quit":  # :=
    foods.append(food)


# higher level functions
def mult(a):
    def mult2(b):
        return a * b

    return mult2


a = lambda b: b*2
print(a(2))

# map(func, iterable)  apply function to each item of iterable
# filter(func, iterable) create collection of element
# reduce(func, iterable) apply function to iterable and reduce it to single value
