# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
import Data_getter
import flowtools

xThroat = 65.0 #mm
gamma = 1.4
data = Data_getter.get_data_area()
xvals = data[0]
heights = data[1]
areas = data[2]
print(data)
pressureRatios = np.array([])
MachNums = np.array([])
for i in range(len(xvals)):
    A = areas[i]
    if xvals[i] < xThroat:
        mode = 'sub'
    else:
        mode = 'sup'

    results = flowtools.flowisentropic2(gamma, A, mode)
    MachNums = np.append(MachNums, results[0])
    pressureRatios = np.append(pressureRatios, results[2])

print(pressureRatios)
print(MachNums)
plt.plot(xvals, MachNums)
plt.plot(xvals, pressureRatios)
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
