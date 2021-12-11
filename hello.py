import math, random
from data import ANIMALS




print('Welcome to the jungle')

multiples_of_5 = [i for i in range(50) if i%5 == 0 and i>0]

num = random.choice(multiples_of_5)

print(f'random integer = {num}')

odd = [i for i in range(num) if i%2 != 0]
even = [i for i in range(num) if i%2 ==0]

print(ANIMALS)
print(odd)
print(even)



#if __name__ == "__main__":

