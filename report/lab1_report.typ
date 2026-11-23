#align(center)[= Lab 1 Report]
#align(center)[== GEO1003 - Positioning and Location Awareness]
\
#align(center)[Simon Kasdorp, Alicja Urbańczyk, Ewa Kużelewska
 Shelene Low]

#align(center)[Last updated: 21 November 2026]

= Lab 1a
== Smartphone GNSS - Perimeter and Area

#align(center)[
  #figure(image("images/bk_walk_allpoints.jpg", width: 70%), caption: [All recorded points from smartphone GNSS, extracted from GNSS text file log]) <bk_phone_walk_allpts>
]

@bk_phone_walk_allpts shows all the recorded points from an android smartphone GNSS, during our walk around the Architecture faculty. This also includes unwanted inaccurate points that do not necessarily correspond correctly to the perimeter of the faculty. As such, pre-processing of the points was done in QGIS by removing manually these unwanted points before the calculation of the area and perimeter. Such points include those that lie within the interior of the building.

After removing the unwanted points, a concave hull was made with the resulting points using the `Concave Hull (by layer)` function in QGIS. The perimeter and area were calculated based on the resulting concave hull, using `area($geometry)` and `perimeter($geometry)` in the `Field Calculator` of QGIS. A concave hull was chosen instead of a convex hull because of the shape of the building, since the building is not a a perfect rectangle (but with 'indents') and an attempt was made to preserve the integrity of the shape of the building. 

*An area of approximately $23,789m^2$ was obtained, with an approximate perimeter of $666m$.*