import math
import numpy as np
import matplotlib.pyplot as plt

def parse_nmea(file):
    satellites = {}
    prns = []
    for line in file:
        if line[:4] != 'NMEA':
            continue
        segments = line.split(',')
        if segments[1] == "$GPGSV":
            for i in range(5, len(segments) - 4, 4):
                try:
                    prn = int(segments[i])
                    elevation = int(segments[i + 1])
                    azimuth = int(segments[i + 2])
                    if 0 < prn <= 32:
                        satellites[prn] = [elevation, azimuth]
                except:
                    continue
        elif segments[1] == "$GNGSA":
            prns += [-1 if segments[i] == "" else int(segments[i]) for i in range(4, len(segments) - 5)]
            t = int(segments[len(segments) - 1])


    sorted_satellites = dict(sorted(satellites.items()))
    # im just happy I get to use a lambda function
    used_satellites = list(filter(lambda x : x in prns, sorted_satellites.keys()))
    A = []
    for i, s in enumerate(used_satellites):
        if i >= 4: break;
        el, azi = sorted_satellites[s]
        A.append([-math.cos(el) * math.sin(azi), -math.cos(el) * math.cos(azi), -math.sin(el), 1])
    if not A: return -1, -1, -1, -1, -1
    A = np.array(A)
    cofactor = np.linalg.inv(A @ A.T)
    q_ee = cofactor[0][0]
    q_nn = cofactor[1][1]
    q_uu = cofactor[2][2]
    q_tt = cofactor[3][3]
    HDOP = np.sqrt(q_ee + q_nn)
    VDOP = np.sqrt(q_uu)
    PDOP = np.sqrt(q_ee + q_nn + q_uu)
    GDOP = np.trace(cofactor)
    return HDOP, VDOP, PDOP, GDOP, t

def get_dop_values(path):
    with open(path) as f:
        epochs = f.read().split("$GNGGA")
        res = []
        name = path.split('/')
        name = name[len(name) - 1]
        name = name[:len(name)-4]
        for j, epoch in enumerate(epochs):
            hdop, vdop, pdop, gdop, t = parse_nmea(epoch.splitlines())
            if t == -1: continue
            res.append([hdop, vdop, pdop, gdop, t])
        np.savetxt(f"../data/dop_values_{name}csv", res, delimiter=",", header="hdop, vdop, pdop, gdop, time")

# get_dop_values("../data/gnss_log_2026_11_13_12_25_01.nmea")

values = np.genfromtxt('../data/dop_values_gnss_log_2026_11_13_12_25_01.csv', delimiter=',')
values = np.transpose(values[1:])
hdops, vdops, pdops, gdops, t = values
plt.plot(np.arange(len(hdops)), hdops)
plt.plot(np.arange(len(vdops)), vdops)
plt.plot(np.arange(len(pdops)), pdops)
plt.plot(np.arange(len(gdops)), gdops)
plt.show()