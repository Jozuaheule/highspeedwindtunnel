# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
import Data_getter
import flowtools

# return graphs
def return_graph(xlist, ylist, labelx, labely, legend_measurement, legend_theoretical, position, xfit, yfit):

    plt.xlabel(str(labelx), fontsize = 16)
    plt.ylabel(str(labely), fontsize = 16)
    #plotting graphs including markers
    plt.plot(xlist, ylist, markersize=10, linewidth=1, label = str(legend_measurement), marker="o", color="black")
    plt.plot(xfit, yfit, markersize=10, linewidth=1, label = str(legend_theoretical), marker="x", color="red")
    plt.legend(loc= position)
    plt.grid(True)
    plt.show()

    return

xThroat = 65.0 #mm
gamma = 1.4
xvals, heights, areas = Data_getter.get_data_area()
pressureRatios = np.array([])
MachNums = np.array([])
for i in range(len(xvals)):
    A = areas[i]
    if xvals[i] < xThroat:
        mode = 'sub'
    else:
        mode = 'sup'

    results = flowtools.flowisentropic2(gamma, A, mode)
    MachNums = np.append(MachNums, float(results[0]))
    pressureRatios = np.append(pressureRatios, float(results[2]))

return_graph(xvals, pressureRatios, "x [mm]", "$p/p_t$ [-]", "quasi 1 D theory", "measured pressure ratio", "upper right", xvals, pressureRatios)

return_graph(xvals, MachNums, "x [mm]", "M [-]", "quasi 1 D theory", "computed from measured pressure ratio", "lower right", xvals, MachNums)