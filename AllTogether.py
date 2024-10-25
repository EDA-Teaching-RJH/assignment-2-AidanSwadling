### Part Four -- your code goes here. 
import random

list = []
numbers = 10
for x in range(numbers):
    list.append(random.randint(1,100))
print(list)

for y in list:
    print(y)

n = [i for i in list if i % 2 != 0]
print(n)
