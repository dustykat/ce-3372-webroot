#!/usr/bin/python
# SolidsInRivers.py
# Uses HMTL POST method
# Computer Name(s): localhost on Theodore's MacBook Pro 15
#                 : theodores-pro.ttu.edu on Theodore's MacPro
import cgi, cgitb , time  # Import modules for CGI handling
import subprocess  # Import subprocess module for handling system calls
# Create instance of FieldStorage 
form = cgi.FieldStorage()
# Get inputs from fields
exponent = float(form.getvalue('exponent')
alpha    = float(form.getvalue('alpha')
linesy = float(form.getvalue('linesy')
linesx = float(form.getvalue('linesx')
title = str(form.getvalue('title')
xlabel = str(form.getvalue('xlabel')
ylabel = str(form.getvalue('ylabel')
xyzfilename = str(form.getvalue('xyzfilename')
# Build the input file
#ofile = open("/var/www/html/wordpress/OK2Write/SolidsInRivers/input.dat","w") # open a file to transfer input stream to R
#ofile.write(repr(mySlope) + "\n")
#ofile.write(repr(myD50)+ "\n")
#ofile.write(repr(myQ)+ "\n")
#ofile.write(repr(myW)+ "\n")
#ofile.write(repr(nxp)+ "\n")
#ofile.write(repr(near)+ "\n")
#ofile.close()
# Build the system command
#path_to_Rscript = "/usr/bin/Rscript"
#commando = path_to_Rscript + " SolidsInRiversCGI-BINcopy.R"
return_code = 1  #  Set return code to 1 (Fail)
# Here we run SolidsInRiversCGI-BIN.R, and PIPE stdout to the solidsInrivers object
#solidsInrivers = subprocess.Popen(commando, stdout=subprocess.PIPE, shell = True)  # run process
#output, err = solidsInrivers.communicate() # capture output from stdout (command line)
#return_code = solidsInrivers.returncode # capture the return code
#plotfile = ' <img src = "/OK2Write/SolidsInRivers/plot.jpg" width= "800" height = "500"> '
# Prepare the output HTML 
now = time.strftime("%c")
print "Content-type:text/html\r\n"  # should have two returns and line feeds
print "<html>"
print "<style> table, th, td {border: 1px solid black;} </style>"
print "<head>"
print "<title> Solids in Rivers Estimate </title>"
print "</head>"
print "<body>"
print "<p style ="""" "font-family:arial" """ ">"
print "Solids in Rivers Estimate <br/><br/> "
print "Machine Name : theodore-macbookpro.ttu.edu <br/>"
print "Run Date : " , now ," <br/> "
print "<table style="""" "width:99%" """ ">"
print "<tr>"
print "<td>------ INPUT VALUES ------</td> <td> </td> <td> </td>"
print "</tr>"
print "<tr> <td> Gridding Exponent = </td> <td> ", exponent," </td> <td> Dimensionless </td> </tr> "
print "<tr> <td> Smoothing Parameter = </td> <td> ", alpha , " </td> <td> meters </td> </tr> "
print "<tr> <td> Grid Lines X = </td> <td> ", linesx , "</td> <td> cubic meters per second </td> </tr> "
print "<tr> <td> Grid Lines Y = </td> <td> ", linesy, "</td> <td> meters per second </td> </tr> "
print "<tr> <td> Plot Title = </td> <td> ", title, "</td> <td> n = 2 is Euclidean Norm </td> </tr> "
print "<tr> <td> X-Axis Label = </td> <td> ", xlabel, "</td> <td> Search Count </td> </tr> "
print "<tr> <td> Y-Axis Label = </td> <td> ", ylabel, "</td> <td> Search Count </td> </tr> "
print "<tr> <td> XYZ Filename = </td> <td> ", xyzfilename, "</td> <td> Search Count </td> </tr> "
#print "COMMAND TO RUN : ", commando, "<br/>"
print "<tr> <td>------ COMPUTED RESULT ------ </td> <td> </td> <td> </td> "
print "Return Code : ",return_code, " <br/>"
# split the output from R script
#op1,op2 = output.split(" ")
#print "<tr> <td> Estimated Solids Flux = </td> <td> ", op1, "</td> <td> kg/m/sec </td> </tr> "
#print "<tr> <td> Estimated Solids Concentration = </td> <td> ", op2, "</td> <td> parts per hundred thousand </td> </tr> "
print "</table><br/>"
#print "Bar Plots of 5-Nearest Neighbor Values, Input Values, and Estimates (based on all search neighbors)"
#print "<tr>"
#print "<table style="""" "width:99%" """ ">"
#print "<td>"
#print plotfile
#print "</td>"
#print "</tr>"
#print "</p>"
print "</body>"
print "</html>"
# end of script