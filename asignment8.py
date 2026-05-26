# 1) Convert a series of date-strings to a timeseries

import pandas as pd

dates = ["2026-01-01", "2026-02-15", "2026-03-20"]

timeseries = pd.to_datetime(dates)

print(timeseries)

# 2) Create two DataFrames and perform joins

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Karan", "Neha"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4, 5],
    "Marks": [85, 90, 78, 88]
})

# Inner Merge
inner_merge = pd.merge(df1, df2, on="ID", how="inner")

print("Inner Merge")
print(inner_merge)

# Left Join

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Karan", "Neha"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4, 5],
    "Marks": [85, 90, 78, 88]
})

left_join = pd.merge(df1, df2, on="ID", how="left")

print(left_join)

# Missing values are shown as NaN
# because some IDs are not present in df2

# Right Join

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Karan", "Neha"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4, 5],
    "Marks": [85, 90, 78, 88]
})

right_join = pd.merge(df1, df2, on="ID", how="right")

print(right_join)

# Index-Based Join using join()

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Karan", "Neha"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [80, 90, 85, 88]
})

df1 = df1.set_index("ID")
df2 = df2.set_index("ID")

result = df1.join(df2)

print(result)

# Multiple Keys Merge

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 1],
    "Subject": ["Math", "Science", "English"],
    "Marks": [80, 90, 75]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 1],
    "Subject": ["Math", "Science", "English"],
    "Grade": ["A", "A+", "B"]
})

result = pd.merge(df1, df2, on=["ID", "Subject"])

print(result)

# 3) Concatenate and Merge DataFrames

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Aman", "Riya"]
})

df2 = pd.DataFrame({
    "ID": [3, 4],
    "Name": ["Karan", "Neha"]
})

df3 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [80, 90, 85, 88]
})

# Vertical Concatenation
concat_df = pd.concat([df1, df2])

print("Concatenated DataFrame")
print(concat_df)

# Merge with third DataFrame
final_df = pd.merge(concat_df, df3, on="ID")

print("Merged DataFrame")
print(final_df)

# Difference between join() and merge()

# join()
# 1. Works mainly on index
# 2. Simpler syntax
# 3. Uses .join()

# merge()
# 1. Works mainly on columns
# 2. More flexible
# 3. Uses pd.merge()