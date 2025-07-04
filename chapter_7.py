"""
that is last chapter in this chpater 
we are save the chart with help savefig("filename.ext",dip=value,bbox_inches="tight")
"""


import matplotlib.pyplot as plt

# we are create a 1 week sales of car  graph 

x=["Mo","Tu","We","Th","Fr","Sa"]
y=[4,6,2,5,3,1]

plt.plot(x,y)
plt.xlabel("Weeks days") 
plt.ylabel("sale of Car")
plt.title("Car showroom")

plt.savefig("CarSale.png",dpi=300,bbox_inches="tight")

plt.show()