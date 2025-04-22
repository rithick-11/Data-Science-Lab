import numpy as np
import matplotlib.pyplot as plt

# Creating a series of data in range of 1-50
x = np.linspace(1, 50, 200)

# Creating a Function for normal distribution
def normal_dist(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

# Calculate mean and Standard deviation
mean = np.mean(x)
sd = np.std(x)

# Apply function to the data
pdf = normal_dist(x, mean, sd)

# Plotting the Results
plt.figure()
plt.plot(x, pdf, color='red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')
plt.show()

feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
fig, ax = plt.subplots(1, 1)

Z = np.cos(X / 2) + np.sin(Y / 4)
# plots contour lines
ax.contour(X, Y, Z)
ax.set_title('Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')
plt.show()

from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Simple scatter plot
sns.scatterplot(x=df.columns[0], y=df.columns[1], data=df)
plt.title("Scatter Plot")
plt.show()

# Scatter plot with regression line
sns.lmplot(x=df.columns[0], y=df.columns[1], data=df)
plt.title("Scatter Plot with Regression Line")
plt.show()

# Simple histogram
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
plt.figure(figsize=(10, 7))
plt.hist(a, bins=[0, 25, 50, 75, 100])
plt.title("Simple Histogram")
plt.show()

# Distribution histogram
np.random.seed(23685752)
N_points = 10000
n_bins = 20
x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(10000) + 25

plt.figure(figsize=(10, 7))
plt.hist(x, bins=n_bins)
plt.title("Normal Distribution Histogram")
plt.show()