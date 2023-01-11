import numpy as np

def get_data_area():

    with open("Supersonic Mach-Area.txt", "r") as f:
        lines = f.readlines()
        print(len(lines))

        # structure of data is the following
        # first number is the height windtunnel area
        # second number is the location
        # Third number is the area ratio

        h = []
        x = []
        area_relation = []

        for elem in lines:
            data = elem.split(" ")
            h.append(float(data[0]))
            x.append(float(data[1]))
            area_relation.append((float(data[2])))

        h = np.array(h)
        x = np.array(x)
        area_relation = np.array(area_relation)

    return h, x, area_relation


def get_data_diffuser(x):

    with open("Diffuser_data", "r") as f:
        lines = f.readlines()
        print(len(lines))

        # structure of data is the following
        # first number is Meter 4
        # second number is Meter 5
        # Third number is the height of second throat
        # Forth number is derivative dh/dx
        # Fifth number is zero_height

        m4 = []
        m5 = []
        hk2 = []
        dhdx = []
        h0 = []
        h = []

        for elem in lines:
            data = elem.split(" ")
            m4.append(float(data[0]))
            m5.append(float(data[1]))
            hk2.append(float(data[2]))

            a = dhdx.append(float(data[2]))
            b = h0.append(float(data[2]))

            # Find height of current x coordinate
            h = a*x + b
            h.append(h)

        m4 = np.array(m4)
        m5 = np.array(m5)
        hk2 = np.array(hk2)
        h = h.array(h)

    return m4, m5, hk2, h