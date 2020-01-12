import random
import matplotlib.pyplot as plt

print("\n====================Law of Averages====================\n")
myList = ['heads', 'tails']
count = 0

# user input to determine range
rangeLength = int(input("Please enter the number of coin toss:"))
for newList in range(1, rangeLength):

    newList = random.choice(myList)
    print(newList)
    # count tails in random list
    if(newList == 'tails'):

        count = count + 1
# count heads
heads = rangeLength - count
tailPercent = count/rangeLength*100
headPercent = heads/rangeLength*100
print("Number of coin toss: ", rangeLength)
print("total tails: ", count)
print("total heads: ", heads)
print('')

# use round function to eleminate messy percentage
print("Percent of tails:", round(tailPercent, 2), "%")
print("Percent of heads:", round(headPercent, 2), "%")


# visualize the data

# pie layout
labels = ['heads', 'tails']
sizes = [heads, count]
explode = (0, 0.1)

# pie colors
colors = ['#67eaca', '#52de97']

Results, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Coin toss results")
plt.show()
