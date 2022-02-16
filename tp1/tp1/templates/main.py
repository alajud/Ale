import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)
plt.axis([0, 1100, 0, 1100000])

for i in range (1000):
    print ("x: " + str(x_values[i]) + " y: " + str(y_values[i]))

print(a)
# Set chart title and label axes.

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=10)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()




