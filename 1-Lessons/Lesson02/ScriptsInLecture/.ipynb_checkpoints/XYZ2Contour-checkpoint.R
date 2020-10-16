# XYZtoContourOnLine
# A set of scripts to take XYZ files, generate a contour map, and serve the map using a web-interface
# Project uses: R, RScript, Python, HTML, and works with cgi-bin process call
# Intent is code to support UG students at TTU in Water Systems and similar courses
# 
rm(list=ls())
############ Function to Get 3-Point Adjustment Curve #############
################# Used for Map Smoothing ########################## 
get_pump_parm <- function(hshut,hone,htwo,qshut,qone,qtwo){
  # fit a quadratic model to the 3-point curve
  amat <- matrix(0,nrow=3,ncol=2,byrow=TRUE)
  bvec <- numeric(0)
  pumpcrv <- numeric(0)
  # build the amat matrix
  for (irow in 1:3){
    amat[irow,1] <- 1
  }
  amat[1,2] <- qshut^2
  amat[2,2] <- qone^2
  amat[3,2] <- qtwo^2
  # build the bvec
  bvec[1] <- hshut
  bvec[2] <- hone
  bvec[3] <- htwo
  # solve the linear system
  pumpcrv <- solve(t(amat)%*%amat,t(amat)%*%bvec)
  return(pumpcrv)
}
# here is the actual adjust curve function
hpump <- function(hshutoff,pumpconst,flowrate){
  hpump <- hshutoff + pumpconst*abs(flowrate)*flowrate
  return(hpump)
}
#####################################################################
# Read the input data streams specifications
zzTop <- file("XYZParms.txt","r")
mapparm <- readLines(zzTop)
close(zzTop)
# xyz file
xyz <- read.table(file=mapparm[8],header=FALSE)
x <- xyz$V1
y <- xyz$V2
z <- xyz$V3
howmanypoints <- length(x)
# find bounding rectangle
xmin <- min(x)
ymin <- min(y)
xmax <- max(x)
ymax <- max(y)
linesx <- as.numeric(mapparm[3])
linesy <- as.numeric(mapparm[4])
xgrid <- numeric(length=linesx)
ygrid <- numeric(length=linesy)
deltax <- (xmax-xmin)/(linesx-1)
deltay <- (ymax-ymin)/(linesy-1)
zmatrix <- matrix(0,ncol=linesx,nrow=linesy)
# build the xy grid coordinates
xgrid[1] <- xmin
for(i in 2:linesx){
  xgrid[i] <- xgrid[i-1] + deltax
}
ygrid[1] <- ymin
for(j in 2:linesy){
  ygrid[j] <- ygrid[j-1] + deltay
}
# Grid the data onto a rectangle 
rownum <- numeric(0)
distance <- numeric(length = howmanypoints)
sortedZ <- numeric(length = howmanypoints)
sortedD <- numeric(length = howmanypoints)
#exponent <- 2
#alpha <- 100*exponent
exponent <- as.numeric(mapparm[1])
alpha <- as.numeric(mapparm[2])
for (irow in 1:linesy){
  for(jcol in 1:linesx){
    rownum <- 0
    for(krows in 1:howmanypoints){
      distance[krows] <- alpha + sqrt( (xgrid[jcol]-x[krows])^2 + (ygrid[irow]-y[krows])^2 )
    }
    sortedZ <- z[order(distance)]
    sortedD <- distance[order(distance)]
# nearest neighbor method
#    zmatrix[irow,jcol] <- sortedZ[1] 
# inverse distance to a power
       numerator <- 0
       denominator <- 0
       flag <- 0
       for(iii in 1:howmanypoints){
         if(sortedD[iii] == 0) {
           flag <- iii
           break # grid location corresponds to an observation
         }
         numerator <- numerator + sortedZ[iii]/(sortedD[iii]^exponent)
         denominator <- denominator + 1/(sortedD[iii]^exponent)
       }
       zmatrix[irow,jcol] <- numerator/denominator
       if(flag != 0){zmatrix[irow,jcol] <- sortedZ[flag]}
  }
}
# quadratic fit to adjust smoothed map
hshut <- max(z)
hone <- median(z)
htwo <- min(z)
#
qshut <- max(zmatrix)
qone <- median(zmatrix)
qtwo <- min(zmatrix)
#
adjust <- get_pump_parm(hshut,hone,htwo,qshut,qone,qtwo)
#
value <- hpump(adjust[1,1],adjust[2,1],zmatrix)
# 
par(mfrow=c(1,1))
contour2D(value,xgrid,ygrid,main=mapparm[7],xlab=mapparm[5],ylab=mapparm[6],tck=1,lwd=2,drawlabels=TRUE,labcex=1.1,
        xlim=c(0.9*xmin,1.1*xmax),ylim=c(0.9*ymin,1.1*ymax),nlevels=12,col="blue")
lines(x,y,type="p",pch=3)