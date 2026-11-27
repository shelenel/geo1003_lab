#align(center)[= Lab 1 Report]
#align(center)[== GEO1003 - Positioning and Location Awareness]
\
#align(center)[Simon Kasdorp, Alicja Urbańczyk, Ewa Kużelewska
 Shelene Low]

#align(center)[Last updated: 21 November 2026]

= Lab 1a
== Part 1 - Smartphone GNSS: Perimeter and Area

#align(center)[
  #figure(image("images/bk_walk_allpoints.jpg", width: 70%), caption: [All recorded points from smartphone GNSS, extracted from GNSS text file log]) <bk_phone_walk_allpts>
]

/// SHELENE NEEDS TO CHANGE THIS PART TO ONLY USING POINTS WITH 'FIX, GPS' 
/// 

@bk_phone_walk_allpts shows all the recorded points from an android smartphone GNSS, during our walk around the Architecture faculty. This also includes unwanted inaccurate points that do not necessarily correspond correctly to the perimeter of the faculty. As such, pre-processing of the points was done in QGIS by removing manually these unwanted points before the calculation of the area and perimeter. Such points include those that lie within the interior of the building.

#align(center)[
  #figure(image("images/bk_walk_concave-hull.png", width: 50%), caption: [Generated concave hull in QGIS, based on recorded points from smartphone GNSS]
  ) <concave-hull>
]

After removing the unwanted points, a concave hull was made with the resulting points using the `Concave Hull (by layer)` function in QGIS. As observed in @concave-hull, the resulting concave hull is not accurate and greatly changes the integrity of the building footprint.

Regardless, the perimeter and area were calculated based on the resulting concave hull, using `$area` and `$perimeter` in the `Field Calculator` of QGIS. A concave hull was chosen instead of a convex hull because of the shape of the building, since the building is not a a perfect rectangle (but with 'indents') and an attempt was made to preserve the integrity of the shape of the building. A threshold of 0.05 was used to generate the concave hull, it was the smallest number we tested which attempted to preserve the building footprint the best without gaps or big distortions. 

*An area of approximately $20,261m^2$ was obtained, with an approximate perimeter of $856m$.*

= Lab 1b
== RTK measuring - Perimeter and Area

After cleaning the data such that we can obtain the longitude and latitude for each point, we connect the points in the order they were obtained. This leads to a counterclockwise trace around the building, visible in the black lines in Figure 2. We obtain the perimeter from summing the length of the line segments using a Python script. The area was obtained using QGIS. We first turned the connected line segments into a polygon using the Polygonize function. After this we could calculate the area using the field calculator with `$area`.

*We calculated an area of $13116m^2$ and a perimeter of 1141m.*


== Part 2 - Precision of GPS code observations 
To asses the precision of the GPS observations, we made 10- minute measurements in two distinct locations - one
in an area with most of the sky uncovered, and one with the line of sight in the southern direction blocked
by a building. These locations were chosen to compare how the precision of the observations depends on the visibility of satellites.

The points are first transformed into the RD system EPSG:28992. This is done to obtain the coordinate values in a cartesian system, and
to calculate the statistical parameters in meters. The points are then
== Part 3 - Mission planning and DOP

= Lab 1b
== Part 4 - Survey grade GNSS-RTK measurements

In order to preserve as much integrity of the building shape and to obtain more accurate results, we thought it would be best to collect measurements from every corner of the building as much as possible. As such, we mapped most of the corner points of the building in QGIS (see @wanted-points) that we wanted to measure using the GNSS-RTK equipment. This entailed a total of 80 points.

#align(center)[
  #figure(image("images/part4_wanted-points_bk.png", width: 60%), caption: [Mapped points from most corners of the BK building]
  ) <wanted-points>
]

The RTK fix status, reported horizontal (HDOP) and vertical (VDOP) accuracy, number of satellites, epoch (date and time) and antenna height are provided in Table. All points were recorded with a RTK network fix with an antenna height of 2 meters, and were taken during 20 November 2026. A report was generated from the taken measurements, with details of each recorded vertex. An example is provided for one recorded vertex, shown in @gnss-point-example.

#align(center)[
  #figure(image("images/part4_gnss_example.png", width: 100%), caption: [Example of recorded details from first GNSS recorded vertex]
  ) <gnss-point-example>
]

For the full report with details on all recorded points, please refer to the  GitHub repository of this assignment where the report is uploaded. #footnote[The full report can be found in the data folder here: https://github.com/shelenel/geo1003_lab]


= Lab 1c
== Part 5 - RDNAPTRANS: perimeter, area and NAP heights 

== Part 6 - Re-assess the smartphone measurements

== Part 7 - PDOK: perimeter and area 
From using the maps and tools from PDOK #footnote[https://app.pdok.nl/viewer/], an 
*area of 10,000$m^2$ was obtained* by tracing the building and calculating the area using 'Polygon meten'. 

#align(center)[
  #figure(image("images/part7_pdok_area.png", width: 90%), caption: [Calculated area of BK with 'Polygon meten']
  ) <pdok-area>
]

*1211.53m was obtained for the perimeter* by using the 'Line meten' tool. 

#align(center)[
  #figure(image("images/part7_pdok_perimeter.png", width: 90%), caption: [Calculated perimeter of BK with 'Polygon meten']
  ) <pdok-perimeter>
]


== Part 8 - Conclusions and recommendations

=== Area

We have attempted to compared our calculated area results with official statistics. 

Firstly, the official floor area provided by TU Delft is 36,0000 $m^2$ #footnote[https://www.tudelft.nl/en/architecture-and-the-built-environment/about-the-faculty/the-building/]. However, this is not a good comparison since our calculations are based on the building (lot) area and not a calculation of the building internally. 

The PDOK calculation using the aerial photo is also not very precise due to the fact that it is highly dependent on how a user selects points on the map to be measured, especially when the aerial photo presents angles of the buildings rather than a flat top-down view. 

=== Recommendations

We have attempted at different methods to better estimate the area and perimeter, namely 2 methods: through polygon tracing of the building footprint in QGIS and referencing open-source data from 3DBAG #footnote[https://3dbag.nl/en/viewer] or OpenKaartData #footnote[https://openkaartdata.nl/]

#align(center)[
  #figure(image("images/part8_openkaart.png", width: 100%), caption: [OpenKaart attributes of the BK faculty]
  ) <openkaart>
]


