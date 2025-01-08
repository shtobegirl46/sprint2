import pandas as pd

# Read the CSV file
df = pd.read_csv('your_file.csv', header=None)
# Convert each row to a list
lines_as_lists = df.values.tolist()
"""
1,2,3                   [[1, 2, 3]
4,5,6   ======>>>>>      [4, 5, 6]"""
