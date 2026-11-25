
import pandas as pd
import numpy as np
import pyproj

from pathlib import Path
from pyproj.transformer import TransformerGroup

input_file = "data/gnss_log_bk_walk.txt"

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
print(coordinates)
print(coordinates.shape)

epoch = 2026 + 316/365
print (epoch)

t1 = pyproj.Transformer.from_crs(
    "EPSG:9989",
    "EPSG:7931",
    always_xy=True
)

ETRF_coordinates = []

for long, lat, h in coordinates:
    long_n, lat_n, h_n, time = t1.transform(
        long, lat, h, epoch, errcheck=True
    )

    ETRF_coordinates.append([long_n, lat_n, h_n])

ETRF_coordinates = np.array(ETRF_coordinates)

print(ETRF_coordinates)

group = TransformerGroup(
    "EPSG:7931",
    "EPSG:28992",
    always_xy=True
)

for t in group.transformers:
    print(t.description)
    print(t.definition)


t2 = pyproj.Transformer.from_crs(
    "EPSG:7931",
    "EPSG:28992",
    always_xy=True,
    allow_ballpark=False,
    only_best=True
)

RD_coordinates = []
for long, lat, h in ETRF_coordinates:
    x, y = t2.transform(long, lat, errcheck=True)
    RD_coordinates.append([x, y])

RD_coordinates = np.array(RD_coordinates)

print(RD_coordinates)
print(RD_coordinates.shape)

print(t2.get_last_used_operation().definition)