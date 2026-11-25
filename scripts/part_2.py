


import pandas as pd
import numpy as np
import pyproj
import matplotlib.pyplot as plt

from pathlib import Path
from pyproj.transformer import TransformerGroup

input_file = "data/gnss_log_2026_11_13_12_25_01.txt"

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

plt.scatter(x, y, s=5)

plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.title("Open sky conditions")
plt.axis("equal")
plt.grid()
plt.show()

mean_x = np.mean(x)
mean_y = np.mean(y)
mean_z = np.mean(z)

std_x = np.std(x, ddof=1)
std_y = np.std(y, ddof=1)
std_z = np.std(z, ddof=1)

