# chart render script
# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
d = {
    'group': ['A', 'B', 'C', 'D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
}
# organiza una tabla
'''
group  var1  var2  var3  var4  var5
0     A  38.0    29     8     7    28
1     B   1.5    10    39    31    15
2     C  30.0     9    23    33    32
3     D   4.0    34    24    14    14
'''
df = pd.DataFrame(data=d)

# number of variable
categories = list(df)[1:]  # ['var1', 'var2', 'var3', 'var4', 'var5']
N = len(categories)  # averigua  la longitud de columnas usables de la tabla


values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
plt.ylim(0, 40)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1)


'''
import matplotlib.pyplot as plt
#import numpy as np


def main(data):
    # data = array of arrays [subr[],words[],data[]]
    # data distribution(always 3 arrays)

    subr = data[0]
    words = data[1]
    info = data[2]

    print(subr)
    print(words)
    print(info)

    plt.plot(info)

    #showing/ rendering
    plt.show()
'''
