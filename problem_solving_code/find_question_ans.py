def f(x):
    return x+1
def g(x):
    return x*2
def h(x):
    return f(g(x))

# print(h(2))

# 2. code of array

def func(arr: list):
    gen = (each for each in arr  if len(arr)>=3)
    arr = ['Joe', 'Mary']
    return list(gen)

arr = ['Joe', ' Peter', 'Paul']
# print(func(arr))
# Output is []

# 3. code compiling

# c = d// uncomment this
d = 'Python'
# print(c)

# Output is NmaeError

# 4. type conversion

a = '1_111'
# print(float(a))

# output is 1111.0

# 5. What is the output and why?

class Myclass:
    def __init__(self, my_var) -> None:
        self.my_var = my_var

    def instance_method(self):
        self.my_var = 30
        return f'{self.my_var}'

obj = Myclass(10)

obj.instance_method()

# print(obj.my_var)
# Output is 30

# 6. list remove item when have duplicate value
g = [1,2,3,2,5]
g.remove(2)
# print(g)
# output [1,3,2,5]

# 6. What will be the output

for num in range(10):
    if num<5:
        continue
    elif num>8:
        break
    # print(num, end=' ')
# Output is 5,6,7,8

x = 'abcdef'
i = 'i'
while i in x:
    print(i, end=' ')

# No output