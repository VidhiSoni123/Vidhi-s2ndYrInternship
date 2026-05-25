#q1: creating pandas series from dictionary
import pandas as pd
data={
    "Subject":["python","java","cpp"],
    "Marks":[90,80,87],
    "Grade":["A","B","B"]
     }
df=pd.Series(data)
print(df)

#q1:pandas series from lists
data=[10,20,30,40]
ps=pd.Series(data)
print(ps)

#q1:Accesing elements of Series in Pandas
data=[10,20,30,40,50,60,70]
ps=pd.Series(data,index=["a","b","c","d","e","f","g"],dtype=float,name="integer series")
print(ps)
print(ps[1])
print(ps["a"])

#q2: pandas dataframe with 2-D python list
data=[['a','b'],['c','d'],['e','f'],['g','h']]
df=pd.DataFrame(data, columns=['a1','a2'])
print(df)

#q2:DataFrame fron python Dictionary
data={
    "Subject":["python","java","cpp"],
    "Marks":[90,80,87],
    "Grade":["A","B","B"]
     }
df=pd.DataFrame(data)
print(df)
print(type(df))

#q2:Pandas dataframe from python lists of lists
data=[['a','b'],['c','d'],['e','f'],['g','h']]
df=pd.DataFrame(data, columns=['a1','a2'])
print(df)

#q2:pandas dataframe from list of tuples
data=[('a','b'),('c','d'),('e','f'),('g','h')]
df=pd.DataFrame(data, columns=['a1','a2'])
print(df)

#*q2:pandas dataframe from lists of dictionaries
data=[{'a':'b'},{'c':'d'},{'e':'f'},{'g':'h'}]
df=pd.DataFrame(data, columns=['a1','a2'])
print(df)

#q3:Different ways to iterate over rows in pandas dataframe
 
data={
    "Name":["Aman","Riya","Karan","Neha"],
    "Marks":[85,90,75,60],
    "City":["Jaipur","Delhi","Mumbai","Pune"]
}
df=pd.DataFrame(data)
print(df)

#q3:selecting rows in pandas dataframe based on conditions
res=df[df["Marks"]>80]
print(res)

#q3:select any row from a dataframe using iloc[]
print(df.iloc[1])

#q3:limited rows selection with given column
print(df.loc[0:2,["Name","Marks"]])

#q3:drop rows from the dataframe based on certain condition applied on a column
print(df.loc[0:2,["Name","Marks"]])
#*q3:Insert row at given position in pandas dataframe
#q3:Create a list from rows in pandas dataframe
list=df.values.tolist()
print(list)
