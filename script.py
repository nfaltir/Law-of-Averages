import random
import pandas as pd
import matplotlib.pyplot as plt


print("\n====================Law of Averages====================\n")
myList = ['head', 'tail']
tail = 0
head = 0

# user input to determine range
rangeLength = int(input("Please enter the number of coin toss: "))
for newList in range(1, rangeLength):

    newList = random.choice(myList)
    #print(newList)
    # count tails in random list
    if(newList == 'tail'):
        tail = tail + 1
    if(newList == 'head'):
            head = head + 1
# count heads
heads = rangeLength - tail
tails = rangeLength - head
tailPercent = round(tails/rangeLength*100,3)
headPercent = round(heads/rangeLength*100,3)
print("Number of coin toss: ", rangeLength)
print("total tails: ", tails)
print("total heads: ", heads)
print('')

# use round function to eleminate messy percentage
print("Percent of tails:", round(tailPercent, 3), "%")
print("Percent of heads:", round(headPercent, 3), "%")




# visualize the data

# pie layout
labels = ['heads', 'tails']

sizes = [heads, tails]
explode = (0, 0.07)

# pie colors
colors = ['#8FC1D4', '#52de97']


Results, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, autopct='%1.2f%%',  colors=colors, labels=labels,
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax1.legend(loc="best", title="Results")



plt.title(f"Number of Coin Tosses: {rangeLength}")
plt.show()



