# Steady Flow in a Pipe Network Using Hybrid Method ( and Newton - Raphson ) based on
# Haman YM , Brameller A. Hybrid method for the solution of piping networks . Proc IEEE
#1971;118(11) :1607?12.
#
# Clear all existing objects
rm( list =ls ())
###############################################################
#############################################################
############## Forward Define Support Functions #################
#############################################################
# Jain Friction Factor Function -- Tested OK 23 SEP16
friction_factor <- function( roughness , diameter , reynolds ){
  temp1 <- roughness /(3.7* diameter );
  temp2 <- 5.74/( reynolds ^(0.9) );
  temp3 <- log10 ( temp1 + temp2 );
  temp3 <- temp3 ^2;
  friction_factor <- 0.25/ temp3 ;
  return ( friction_factor )
}
# Velocity Function
velocity <- function( diameter , discharge ){
  velocity <- discharge /(0.25* pi* diameter ^2)
  return ( velocity )
}
# Reynolds Number Function
reynolds_number <- function ( velocity , diameter ,mu){
  reynolds_number <- abs ( velocity )* diameter /mu
  return ( reynolds_number )
}
# Geometric factor function
k_factor <- function( howlong , diameter , gravity ){
  k_factor <- (16* howlong ) /(2.0* gravity *pi ^2* diameter ^5)
  return ( k_factor )
}
###############################################################
# Read Input Data Stream from File
zz <- file ("PipeNetwork.txt", "r") # Open a connection named zz to file named PipeNetwork . txt
nodeCount <- as.numeric( readLines(zz , n = 1, ok = TRUE , warn = TRUE , encoding = " unknown ",
                                      skipNul = FALSE ))
pipeCount <-as.numeric( readLines(zz , n = 1, ok = TRUE , warn = TRUE , encoding = " unknown ",
                                     skipNul = FALSE ))
diameter <- ( readLines(zz , n = 1, ok = TRUE , warn = TRUE , encoding = " unknown ", skipNul =
                           FALSE ))
distance <- ( readLines(zz , n = 1, ok = TRUE , warn = TRUE , encoding = " unknown ", skipNul =
                           FALSE ))
roughness <- ( readLines(zz , n = 1, ok = TRUE , warn = TRUE , encoding = " unknown ", skipNul =
                            FALSE ))
viscosity <- ( readLines(zz , n = 1, ok = TRUE , warn = TRUE , encoding = " unknown ", skipNul =
                            FALSE ))
flowguess <- ( readLines(zz , n = 1, ok = TRUE , warn = TRUE , encoding = " unknown ", skipNul =
                            FALSE ))
nodearcs <- ( readLines(zz , n = nodeCount , ok = TRUE , warn = TRUE , encoding = " unknown ",
                         skipNul = FALSE ))
