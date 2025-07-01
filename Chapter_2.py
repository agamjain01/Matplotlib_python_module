"""
In this chapter we understand some keys point about the matplotlib
1. datapoint --> that is show what x and y axis point the data in a graph (1  that x, 5 that y)
2. x and y axis --> that simple x denotes horizantal line and y denotes vertical line
3. Figure--> figuer is similar to Canvas & full screen display that show the graph
4. Axes --> that is one graph because figure canten multiple graph
5. plot --> that is graph line point 
6. marker --> that show point design (o s d * +)
7. line --> that show line in graph
8. line Style --> that show line design (- -- : -. )
9. color--> line color
10. legend--> that graph name
11. lable  --> with the help of lable we give to name x and y axis 
12. title --> with the help of title we give title of the graph
13. grid--> graph shape design
14. function --> single function to the particular graph
15. method --> 
16. parameters --> 
17. keyword argument--> method(keyword argument)
18. object - oriented api --> that is use in lager data set and also use in multiple graph
19. Dpi--> clarity of graph 
20. backend --> backend works
"""


import matplotlib.pyplot as plt

# we are create a 1 week sales of car  graph 

x=["mon","tue","wed","thu","fir","sat"]
y=[4,6,2,5,3,1]

plt.plot(x,y)
plt.xlabel("Weeks days") 
plt.ylabel("sale of Car")
plt.title("Car showroom")

plt.show()

