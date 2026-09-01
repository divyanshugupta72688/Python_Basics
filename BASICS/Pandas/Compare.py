import pandas as pd
dict = {
    "Fruits":["Apples","Oranges","Bananas","Manogo"],
    "Price":[150,100,50,100],
    "Quantity":[10,7,5,15]
}
df1 = pd.DataFrame(dict)
print(df1)

print()
print()

# if u have small data then this process will work

df2=df1.copy()
df2.loc[0,"Price"]=170
df2.loc[1,"Price"]=80
df2.loc[3,"Price"]=120

df2.loc[0,"Quantity"]=9
df2.loc[1,"Quantity"]=14
df2.loc[2,"Quantity"]=12
df2.loc[3,"Quantity"]=11

print(df2)
print()
print()

# if u have large dataset then u have to apply compare

print(df1.compare(df2))
print()