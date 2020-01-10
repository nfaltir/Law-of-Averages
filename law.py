import random
import matplotlib.pyplot as plt

myList = ['heads', 'tails']


for newList in range(1, 10):

    newList = random.choice(myList)
    countTail = newList.count('tails')
    countHead = newList.count('heads')

    print(newList)


