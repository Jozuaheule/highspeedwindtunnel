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

# Het volgende stuk geeft de hoogte van een punt in de tweede throat met de gegeven diffuser setting

def get_h(X, METER4, METER5):
    difData = Data_getter.get_data_diffuser(500)

    for i in range(len(difData[0])):
        if difData[0][i] == METER4 and difData[1][i] == METER5:
            slope = difData[3][i]
            b = difData[4][i]
            h = slope * X + b
            return h

def get_hk2(METER4, METER5):
    difData = Data_getter.get_data_diffuser(500)

    for i in range(len(difData[0])):
        if difData[0][i] == METER4 and difData[1][i] == METER5:
            hk2 = difData[2][i]
            return hk2


# Berekenen van pe/pt (3, 5, 6)
def getpept(X, METER4, METER5):
    h = get_h(float(X), float(METER4), float(METER5))
    hk2 = get_hk2(float(METER4), float(METER5))
    A = h/hk2
    pept3 = flowtools.flowisentropic2(1.40, A, 'sub')[2]
    pept6 = flowtools.flowisentropic2(1.40, A, 'sup')[2]
    M1 = flowtools.flowisentropic2(1.40, A, 'sup')[0]
    pept5 = flowtools.flownormalshock2(1.40, M1, 'mach')[2]*pept6

    return pept3, pept5, pept6

xpoints = Data_getter.get_data_pressure()[0]
ppoints = Data_getter.get_data_pressure()[1]
plt.plot(xpoints, ppoints)
plt.show()
