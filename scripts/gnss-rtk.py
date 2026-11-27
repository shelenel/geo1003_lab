import csv
import json
import numpy as np
from typing import Any
from pyproj import Transformer

def write_geojson(path, mygeojson):
    with open(path, "w") as f:
        f.write(json.dumps(mygeojson, indent=2))

def make_geojson(lines):
    mygeojson: dict[str, Any] = {}
    mygeojson["type"] = "FeatureCollection"
    mygeojson["features"] = []
    for l in lines:
        f: dict[str, Any] = {}
        f["type"] = "Feature"
        f["geometry"] = {"type": "LineString", "coordinates": l}
        # f["properties"] = {"height": 100, "azimuth": 45, "lightness": 0.75}
        mygeojson["features"].append(f)
    return mygeojson

def make_lines(coords):
    lines = []
    s = 0
    for i in range(0, len(coords)):
        line = [coords[i - 1], coords[i]]
        lines.append(line)
        s += np.linalg.norm(np.array(list(line[1])) - np.array(list(line[0])))
    print("Perimeter:", s)
    return lines

def make_coords(csv_file):
    coords = []
    with open(csv_file, "r") as f:
        file = csv.reader(f, delimiter=";")
        for row in file:
            lat = row[1]
            lat_deg = float(lat[:2])
            lat_arcmin = float(lat[3:5])
            lat_arcsec = float(lat[6:len(lat)-1])
            latitude = lat_deg + lat_arcmin/60 + lat_arcsec/3600
            lon = row[2]
            lon_deg = float(lon[:1])
            lon_arcmin = float(lon[2:4])
            lon_arcsec = float(lon[5:len(lon)-1])
            longitude = lon_deg + lon_arcmin/60 + lon_arcsec/3600
            coords.append((latitude, longitude))
    coords = np.asarray(coords)
    return coords

def transform(latlon):
    xy = []
    t = Transformer.from_crs("EPSG:4258", "EPSG:28992", always_xy=True)
    for lat, lon in latlon:
        x, y = t.transform(lon, lat)
        xy.append((float(x),float(y)))
    return xy

coords = make_coords("../data/totalstation_points.csv")
np.savetxt("../data/qgis/building_coords_part_1b.csv", coords, delimiter=",", header="y, x")
points = transform(coords)
np.savetxt("../data/qgis/building_points_part_4.csv", points, delimiter=",", header="x, y")
lines = make_lines(points)
geojson = make_geojson(lines)
# write_geojson("../data/qgis/building_outline_part_1b.geojson", geojson)