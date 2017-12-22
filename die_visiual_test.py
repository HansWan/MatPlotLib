import matplotlib.pyplot as plt
from die import Die

# Create a D6
die = Die(6)

# Do several die and put the results in a list
results = []
max_number = 1000
for roll_num in range(max_number):
    result = die.roll()
    results.append(result)

# Analyze results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, 7))
y_values = frequencies

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)

# Set pic title, and set tags for coordinate axes
plt.title("Die Frequencies", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Frequency", fontsize = 14)

# Set tick
plt.tick_params(axis = 'both', labelsize = 14)

# Set axes scope
plt.axis([0, 10, 0, int(max_number / 5)])

plt.show()
#plt.savefig('squares_plot.png', bbox_inches = 'tight')

