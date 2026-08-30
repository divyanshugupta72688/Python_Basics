print("Break and Continue")
# Kisi particular condition ko skip karne ke liye
# hum continue statement use karte hain.

for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# kisi particular condition pe loop ko break ke liye
# break statment use krte hai


for i in range(1, 11):
    if i == 3:
        break
    print(i)