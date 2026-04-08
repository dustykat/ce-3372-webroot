# MakeFileForExcel.py
#############################################################################
# Script to Read SWMM time series output file, parse contents, and build#####
#  a file for use in subsequent analysis and R plotting for             #####
#      Marsha Sharp Freeway Study                                       #####
#############################################################################
# tgc  7-17-2016
# Main problem is an extra CR/LF in the SWMM file.  DOS2UNIX does not fix
#
## Read using for loop -- note that "line" is the iterable
## Forward Declare Variables
## Lets also count how many lines are read!
xy = [] # a null list for reading the file lines
days = [] # a null list for storing days (as integer or float)
hours = [] # a null list for storing hours (as character)
etime = [] # a null list for storing elapsed time (computed as float)
depth = [] # a null list for storing node depth (as float)
#
rowNumA = 0  # counter for how many rows get read
colNumA = 0  # counter for how many columns get read
#
################################################################################
#   Prompt for Input and Output File Names                                    ##
################################################################################
inFile = raw_input("Enter Input  File Name \n")
inTime = raw_input("Enter Time Increment \n")
ouFile = raw_input("Enter Output File Name \n")
inFile = str(inFile)
inTime = float(inTime)
ouFile = str(ouFile)
#debug print inFile
#debug print ouFile
Afile = open(inFile,"r")  # Open a connection from the program to the file
##########################################################################################
# Read the input file -- notice the line skips -- turn on debug lines to find           ##
#  skip count for different kinds of SWMM files                                         ##
##########################################################################################
how_many_lines = 0
for line in Afile:
## Echo First 4 Lines
    if how_many_lines < 3:
        print (line)
        how_many_lines += 1
    else:
        break
####### END ECHO ###############
print how_many_lines # don't really need to keep this but useful for debug
####################################
####### Now Read the Data ##########
####################################
for line in Afile:
    xy.append([str(n) for n in line.strip().split()])
    how_many_lines += 1
    rowNumA += 1
Afile.close() # Disconnect the file
colNumA = len(xy[0]) # Get how many columns
##########################################################################################
####### Now Process the String Array to TypeCast values into new arrays ##################
##########################################################################################
index = 1
for i in range(0,rowNumA,1):
    days.append(float(xy[i][0]))
    hours.append(str(xy[i][1]))
    etime.append(float(index)*inTime)
    depth.append(float(xy[i][2]))
    index += 1 # increment index
###########################################################################################
######## Now want to write the output in distance, then profile order #####################
######## Write to an output file -- See P4E book for script detail    #####################
###########################################################################################
ofile = open(ouFile,"w") # Open a connection from the program to the file -- w clobbers existing data
message = "".join("days"+" "+"etime"+" "+"depth")+ "\n"
ofile.write(message)
howManyRows = len(depth)
for i in range(0,howManyRows):   # thus is a really fucked up way to format the output, fix someday ...
    message = "".join(repr(days[i])+" "+repr(etime[i])+" "+repr(depth[i]) )+ "\n"
    ofile.write(message)
ofile.close() # disconnect the file
print "DONE!"
################ DONE ! ###################################################################
