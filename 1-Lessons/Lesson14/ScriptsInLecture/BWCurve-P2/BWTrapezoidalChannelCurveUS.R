# Backwater Curves, variable step method, prisimatic channels only!
rm(list=ls()) # deallocate memory
# Illustrates use of R as a programming environment
# Direct port of FORTRAN code, so code is NOT R efficient
# 
# Depth-Area Function - Trapezoidal
area<-function(depth,width,sideslope){
	area<-depth*width + depth*(depth*sideslope);
	return(area)
	}
# Wetted perimeter function for rectangular channel
perimeter<-function(depth,width,sideslope){
	perimeter<-width+2*sqrt(depth^2+(depth*sideslope)^2);
	return(perimeter)
	}
# Hydraulic radius function
radius<-function(area,perimeter){
	radius<-area/perimeter;
	return(radius)
	}
# Friction slope function
slope_f<-function(discharge,mannings_n,area,radius){
	slope_f<-(discharge^2)*(mannings_n^2)/((1.00^2)*(radius^(4/3))*(area^2) ); #compute friction slope
	return(slope_f)
}
slope_fUS<-function(discharge,mannings_n,area,radius){
  slope_f<-(discharge^2)*(mannings_n^2)/((1.49^2)*(radius^(4/3))*(area^2) ); #compute friction slope
  return(slope_f)
}
# 2-point average
avg2point<-function(x1,x2){
	avg2point<-0.5*(x1+x2);
	return(avg2point)
  } 
