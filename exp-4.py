#Reading data from text files , Excel and the web and exploring various commands for doing descriptive analysis on the Iris data set.

import pandas as pd

# Reading the CSV file
df = pd.read_csv("./irisdataset.csv")

# Printing top 5 rows
print(df.head())
print("")

print("Shape: the shape parameter to get the shape of the dataset")
print(df.shape)
print("")

print("Info(): the columns and their data types")
print("")
print(df.info())
print("")

print("Describe():- function gives a good picture of the distribution of data")
print("")
print(df.describe())
print("")

print("Isnull():We will check if our data contains any missing values or not. M")
print("")
print(df.isnull().sum())

print("Checking Duplicates: Pandas drop_duplicates() method helps in removing duplicates.")
print("")
data = df.drop_duplicates()
print(data)
print()

print("value_counts() function. This function returns a Series containing counts of unique values.")
print(df.value_counts(  ))
print("")

import seaborn as sns
import matplotlib.pyplot as plt


#Example 1 Comparing Sepal Length and Sepal Width
sns.countplot(x="Species", data=df)
plt.show()

sns.scatterplot(x="SepalLengthCm", y="SepalWidthCm", data=df)
# plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

#Example 2: Comparing Petal Length and Petal Width
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm',  data=df   )
# plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()

#Histograms allow seeing the distribution of data for various columns. It can be used for uni as well as bi-variate analysis.

fig, axes = plt.subplots(2,2, figsize=(10, 10))

axes[0,0].set_title("Sepal Length")
axes[0,0].hist(df["SepalLengthCm"], bins=7)