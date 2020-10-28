# Backwater Curves, variable step method, prisimatic channels only!
rm(list=ls()) # deallocate memory
# Illustrates use of R as a programming environment
# Direct port of FORTRAN code, so code is NOT R efficient
# 
# Depth-Area Function
area<-function(depth,width){
	area<-depth*width;
	return(area)
	}
# Wetted perimeter function for rectangular channel
perimeter<-function(depth,width){
	perimeter<-2*depth+width;
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
# Backwater curve function in US Customary
backwaterUS<-function(begin_depth,end_depth,how_many,discharge,width,mannings_n,slope){
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
velocity<-discharge/area(depth,width) # velocity for each depth
deltax<-numeric(0) # numeric vector for spatial steps
# next for loop is very FORTRANesque!  
for (i in 1:(how_many-1)){
    depth_bar<-avg2point(depth[i],depth[i+1]); #compute average depth in reach
    area_bar<-area(depth_bar,width); #compute average area in reach
    perimeter_bar<-perimeter(depth_bar,width); #compute average wetted perimeter
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
plot(distance,wse,col="blue",type="l",lwd=8,ylim=c(0,max(wse)));
lines(distance,bse,type="l",col="grey",lwd=6);
z<-cbind(distance,depth,bse,wse) # bind output into 4 columns
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
  plot(distance,wse,col="blue",type="l",lwd=8,ylim=c(0,max(wse)));
  lines(distance,bse,type="l",col="grey",lwd=6);
  z<-cbind(distance,depth,bse,wse) # bind output into 4 columns
  return(z)
  #
}
######### Probelm Solution #########
# Textbook Example
backwaterSI(begin_depth=0.10,end_depth=0.47,how_many=20,discharge=1.0,width=1.0,mannings_n=0.02,slope=0.000)
# Problem 1 Solution
#backwaterUS(begin_depth=4,end_depth=3,how_many=31,discharge=5000,width=1000,mannings_n=0.022,slope=0.0048)