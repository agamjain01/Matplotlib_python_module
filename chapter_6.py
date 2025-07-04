'''
In this chapter we are see how two chart compair same canvas .
that could we happen by subplot function 

supplot(nrow,ncolm,supplot)

'''
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("line Chart")


plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("bar Chart")

plt.tight_layout() # that is help in title name in center 
plt.show()


# subplot  chart with width and height

# fig , ax= plt.subplot(nrow,ncol,figsize=(width,height))
fig , ax= plt.subplots(1,2,figsize=(10,5))
x=[1,2,3,4]
y=[10,20,15,25]

ax[0].plot(x,y,color="red")
ax[0].set_title("Line chart")


ax[1].bar(x,y,color="red")
ax[1].set_title("Bar chart")

plt.tight_layout()
plt.show()