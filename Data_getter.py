import numpy as np

with open("Supersonic Mach-Area.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))

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

print(h)