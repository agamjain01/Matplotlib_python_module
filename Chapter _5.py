'''
In this chapter we are see compair the data set.
like a example we  compair data class like study hours 
learning rate .

So we are use the scatter chart --> scatter(x,y,color="color_name",marker ="+,*,^,S,D,O",label="label_name")
'''

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[45,63,52,41,54]
plt.scatter(x,y,color="red",marker="*",label="Student Data For Section A ")
plt.xlabel("hours")
plt.legend()
plt.grid(True)
plt.ylabel("student Perform")
plt.show()


# next compair two section class performance

plt.scatter([1,2,3,4,5],[45,62,52,64,45],color="red",marker="^",label="Class A")
plt.scatter([1,2,3,4,5],[45,63,42,54,32],color="blue",marker="o",label="Class B")
plt.xlabel("hours")
plt.legend()
plt.grid(True)
plt.ylabel("student Perform")
plt.show()
