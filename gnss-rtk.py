import csv
import json
import numpy as np
from typing import Any

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

def make_lines(csv_file):
    coords = []
    lines = []
    with open(csv_file, "r") as f:
        file = csv.reader(f, delimiter=";")
        index = 0
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
            coords.append([longitude, latitude])
            if index > 0:
                line = [coords[index-1], coords[index]]
                print(line)
                lines.append(line)
            index += 1
    lines.append([coords[-1], coords[0]])
    # coords = np.asarray(coords)
    # np.savetxt("buildingcoords.csv", coords, delimiter=",")
    return lines

lines = make_lines("totalstation_points.csv")
geojson = make_geojson(lines)
write_geojson("building_outline.geojson", geojson)