
import pandas as pd

data = {
    "Name": ["Rahul", "Aman", "Riya"],
    "Age": [20, 21, 19],
    "City": ["Delhi", "Noida", "Meerut"]
}

df = pd.DataFrame(data)

# print(df)

data  = pd.read_excel("C:/Users/gdivy/OneDrive/Desktop/Downloads/employee_data.xlsx")

# KOI DATA HAI USKE STARTING ROWS DEKHNI HAI TO USKE LIYE

print(data.head(10))

# KOI DATA HAI USKE LAST 10 ROWS DEKHNA HAI

print(data.tail(10))

# KOI DATA HAI USKE USKI SAARI ROWS AUR SAARI COLN DEKHNA HAI


pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)


# BASICS OPERATIONS

print(data.shape)# total rows and total coln
print(data.info())# total rows , coln names , non-null values,datatypes,memory usages
print(data.describe()) #numerical columns ka statistical summary
print(data.isnull().sum())# it tell us how many null values in in the coln