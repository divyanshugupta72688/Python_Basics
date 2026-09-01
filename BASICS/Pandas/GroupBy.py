import pandas as pd
data = pd.read_excel("C:/Users/gdivy/OneDrive/Desktop/Downloads/employee_data.xlsx")
pd.set_option("display.max_columns", None)
print(data)


gp = data.groupby("Department").agg({"Gender":"count"})
print(gp)
gp = data.groupby(["Department","Gender"]).agg({"EmployeeID":"count"})
print(gp)