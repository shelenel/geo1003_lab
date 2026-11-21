from pyproj import Transformer
import numpy as np

def extract_latlon(file):
    file = open(file, "r")
    lines = file.readlines()
    latlon = []
    for line in lines:
        if line.startswith("Fix"):
            line = line.split(",")
            lat, lon = line[2], line[3]
            latlon.append((lat,lon))
    return latlon

latlon = extract_latlon("/Users/Shelene/Desktop/Geomatics/Q2/GEO1003_Positioning/Lab/data/gnss_log_bk_walk.txt")

def transform_coord(latlon):
    xy = []
    t = Transformer.from_crs("EPSG:4258", "EPSG:28992", always_xy=True)
    for lat, lon in latlon:
        x, y = t.transform(lon, lat)
        xy.append((float(x),float(y)))
    return xy

xy = transform_coord(latlon)

unique_points = np.unique(xy, axis=0)

np.savetxt(
    "bk_walk_points.csv",
    unique_points,
    delimiter=",",
    header="x,y",
    comments=""
)
