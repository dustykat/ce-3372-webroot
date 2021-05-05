# ES-2

## Purpose:
Demonstrate ability to interpret and render from an image a topographic map, and overlay the topographic map onto the basemap.

## Background
Figure 1 is a subdivision conceptual map for Somewhere, USA. The numbers on the map are land surface elevations located at the decimal points in the drawing. Along the bottom edge of the map is a black line segment (with arrowheads at each end) that indicates a distance of 1,100 feet on the map. The black circle in the lower left hand corner is to be used as an origin for X-Y measurements for making XYZ data files.

![](SomewhereUSABaseMap.png)

|Figure 1.  Somewhere USA Study Area|
|---|

The semester design project is the conceptual design and analysis of a water distribution, stormwater collection, and wastewater collection system for this subdivision. All such systems will be influenced by the local topography, so a first step is to build a topographic map to guide design decisions, especially for the stormwater part of the design. The .png file is [located here](https://3.137.111.182/ce-3372-webbook/exercise2/SomewhereUSABaseMap.png) so you can render a larger graphic if needed.

## Exercise
Construct a topographic contour map of the area.

1. Use the indicated origin and find X,Y, and Z coordinates for each displayed elevation. Include example measurements for one or two points (as if someone else would have to check your work)
2. Arrange those coordinates into an ASCII (text) file where each row of the file is a coordinate triple. 
3. Use the ASCII file to make a topographic map (software choice is yours; you can use http://theodore-odroid.ttu.edu/documents/toolbox/ordinarytools/SimpleContourMap/ if you wish.  The credentials are username==`TTUStudent` password==`id10t` ) 
4. Use graphics tools to overlay the topographic map onto the base map (this step is tricky, you will have to read how to make a layer have transparent portions to do the overlay, scaling and alignment take some effort) 

## Deliverables:

A short report (1 page) where you describe your map making activity, including how you built the ASCII input file, and your rendered topographic map.  Put both of these into a single PDF file to upload to the Blackboard Server.


