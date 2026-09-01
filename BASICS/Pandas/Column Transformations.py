import pandas as pd
import numpy as np
data = pd.read_excel("C:/Users/gdivy/OneDrive/Desktop/Downloads/employee_data.xlsx")
data.loc[(data["Age"]>=45),"GetBonus"] = "Yes Bonus"
data.loc[(data["Age"]<45),"GetBonus"] = "No Bonus"
pd.set_option("display.max_columns", None)
print(data.head(10))
print(data["GetBonus"].value_counts())