rhs_true <- ( readLines(zz , n = pipeCount + nodeCount , ok = TRUE , warn = TRUE , encoding = "
                         unknown ", skipNul = FALSE ))
close(zz) # Close connection zz
#
# Convert Input Stream into Numeric Structures
diameter <-as.numeric( unlist( strsplit ( diameter , split =" ")))
distance <-as.numeric( unlist( strsplit( distance , split =" ")))
roughness <-as.numeric( unlist( strsplit( roughness , split =" ")))
viscosity <-as.numeric( unlist( strsplit( viscosity , split =" ")))
flowguess <-as.numeric( unlist( strsplit( flowguess , split =" ")))
nodearcs <-as.numeric( unlist( strsplit( nodearcs , split =" ")))
rhs_true <-as.numeric( unlist( strsplit( rhs_true , split =" ")))
# convert nodearcs a matrix
# We will need to augment this matrix for the actual solution -- so after augmentation will deallocate the memory
nodearcs <- matrix( nodearcs , nrow = nodeCount , ncol = pipeCount , byrow = TRUE )
# echo input
message(" Node Count = ", nodeCount )
message(" Pipe Count = ", pipeCount )
message(" Pipe Lengths = "); distance
message(" Pipe Diameters = "); diameter
message(" Pipe Roughness = "); roughness
message(" Fluid Viscosity = ", viscosity )
message(" Initial Guess = "); flowguess
message(" Node -Arc - Incidence Matrix = "); nodearcs
#########
# create the augmented matrix
headCount <- nodeCount
flowCount <- pipeCount
augmentedRowCount <- nodeCount + pipeCount
augmentedColCount <- flowCount + headCount
augmentedMat <- matrix(0, nrow = augmentedRowCount , ncol = augmentedColCount , byrow = TRUE )
#
augmentedMat
# build upper left partition of matrix -- this partition is constants from node - arc matrix
for(i in 1: nodeCount ){
  for(j in 1: flowCount ){
    augmentedMat[i,j] <- nodearcs[i,j]
  }
}
augmentedMat
# build lower right partition of matrix -- this partition is -1* transpose (node - arc ) matrix
istart <- nodeCount +1
iend <- nodeCount + pipeCount
jstart <- flowCount +1
jend <- flowCount + headCount
for(i in istart : iend ){
  for(j in jstart : jend ){
    augmentedMat[i,j] <- -1* nodearcs[j- jstart +1,i- istart +1]
  }
}
augmentedMat
# here it should be safe to delete the nodearc matrix
rm( nodearcs )
# Need some vorking vectors
HowMany <- 50
tolerance1 <- 1e-24
tolerance2 <- 1e-24
velocity_pipe <- numeric(0)
reynolds <- numeric(0)
friction <- numeric(0)
geometry <- numeric(0)
lossfactor <- numeric(0)
jacbMatrix <- matrix(0, nrow = augmentedRowCount , ncol = augmentedColCount , byrow = TRUE )
gq <- numeric(0)
solvecguess <- numeric( length = augmentedRowCount )
solvecnew <- numeric( length = augmentedRowCount )
solvecguess[1: flowCount ] <- flowguess[1: flowCount ]
# compute geometry factors ( only need once , goes outside iteration loop )
for(i in 1: pipeCount )
{
  geometry[i] <- k_factor( distance [i], diameter [i ] ,32.2)
}
geometry
# going to wrap below into an interation loop -- forst a single instance
for( iteration in 1: HowMany ){
  ################### BEGIN ITERATION OUTER LOOP ###########################
  # compute current velocity
  for(i in 1: pipeCount )
  {
    velocity_pipe [i]<- velocity ( diameter[i], flowguess[i])
  }
  # compute current reynolds
  for(i in 1: pipeCount )
  {
    reynolds [i]<- reynolds_number( velocity_pipe[i], diameter[i], viscosity )
  }
  # compute current friction factors
  for(i in 1: pipeCount )
  {
    friction [i]<- friction_factor( roughness[i], diameter[i], reynolds[i])
  }
  # compute current loss factor
  for(i in 1: pipeCount )
  {
    lossfactor[i] <- friction[i]* geometry[i]* abs(flowguess [i])
  }
  # build the function matrix
  # operate on the lower left partition of the matrix
  istart <- nodeCount +1
  iend <- nodeCount + pipeCount
  jstart <- 1
  jend <- flowCount
  for(i in istart : iend ){
    for(j in jstart : jend ){
      if((i- istart +1) == j) augmentedMat[i,j] <- -1* lossfactor[j]
    }
  }
  # now build the current jacobian
  # slick trick -- we will copy the current function matrix , then modify the lower left partition
  jacbMatrix <- augmentedMat
  # build the function matrix
  # operate on the lower left partition of the matrix
  istart <- nodeCount +1
  iend <- nodeCount + pipeCount
  jstart <- 1
  jend <- flowCount
  for(i in istart : iend ){
    for(j in jstart : jend ){
      if((i- istart +1) == j) jacbMatrix[i,j] <- 2* jacbMatrix[i,j]
    }
  }
  # now build the gq () vector
  gq <- augmentedMat %*% solvecguess - rhs_true
  gq
  dq <- solve( jacbMatrix ,gq)
  # update the solution vector
  solvecnew <- solvecguess - dq
  solvecnew
  # # now test for stopping
  test <- abs( solvecnew - solvecguess )
  if( t( test ) %*% test < tolerance1 ){
    message(" Update not changing -- exit loop and report current update ")
    message(" Iteration count = ", iteration )
    solvecguess <- solvecnew
    flowguess[1: flowCount ] <- solvecguess[1: flowCount ]
    break
  }
  test <- abs(gq)
  if( t( test ) %*% test < tolerance2 ){
    message ("G(Q) close to zero -- exit loop and report current update ")
    message (" Iteration count = ", iteration )
    solvecguess <- solvecnew
    flowguess[1: flowCount ] <- solvecguess[1: flowCount ]
    break
  }
  solvecguess <- solvecnew
  flowguess[1: flowCount ] <- solvecguess [1: flowCount ]
  ################### END OF ITERATION OUTER LOOP #############################
}
message (" Current Results ")
print( cbind ( solvecguess ,gq ,dq))
print( cbind ( friction , diameter , distance , velocity_pipe ))