'''
In this chapter 4 we are see different type of  graph.

1. Bar chart --> bar can we are create vertical and horigental barh() 
2. Pie chart
3. Histograms

'''

# Bar chart --> plt.bar(x,hight=,color="color name ",width=value,label="label name ")

import matplotlib.pyplot as plt
marks=[25,46,52,41,84,55,45]
student=['A','B','C','D','E','F','G']
plt.bar(student,marks,width=0.5,color="purple",label="Student Marks ",)
plt.xlabel="student"
plt.ylabel="Marks"
plt.legend()
plt.show()


# pie chart --> plt.pie(values,labels=[label_list],colors=color_list,autopct='%1.1f%%')
label_name=["Agam","hardik","Harsh","kunal"]
Pre=[200,500,100,600]
plt.pie(Pre,labels=label_name,autopct='%1.1f%%')
plt.show()

# Histograms --> plt.hist(data,bins=number_of_number,color="Color name ,edgecolor="black")

marks=[55,74,55,45,26,1,4,65,44,11,55,41,55,77,9,2,44,55,11,22,33,66,55,44,46,45,56,41]
bins_size=5

plt.hist(marks,bins=bins_size,color="blue",edgecolor="black")
plt.show()

