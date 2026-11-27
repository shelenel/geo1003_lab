

import numpy as np
import pyproj
import matplotlib.pyplot as plt


input_file = "data/gnss_log_2026_11_13_12_09_42 (1).txt"

records = []
with open(input_file) as file:
    for row in file:
        row = row.split(',')
        if row[:2] == ["Fix", "GPS"]:
            records.append([
                float(row[3]),
                float(row[2]),
                float(row[4])
            ])

coordinates = np.array(records)

t = pyproj.Transformer.from_crs(
    "EPSG:4326",
    "EPSG:28992",
    always_xy=True
)

RD_coordinates = []

for long, lat, h in coordinates:
    x, y = t.transform(long, lat)
    RD_coordinates.append([x, y, h])

RD_coordinates = np.array(RD_coordinates)

print(RD_coordinates)

x = RD_coordinates[:, 0]
y = RD_coordinates[:, 1]
z = RD_coordinates[:, 2]

mean_x = np.mean(x)
mean_y = np.mean(y)
mean_z = np.mean(z)

std_x = np.std(x, ddof=1)
std_y = np.std(y, ddof=1)
std_z = np.std(z, ddof=1)

print(mean_x, mean_y, mean_z, std_x, std_y, std_z)

plt.figure()
plt.scatter(x, y, s=5, color='blue')

plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.title("Blocked southern direction")
plt.axis("equal")
plt.grid()
plt.ticklabel_format(useOffset=False)
plt.tight_layout()
#plt.show()

plt.savefig("report/images/scatter_2.png", dpi=300)

from part_2 import RD_coordinates as RD_part_2
from part_2 import mean_x as mean_x_2
from part_2 import mean_y as mean_y_2

#RD_combined = np.vstack((RD_coordinates, RD_part_2))

x_norm = RD_coordinates[:,0]-mean_x
y_norm = RD_coordinates[:,1]-mean_y


x_1 = RD_part_2[:, 0] - mean_x_2
y_1 = RD_part_2[:, 1] - mean_y_2
z_1 = RD_part_2[:, 2]

plt.figure()

plt.scatter(x_norm, y_norm, s=5, color='blue')
plt.scatter(x_1, y_1, s=5, color='orange')

plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.title("Both observations")
plt.axis("equal")
plt.grid()
plt.ticklabel_format(useOffset=False)
plt.tight_layout()
plt.legend(['Blocked south', 'Open sky'])

plt.savefig("report/images/scatter_together.png", dpi=300)


