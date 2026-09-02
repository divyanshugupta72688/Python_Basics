import matplotlib.pyplot as plt

x = ["Part1","Part2","Part3","Part4","Part5"]
y = [98,67,85,50,80]
colors = ["red","green","blue","yellow","orange"]
# We can also provide color to the graph
plt.bar(x,y,color=colors)
# we can provide title as well as fontisize for them
plt.xlabel("Parts of Harry Potter",fontsize = 17)
plt.ylabel("Popularity",fontsize = 17)
plt.title("Popularity of different parts of Harry Potter",fontsize = 20)
plt.show()