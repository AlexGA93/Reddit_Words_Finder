
# script that takes index.py data and operate with them to render a chart
from index import dataCharts
# importing matplotlib to render the charts components
import matplotlib.pyplot as plt
# importing NumPy to generate data later
import numpy as np


def main():
    # simple chart
    array = [1, 4, 6, 8, 3, 6, 8, 9, 4, 6]  # x coordenates
    array2 = [6, 5, 1, 9, 3, 2, 5, 6, 43, 2]  # y coordenates
    '''
    plt.plot(array)
    plt.ylabel('array data')
    plt.xlabel('num elem array')  # xlabel will be the number of items in array
    '''
    # plt.plot(array, array2, linewidth=2.0) #single line
    lines = plt.plot(array, array2)
    #plt.axis([0, 50, 0, 58])
    # axis dimensions --> x(start,final),y(start,final)

    # use keyword arguments
    plt.setp(lines, color='r', linewidth=2.0)

    #showing/ rendering
    plt.show()


if __name__ == "__main__":
    main()
