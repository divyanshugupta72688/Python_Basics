import pandas as pd

data1 = {
    "EmployeeID":["E01","E02","E03","E04","E05"],
    "Name":["Divyanshu","Sushant","Ayush","Chotu","Sneha"],
    "Age":[23,24,22,22,21]
}

data2 = {
    "EmployeeID": ["E01", "E02", "E03", "E04", "E05"],
    "Salary":[48500,47000,55000,52000,41000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print()
print(df2)


#merge
print(pd.merge(df1,df2,on="EmployeeID"))
print()



