#Working with Pandas Data Frames

import pandas as pd

print("Example 1:-")
print("")

mydataset = {
'cars': ["BMW", "Volvo", "Ford"], 
'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset) 
print(myvar)

# Create Labels 
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"]) 
print(myvar)

# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

data = {
"calories": [420, 380, 390],
"duration": [50, 40, 45]
}
    
#load data into a DataFrame object:
df = pd.DataFrame(data) 
print(df)