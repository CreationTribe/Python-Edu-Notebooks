# from matplotlib import pyplot
#
# pyplot.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25])
# pyplot.axis([0, 5, 0, 25])
#
# pyplot.show()


from matplotlib.pyplot import plot, axis, show, legend

xlist = range(0, 6)
ylist = []

for i in xlist:
    ylist.append(i*i)
plot(xlist, ylist, label='squares', marker='+', color='red', markeredgecolor='blue')

axis([0, 5, 0, 25])
legend()
show()


# pyplot.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25])
# pyplot.axis([0, 5, 0, 25])

# pyplot.axes([0, 5], [0, 25])

# pyplot.show()
#
# pyplot.show()


