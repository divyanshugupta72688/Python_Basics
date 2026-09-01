import pandas as pd
import numpy as np
data = pd.read_excel("C:/Users/gdivy/OneDrive/Desktop/Downloads/nan_text_data.xlsx")

#1. SIMPLE FUNCTION
print(data.isnull())


#2.sum nikalana hai ki kitni value null kis kis colun me
print(data.isnull().sum())


#3.agar hume vo row delete karni hai jo row null contain krti hai
print(data.dropna())

# agar data fill karna hai normally
print(data.replace(np.nan, '30000'))

# jo filling vala way hai upr its not correct way because
#ye har jagah vahi data fill kr dega chahe salary ho ya name ho
# aur is baat ka koi sense nahi banta hai

# so we use different way to fill the nan

data["Salary"] = data["Salary"].replace(np.nan,30000)
print(data)

# its also different way to fill the row in the specific coln
# without using numpy library
data["Salary"] = data["Salary"].fillna(30000)
print(data)

