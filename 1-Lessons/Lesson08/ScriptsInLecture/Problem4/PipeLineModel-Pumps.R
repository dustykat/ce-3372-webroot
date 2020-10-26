# Steady Flow in a Pipe Network Using Hybrid Method (and Newton-Raphson) based on
# Haman YM, Brameller A. Hybrid method for the solution of piping networks. Proc IEEE 1971;118(11):1607–12.
# Calculates Steady Flow and Head in Pipe Network with Pumps
# Clear all existing objects
 rm(list=ls())
###############################################################
##############Forward Define Support Functions#################
###############################################################
# Jain Friction Factor Function -- Tested OK 23SEP16
friction_factor <- function(roughness,diameter,reynolds){
  temp1 <- roughness/(3.7*diameter);
  temp2 <- 5.74/(reynolds^(0.9));
  temp3 <- log10(temp1+temp2);
  temp3 <- temp3^2;
  friction_factor <- 0.25/temp3;
  return(friction_factor)
}
# Velocity Function
velocity <- function(diameter,discharge){
  velocity <- discharge/(0.25*pi*diameter^2)
  return(velocity)
}
# Reynolds Number Function
reynolds_number <- function(velocity,diameter,mu){
  reynolds_number <- abs(velocity)*diameter/mu
  return(reynolds_number)
}
# Geometric factor function
k_factor <- function(howlong,diameter,gravity){
  k_factor <- (16*howlong)/(2.0*gravity*pi^2*diameter^5)
  return(k_factor)
}
# Pump Curve factor function
p_factor <- function(shutoff,constant,exponent,flow){
  p_factor <- shutoff/abs(flow) - constant*abs(flow^(exponent-1))
  return(p_factor)
}
# Read Input Data Stream from File
zz <- file("Problem1ES8.txt", "r") # Open a connection named zz to file named PipeNetwork.txt
pumpCount <- as.numeric(readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
nodeCount <- as.numeric(readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
pipeCount <-as.numeric(readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
elevation <-(readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
diameter <- (readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
distance <- (readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
roughness <- (readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
viscosity <- (readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
flowguess <- (readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
nodearcs <- (readLines(zz, n = nodeCount, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
rhs_true <- (readLines(zz, n = 1, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
pumps <- (readLines(zz, n = pumpCount, ok = TRUE, warn = TRUE,encoding = "unknown", skipNul = FALSE));
close(zz) # Close connection zz
#
# Convert Input Stream into Numeric Structures
elevation <-as.numeric(unlist(strsplit(elevation,split=" ")))
diameter <-as.numeric(unlist(strsplit(diameter,split=" ")))
distance <-as.numeric(unlist(strsplit(distance,split=" ")))
roughness <-as.numeric(unlist(strsplit(roughness,split=" ")))
viscosity <-as.numeric(unlist(strsplit(viscosity,split=" ")))
flowguess <-as.numeric(unlist(strsplit(flowguess,split=" ")))
nodearcs <-as.numeric(unlist(strsplit(nodearcs,split=" ")))
rhs_true <-as.numeric(unlist(strsplit(rhs_true,split=" ")))
pumps <-as.numeric(unlist(strsplit(pumps,split=" ")))
# convert nodearcs a matrix
# We will need to augment this matrix for the actual solution -- so after augmentation will deallocate the memory
nodearcs <-matrix(nodearcs,nrow=nodeCount,ncol=pipeCount,byrow = TRUE)
pumps <-matrix(pumps,nrow=pumpCount,ncol=4,byrow=TRUE)
# echo input
message("Node Count = ",nodeCount)
message("Pipe Count = ",pipeCount)
message("Pump Count = ",pumpCount)
message("Pipe Lengths = "); distance
message("Pipe Diameters = "); diameter
message("Pipe Roughness = "); roughness
message("Fluid Viscosity = ",viscosity)
message("Initial Guess = "); flowguess
message("Node-Arc-Incidence Matrix = "); nodearcs
# 
# create the augmented matrix 
print(pumps)
headCount <- nodeCount
flowCount <- pipeCount
augmentedRowCount <- nodeCount+pipeCount
augmentedColCount <- flowCount+headCount
augmentedMat <- matrix(0,nrow=augmentedRowCount,ncol=augmentedColCount,byrow = TRUE)
#print(augmentedMat)
# build upper left partition of matrix -- this partition is constants from node-arc matrix
for (i in 1:nodeCount){
  for (j in 1:flowCount){
    augmentedMat[i,j] <- nodearcs[i,j]
  }
}
#print(augmentedMat)
# build lower right partition of matrix -- this partition is -1*transpose(node-arc) matrix
istart <- nodeCount+1
iend <- nodeCount+pipeCount
jstart <- flowCount+1
jend <- flowCount+headCount
for (i in istart:iend ){
  for(j in jstart:jend ){
    augmentedMat[i,j] <- -1*nodearcs[j-jstart+1,i-istart+1]
  }
}
#print(augmentedMat)
# here it should be safe to delete the nodearc matrix
rm(nodearcs)
# Need some vorking vectors
 HowMany <- 50
 tolerance1 <- 1e-24
 tolerance2 <- 1e-24
 velocity_pipe <-numeric(0)
 reynolds <- numeric(0)
 friction <- numeric(0)
 geometry <- numeric(0)
 lossfactor <- numeric(0)
 addedhead <- numeric(0)
 jacbMatrix <- matrix(0,nrow=augmentedRowCount,ncol=augmentedColCount,byrow = TRUE)
 gq <- numeric(0)
 solvecguess <- numeric(length=augmentedRowCount)
 solvecnew <- numeric(length=augmentedRowCount)
 solvecguess[1:flowCount] <- flowguess[1:flowCount]
 
 # compute geometry factors (only need once, goes outside iteration loop)
 for (i in 1:pipeCount)
 {
   geometry[i] <- k_factor(distance[i],diameter[i],32.2)
 }
#print(geometry)
 
 # going to wrap below into an interation loop -- forst a single instance
for (iteration in 1:HowMany){
################### BEGIN ITERATION OUTER LOOP ###########################
 # compute current velocity
 for (i in 1:pipeCount)
 {
   velocity_pipe[i]<-velocity(diameter[i],flowguess[i])
 }
 velocity_pipe
 # compute current reynolds
 for (i in 1:pipeCount) 
 {
   reynolds[i]<-reynolds_number(velocity_pipe[i],diameter[i],viscosity)
 }
 reynolds
 # compute current friction factors
 for (i in 1:pipeCount) 
 {
   friction[i]<-friction_factor(roughness[i],diameter[i],reynolds[i])
 }
 friction
 # compute current loss factor
 for (i in 1:pipeCount)
 {
   lossfactor[i] <- friction[i]*geometry[i]*abs(flowguess[i])  
 }
 lossfactor
 # compute the current pump factor
 if(pumpCount > 0){
  for (i in 1:pumpCount)
    {
      addedhead[i] <- p_factor(pumps[i,2],pumps[i,3],pumps[i,4],flowguess[pumps[i,1]]) 
    }
  }
 # build the function matrix
 # operate on the lower left partition of the matrix
 istart <- nodeCount+1
 iend <- nodeCount+pipeCount
 jstart <- 1
 jend <- flowCount
 for (i in istart:iend ){
   for(j in jstart:jend ){
     if ((i-istart+1) == j)  {augmentedMat[i,j] <- -1*lossfactor[j];
      if(pumpCount > 0){
        for(ipump in 1:pumpCount) {
          if(j == pumps[ipump,1]) augmentedMat[i,j] <- addedhead[ipump]
        }
      }
    }
   }
 }
# print(augmentedMat)
 # now build the current jacobian
 # slick trick -- we will copy the current function matrix, then modify the lower left partition
 jacbMatrix <- augmentedMat
 jacbMatrix
 # build the function matrix
 # operate on the lower left partition of the matrix
 istart <- nodeCount+1
 iend <- nodeCount+pipeCount
 jstart <- 1
 jend <- flowCount
 for (i in istart:iend ){
   for(j in jstart:jend ){
     if ((i-istart+1) == j) jacbMatrix[i,j] <- 2*jacbMatrix[i,j]
     
   }
 }
jacbMatrix
rhs_true
solvecnew
solvecguess
# now build the gq() vector
gq <- augmentedMat %*% solvecguess - rhs_true
gq
dq <- solve(jacbMatrix,gq)
# update the solution vector
solvecnew <- solvecguess - dq
solvecnew
# # now test for stopping
test <- abs(solvecnew - solvecguess)
if( t(test) %*% test < tolerance1){
  message("Update not changing -- exit loop and report current update")
  message("Iteration count = ",iteration)
  solvecguess <- solvecnew
  flowguess[1:flowCount] <- solvecguess[1:flowCount]
  break
}
test <- abs(gq)
if( t(test) %*% test < tolerance2 ){
  message("G(Q) close to zero -- exit loop and report current update")
  message("Iteration count = ",iteration)
  solvecguess <- solvecnew
  flowguess[1:flowCount] <- solvecguess[1:flowCount]
  break
}
solvecguess <- solvecnew
flowguess[1:flowCount] <- solvecguess[1:flowCount]
################### END OF ITERATION OUTER LOOP #############################
}
message("Current Results")
print(cbind(solvecguess,gq,dq))
#print(cbind(friction,diameter,distance,velocity_pipe))
if(pumpCount >0){
  for (ipump in 1:pumpCount)
    message("Pump # ",ipump," at Q = ",solvecguess[pumps[ipump,1]])
}
###### compute pressures #######
istart <- pipeCount+1
iend <- pipeCount+nodeCount
#print(istart)
#print(iend)
totalhead <- solvecguess[istart:iend]
pressure <- totalhead-elevation
pressure <- pressure*(62.4)/(144)
print(pressure)