# normal-depth
flow_normalUS <- function(depth,width,sideslope,mannings_n,slope){
  ar <- area(depth,width,sideslope)
  pw <- perimeter(depth,width,sideslope)
  rh <- radius(ar,pw)
  flow_normalUS <- (1.49/mannings_n)*ar*(rh^(2/3))*sqrt(slope)
  return(flow_normalUS)
}
# Backwater curve function in US Customary
backwaterUS<-function(begin_depth,end_depth,how_many,discharge,width,mannings_n,slope,sideslope){
#
## Example function call
##  zz<-backwater(begin_depth=8,end_depth=5,how_many=30,discharge=55.4,width=5,mannings_n=0.02,slope=0.001)
## Numerical values are values used in essay, they correspond to a particuar example from Koutitas 1983
#
# Other functions must exist otherwise will spawn errors
#
# Prepare space for vectors
g <- 32.2
depth<-numeric(0)  # numeric vector for depths
bse<-numeric(0) # numeric vector for bottom elevations
wse<-numeric(0) # numeric vector for water surface elevations
delta_depth<-(begin_depth-end_depth)/(how_many)  # change in depth for finding spatial steps
depth[1]<-begin_depth # assign downstream value
for (i in 2:how_many){depth[i]<-depth[1]-i*delta_depth} # uniform depths
velocity<-discharge/area(depth,width,sideslope) # velocity for each depth
deltax<-numeric(0) # numeric vector for spatial steps
# next for loop is very FORTRANesque!  
for (i in 1:(how_many-1)){
    depth_bar<-avg2point(depth[i],depth[i+1]); #compute average depth in reach
    area_bar<-area(depth_bar,width,sideslope); #compute average area in reach
    perimeter_bar<-perimeter(depth_bar,width,sideslope); #compute average wetted perimeter
    radius_bar<-radius(area_bar,perimeter_bar); #compute average hydraulic radius
    friction<-slope_fUS(discharge,mannings_n,area_bar,radius_bar) #compute friction slope
    deltax[i]<-( (depth[i+1]+(velocity[i+1]^2)/(2*g)) - (depth[i] + (velocity[i]^2)/(2*g)) )/(slope-friction); # compute change in distance for each change in depth
}
distance<-numeric(0); # space for computing cumulative distances
distance[1]<-0;
bse[1]<-0; # bottom elevation at origin
for (i in 2:(how_many)){
	distance[i]<-distance[i-1]+deltax[i-1]; # spatial distances
	bse[i]<-bse[i-1]-deltax[i-1]*slope; # bottom elevations
	}
wse<-bse+depth # water surface elevations
# output
plot(distance,wse,col="blue",type="l",lwd=8,ylim=c(min(bse),max(wse)));
lines(distance,bse,type="l",col="grey",lwd=6);
z<-cbind(distance,depth,bse,wse) # bind output into 4 columns
######## this shit custom for problem 2!! ###############
message("normal flow at depth 2.40053 = ",flow_normalUS(2.40053,3.5,2,0.022,0.012))
message("critical flow at depth   2.7 = ",flow_normalUS(2.40053,3.5,2,0.022,0.012))
message("distance to normal flow      = ",distance[how_many])
return(z)
#
}
########### backwater curve in SI #################################
backwaterSI<-function(begin_depth,end_depth,how_many,discharge,width,mannings_n,slope){
  #
  ## Example function call
  ##  zz<-backwater(begin_depth=8,end_depth=5,how_many=30,discharge=55.4,width=5,mannings_n=0.02,slope=0.001)
  ## Numerical values are values used in essay, they correspond to a particuar example from Koutitas 1983
  #
  # Other functions must exist otherwise will spawn errors
  #
  # Prepare space for vectors
  g <- 9.81
  depth<-numeric(0)  # numeric vector for depths
  bse<-numeric(0) # numeric vector for bottom elevations
  wse<-numeric(0) # numeric vector for water surface elevations
  delta_depth<-(begin_depth-end_depth)/(how_many)  # change in depth for finding spatial steps
  depth[1]<-begin_depth # assign downstream value
  for (i in 2:how_many){depth[i]<-depth[1]-i*delta_depth} # uniform depths
  velocity<-discharge/area(depth,width) # velocity for each depth
  deltax<-numeric(0) # numeric vector for spatial steps
  # next for loop is very FORTRANesque!  
  for (i in 1:(how_many-1)){
    depth_bar<-avg2point(depth[i],depth[i+1]); #compute average depth in reach
    area_bar<-area(depth_bar,width); #compute average area in reach
    perimeter_bar<-perimeter(depth_bar,width); #compute average wetted perimeter
    radius_bar<-radius(area_bar,perimeter_bar); #compute average hydraulic radius
    friction<-slope_f(discharge,mannings_n,area_bar,radius_bar) #compute friction slope
    deltax[i]<-( (depth[i+1]+(velocity[i+1]^2)/(2*g)) - (depth[i] + (velocity[i]^2)/(2*g)) )/(slope-friction); # compute change in distance for each change in depth
  }
  distance<-numeric(0); # space for computing cumulative distances
  distance[1]<-0;
  bse[1]<-0; # bottom elevation at origin
  for (i in 2:(how_many)){
    distance[i]<-distance[i-1]+deltax[i-1]; # spatial distances
    bse[i]<-bse[i-1]-deltax[i-1]*slope; # bottom elevations
  }
  wse<-bse+depth # water surface elevations
  # output
  plot(distance,wse,col="blue",type="l",lwd=8,ylim=c(0,max(wse)+max(bse)));
  lines(distance,bse,type="l",col="grey",lwd=6);
  z<-cbind(distance,depth,bse,wse) # bind output into 4 columns
  return(z)
  #
}
######### Probelm Solution #########
# Textbook Example
#backwaterSI(begin_depth=8,end_depth=5,how_many=31,discharge=55.4,width=5,mannings_n=0.02,slope=0.001)
# Problem 1 Solution
# backwaterUS(begin_depth=6,end_depth=3,how_many=31,discharge=5000,width=1000,mannings_n=0.022,slope=0.0048,sideslope=0.0)
# Problem 2 Solution
backwaterUS(begin_depth=2.7,end_depth=2.40053,how_many=31,discharge=185,width=3.5,mannings_n=0.022,slope=0.012,sideslope=2.0)