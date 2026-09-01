import pandas as pd

data = pd.read_excel("C:/Users/gdivy/OneDrive/Documents/OneDrive/Documents/small_duplicate_data_1.xlsx")

# Ye har row ke liye True/False batayega:
# False → duplicate nahi hai
# True → duplicate row hai
print(data.duplicated())


#Total duplicate rows count karna ho:
print(data.duplicated().sum())

#Agar actual duplicate rows dekhni hain:
print(data[data.duplicated()])
print(data["ID"].duplicated().sum())


# hmehsa ID pe drop lgana chahiye
print(data.drop_duplicates("ID"))



