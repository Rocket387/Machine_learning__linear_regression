import numpy
import matplotlib.pyplot as plt
from scipy import stats

#x = numpy.random.normal(5.0, 1.0, 13) generates 13 random numbers on x axis with mean value 5, standard deviation 1
#y= numpy.random.normal(10.0, 2.0, 13) generates 13 random numbers on y axis with mean value 10, standard deviation 2

#these arrays represent values of x and y axis
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#this method returns important key values of linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)
# r = relationship between values of x axis and y axis. values range from -1 to 1 (100% related), 0 = no relationship

def myfunc(x):
    return slope * x + intercept
#function uses slope and intercept values ot return new value
#new value = position on y axis the corresponding x value will be placed

speed = myfunc(7)
print(speed) # prints speed of a 7 year old car

mymodel = list(map(myfunc, x))

plt.scatter(x, y) # draws scatterplot
plt.plot(x, mymodel) #draws line of linear regression
plt.show() #display diagram