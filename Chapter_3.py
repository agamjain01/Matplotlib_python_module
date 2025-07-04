'''
In chapter 3 we are matplotlib plot function .
1. plot -->  In this funnction we are design the graph .
             plt.plot(x,y,color="coloer_name",inestyle="--,..,*,:.",linewidth=intregerNumber,label="lable of line",
             maker="o,*,+,")
             
2. xlabel and ylebel = that is lable the x and y line meaning 

3. legend --> that show the line meaning  top and down of the chart 
             plt.legend(loc="upper left",linewidth=2)

4. tutle = that is  givne the title of the chart

5. grid = that create a graph line 
          plt.grid(linestyle="",linewidth=1 ,color"blue")

6. xlim and  ylim = that is contorl the limit  a range of y axis and xaxis 

7. plt.xticks and yticks = that is change the name of x and y axis 

8. plt.show  --> that is simple work that is show the graph 
'''

import matplotlib.pyplot as plt

# car sale data 


months =[1,2,3,4,5]
sale=[1200,400,800,1400,1350]
plt.plot(months,sale,color="blue",linestyle="--",linewidth=2,marker="o",label="Sale data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(loc="upper left",fontsize=10)
plt.grid(color="green",linestyle="--",linewidth=1)
plt.title("Car sale data")
plt.ylim(100,1500)
plt.xticks(months,["M1","M2","M3","M4","M5"])
plt.show()