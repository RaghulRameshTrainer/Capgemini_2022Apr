import matplotlib.pyplot as plt

plt.subplot(211)
plt.plot([5,8,10],[11,16,6],'g',label="Line1",linewidth=3)

plt.subplot(212)
plt.plot([6,9,11],[6,15,7],'c',label="Line2",linewidth=3)

plt.show()