import re

print("REGEX EXAMPLES")

email = "abc@gmail.com"

if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
    print("Valid Email")
else:
    print("Invalid Email")

mobile = "9876543210"

if re.match(r'^[6-9]\d{9}$', mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

name = "Python"

if re.match(r'^[A-Za-z]+$', name):
    print("Only alphabets present")
else:
    print("Other characters also present")

text = "Python123DSA456"

print("Numbers in string:")
print(re.findall(r'\d+', text))


# -----------------------------
# Datetime functions in pandas
# -----------------------------

import pandas as pd

print("\nDatetime Examples")

date = pd.to_datetime("2026-06-09")

print("Date =", date)
print("Year =", date.year)
print("Month =", date.month)
print("Day =", date.day)

d1 = pd.to_datetime("2026-06-01")
d2 = pd.to_datetime("2026-06-09")

print("Difference =", d2 - d1)

print("\nDate Range")
print(pd.date_range(start="2026-06-01", periods=5))


# -----------------------------
# CSV file analysis
# -----------------------------

data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Riya"],
    "Marks": [85, 90, None, 78, 95],
    "City": ["Delhi", "Mumbai", "Jaipur", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")

print("\nOriginal Data")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

avg = df["Marks"].mean()

df["Marks"] = df["Marks"].fillna(avg)

print("\nAfter Cleaning")
print(df)

print("\nAverage Marks")
print(df["Marks"].mean())

print("\nHighest Marks")
print(df["Marks"].max())

print("\nStudents from Delhi")
print(df[df["City"] == "Delhi"])

print("\nAverage Marks City Wise")
print(df.groupby("City")["Marks"].mean())