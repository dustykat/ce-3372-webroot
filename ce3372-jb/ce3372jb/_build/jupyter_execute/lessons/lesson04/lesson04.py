#!/usr/bin/env python
# coding: utf-8

# # Pipeline Head Loss 

# Water moves from higher to lower energy
# 
# - Path of least resistance
# - Head is energy per unit weight of a fluid 
# - Pumps are used to add energy to move water to a higher elevation or over a barrier 
# 
# - Gravity flow: Change in elevation provides the required energy 
# - Pressure flow: Change in pressure provides the required energy 
# 
# Flowing water encounters friction/resistance; hence there is loss of energy along a flow path. 
# The mean section velocity is related to cross sectional flow area and volumetric discharge as:
# 
# $$ \bar{V} = \frac{Q}{A} $$

# 

# ## Continunity at Different Sections
# 
# words
# 
# ## Continunity at Junctions
# 
# ## Energy Equation

# ### Example: Time to Drain a Storage Tank

# In[ ]:





# ### Example: Steady Discharge between Two Reservoirs

# In[ ]:





# ## Head Loss Models (for losses in closed conduits)
# 
# ### Darcy-Weisbach
# 
# The Darcy-Weisbach frictional head-loss model for pipe flow is 
# 
# $$h_f = f \frac{L}{D}\frac{V^2}{2g}$$
# 
# Frictional loss proportional to: 
# - Length
# - Velocity$^2$ 
# 
# Inversely proportional to: 
# - Cross sectional area 
# 
# Loss coefficient ($f$) depends on 
# - Reynolds number (fluid and flow properties) 
# - Roughness height (pipe material properties) 
# 
# #### Reynolds' ($Re_d$) Number
# 
# $$Re_d = \frac{\rho V D}{\mu} = \frac{V D}{\nu}$$
# 
# 
# Find viscosity as function of temperature from table look-up at [http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html) or [http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesSI/WaterPropertiesSI.html](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesSI/WaterPropertiesSI.html) or other source.
# 
# #### Darcy-Weisbach "$f$" Factor
# 
# The friction factor is determined from a Moody Chart or Colebrook-White or Jain equation like:
# 
# $$f = \frac{0.25}{[log10(\frac{k_s}{3.7D}+\frac{5.74}{Re^{0.9}})]^2}$$
# 
# A web-application with a roughness height database is [http://54.243.252.9/toolbox/Databases/RoughnessHeight/RoughnessHeight.html](http://54.243.252.9/toolbox/Databases/RoughnessHeight/RoughnessHeight.html)
# 
# A web-application to compute friction factor given $Re$ and material properties ($k_s$) is [http://54.243.252.9/toolbox/pipehydraulics/FrictionFactor/FrictionFactor.html](http://54.243.252.9/toolbox/pipehydraulics/FrictionFactor/FrictionFactor.html)
# 
# #### Using the D-W model
# 
# To compute headloss is straightforward, first organize your data:
# 
# 1. Material type, lookup roughness height at [http://54.243.252.9/cgi-bin/Databases/RoughnessHeight/RoughnessHeight.py](http://54.243.252.9/cgi-bin/Databases/RoughnessHeight/RoughnessHeight.py) or another source.  Remember to cite the source.
# 2. Viscosity at desired operating temperature, lookup at [http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html) or [http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesSI/WaterPropertiesSI.html](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesSI/WaterPropertiesSI.html) or another source.  Remember to cite the source.
# 3. Use the pipe diameter and desired flowrate to compute a mean section velocity.
# 4. Compute the Reynolds number; use the equation or [http://54.243.252.9/toolbox/fluidmechanics/ReynoldsNumber/ReynoldsNumber.html](http://54.243.252.9/toolbox/fluidmechanics/ReynoldsNumber/ReynoldsNumber.html)
# 5. Compute the friction factor; use the Moody Chart or Jain equation or [http://54.243.252.9/toolbox/pipehydraulics/FrictionFactor/FrictionFactor.html](http://54.243.252.9/toolbox/pipehydraulics/FrictionFactor/FrictionFactor.html)
# 6. Finally compute the head loss as $h_f = f \frac{L}{D}\frac{V^2}{2g}$

# In[ ]:





# ### Hazen-Williams
# 
# #### Hazen-Williams "C" Factor
# 
# #### Hydraulic Radius
# 
# 

# In[ ]:





# ### Chezy-Mannings
# 
# #### Mannings "n" 
# 
# #### Hydraulic Radius
# 
# 

# In[ ]:





# ### Fitting (Minor) Losses
# 

# ## Computing Discharge from Specified Head Loss
# 
# ### Computational Thinking/Data Science Approach (ENGR 1330)
# 
# CT/DS Approach
# 
# * State the programming problem
# * Known (Inputs)
# * Unknown (Outputs)
# * Governing Equation(s)
# * Test the tool
# 
# #### State the programming problem
# 
# Build a tool that takes inputs for the Jain equation and produces an estimate of discharge
# 
# Build an interface (notebook) that accepts the inputs, calls the function, and returns the computed discharge
# 
# #### Known (Inputs)
# Engineer will specify: 
# 
# * Diameter, D; 
# * Length of pipe, L; 
# * Roughness height, e; 
# * Viscosity, $\nu$; 
# * Gravitational acceleration constant, g;
# * Head loss
# 
# #### Unknown (Outputs)
# The tool will compute and report Discharge, Q.
# 
# #### Governing Equation(s)
# A compact form of the equation to be evaluated is
# 
# $
# Q=-0.965 D^2 \sqrt{\frac{gDh_f}{L}}ln( \frac{k_s}{3.7D}+\frac{1.78\nu}{D\sqrt{\frac{gDh_f}{L}}} )
# $

# ```
# # #######prototype function for computation engine #########################
# # Define the prototype function
# from math import log,sqrt
# def jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss):
#     egl_slope = head_loss/pipe_length
#     t1 = sqrt(grabity*pipe_diameter*egl_slope)
#     t2 = roughness/(3.7*pipe_diameter)
#     t3 = 1.78*viscosity
#     jainQ = (-0.965*pipe_diameter**2)*t1*log(t2 + t3/(pipe_diameter*t1))
#     return jainQ
# ```

# ####  Build and Test the tool
# 
# To build and test the tool, we have a couple of additional requirements:
# - computation engine (above)
# - interface engine (to get inputs to send to the computation engine)
# - output engine (to actually run the computations, and present outputs)
# 
# These added parts appear below

# 

# ```    
# # ############ Interface engine ##########################
# def getInputs():
#     global pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss
# # Get pipe diameter, use a simple error trap
#     yes=0
#     while yes == 0:
#         xnow = input("Enter Pipe Diameter \n")
#         try:
#             pipe_diameter = float(xnow)
#             yes =1
#         except:
#             print ("Value should be numeric, try again \n")
# # Get pipe length, use a simple error trap
#     yes=0
#     while yes == 0:
#         xnow = input("Enter Pipe Length \n")
#         try:
#             pipe_length = float(xnow)
#             yes =1
#         except:
#             print ("Value should be numeric, try again \n")
# # Get roughness, use a simple error trap
#     yes=0
#     while yes == 0:
#         xnow = input("Enter Pipe Roughness Height \n")
#         try:
#             roughness = float(xnow)
#             yes =1
#         except:
#             print ("Value should be numeric, try again \n")
# # Get viscosity, use a simple error trap
#     yes=0
#     while yes == 0:
#         xnow = input("Enter liquid viscosity \n")
#         try:
#             viscosity = float(xnow)
#             yes =1
#         except:
#             print ("Value should be numeric, try again \n")
# # Get grabity, use a simple error trap
#     yes=0
#     while yes == 0:
#         xnow = input("Enter gravitational acceleration constant (unit system appropriate) \n")
#         try:
#             grabity = float(xnow)
#             yes =1
#         except:
#             print ("Value should be numeric, try again \n")
# # Get head loss, use a simple error trap
#     yes=0
#     while yes == 0:
#         xnow = input("Enter head loss \n")
#         try:
#             head_loss = float(xnow)
#             yes =1
#         except:
#             print ("Value should be numeric, try again \n")
#     return()
# ```

# ```       
# # ############### Supervisory Control and Output Engine #######################
# getInputs() # call the interface
# discharge = jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss) # call the computation engine
# # output
# print ("Pipe Diameter : ", pipe_diameter)
# print ("Pipe Length : ", pipe_length)
# print ("Pipe Roughness Height : ", roughness)
# print ("Liquid Viscosity : ", viscosity)
# print ("Gravitational acceleration constant : ",grabity) 
# print ("Head loss : ",head_loss)
# print ("Discharge : ",discharge)
# ```

# A cut and paste the code of the code above into a Jupyter Notebook should produce output like:
# 
# ![](ScreenCaptureJain.png)

# #### Refine the Tool for Generalization
# 
# The refinement step would wrap the above script into a single function/notebook for simple use/reuse. If we save to a single file, we can access the script as we wish (using a JupyterLab magic function).  
# 
# > Or, we can put the script onto a server and access via a web interface as is done at [http://54.243.252.9/toolbox/pipehydraulics/QGivenHeadLoss/QGivenHeadLoss.html](http://54.243.252.9/toolbox/pipehydraulics/QGivenHeadLoss/QGivenHeadLoss.html)  
# > The server-side python code is shown below as is the interface HTML
# 
# 

# :::{note}
# The server-side code that performs the functions of input interface is listed below. On an apache web server the code would go in the webroot `/var/www/html/path-to-html/`
# 
# ```
# <!DOCTYPE html PUBLIC >
# <html><head><title>Discharge Given Head Loss</title></head>
# <link rel = "stylesheet" type = "text/css" href = "styles.css" >
# <body>
# <h1> Discharge in Pressure Conduit Given Head Loss </h1>
# 
# <p> Computes Discharge given Diameter, Material, and Head Loss using Swamee Jain (1976) </p>
# <img src = "./QGivenHeadLoss.gif"  > <br/>
# <p>
#   D = Pipe diameter (in feet or meters) <br/>
#   g = Gravitational acceleration constant (32.2 ft/s^2 or 9.8 m/s^2) <br/>
#  hl = Head loss (in feet or meters) <br/>
#   L = Pipe length (feet or meters) <br/>
#  ks = Equivalent sand roughness height (a material property; in feet or meters) <br/>
#   v = Kinematic viscosity (in feet^2/second or meter^2/second)  <br/>
# 
# <br/>
# Notes: <br/>
# Swamee and Jain, A. K., 1976. Explicit equations for pipe-flow problems.  <br/>
# ASCE J. of Hyd. Div., 102(HY5) pp. 657-664 <br/><br/>
# 
# </p>
# 
# <form method ="POST"
#       action = "http://54.243.252.9/cgi-bin/pipehydraulics/QGivenHeadLoss/QGivenHeadLoss.py">
# 
# 
# Enter Value for Diameter (D in feet or meters) : <br/>
# <input type = "text" name = "diameter"><br/>
#     
# Enter Value for Gravitational acceleration (g in feet/s^2 or meters/s^2) : <br/>
# <input type = "text" name = "gravity"><br/>
#         
# Enter Value for Head loss (hl in feet or meters) : <br/>
# <input type = "text" name = "headloss"><br/>
#                         
# Enter Value for Pipe Length (L in feet or meters) : <br/>
# <input type = "text" name = "length"><br/>
#     
# Enter Value for Roughness height (ks in feet or meters): <br/>
# <input type = "text" name = "roughness"><br/>
#     
# Enter Value for Kinematic viscosity (v in feet^2/second or meter^2/second): <br/>
# <input type = "text" name = "kinematic"><br/>
# 
# <input type = "submit">
# </form>
# </body>
# </html>
# ```
# :::

# :::{note}
# The server-side code that performs the functions of computation and output formatting is listed below. On an apache web server the code would go in cgi-bin, or another directory where you allow execution to occur. On my server this code is located in `/usr/lib/cgi-bin/path-to-script/`
# 
# ```
# #!/usr/bin/python
# # QGivenHeadLoss.py
# # Computes Discharge given HeadLoss
# # Use HMTL POST method
# # Use PYTHON language
# 
# 
# # Import modules for CGI handling
# import cgi, cgitb , time
# # Import log function
# from math import sqrt,log
# 
# 
# # Create instance of FieldStorage
# form = cgi.FieldStorage()
# 
# # Get inputs from fields
# diameter = float(form.getvalue('diameter'))
# gravity = float(form.getvalue('gravity'))
# headloss = float(form.getvalue('headloss'))
# length = float(form.getvalue('length'))
# roughness = float(form.getvalue('roughness'))
# kinematic = float(form.getvalue('kinematic'))
# 
# 
# # Perform arithmetic (assembly language style -- equation a bit too complex)
# temp0 = sqrt( gravity*diameter*headloss/length )
# temp1 = roughness/(3.7*diameter)
# temp2 = 1.784*kinematic
# temp3 = diameter*temp0
# temp4 = temp1 + temp2/temp3
# temp5 = -0.965*diameter**2.0
# discharge = temp5 * temp0 * log( temp4 )
# 
# # Prepare the output HTML
# now = time.strftime("%c")
# 
# print "Content-type:text/html\r\n\r\n"
# # should have two returns and line feeds
# print "<html>"
# print "<head>"
# print "<title>Discharge given Head Loss  using Jain (1976) using Python</title>"
# print "</head>"
# print "<body>"
# print "Discharge given Head Loss using Jain (1976) using Python <br/><br/> "
# print "Host Name : 54.243.252.9 (AWS East) <br/>"
# print "Run Date : " , now ," <br/> "
# print "------ INPUT VALUES ------ <br/> "
# print "-- USE CONSISTENT UNITS -- <br/> "
# print "   Diameter = ", diameter ," [L] <br/> "
# print "          g = ", gravity ," [L]/[T]^2  <br/> "
# print "  Head Loss = ", headloss ," [L] <br/> "
# print "  Pipe Length = ", length ," [L] <br/> "
# print "  Roughness   = ", roughness ," [L] <br/> "
# print "  Kinematic Viscosity = ", kinematic ," [L]^2/[T] <br/> "
# print "------ COMPUTED DISCHARGE ----- <br/> "
# print " Roughness Ratio = ",roughness/diameter, " <br/> "
# # begin debug -- comment out when working OK
# #print " temp0 ",temp0, " <br/> "
# #print " temp1 ",temp1, " <br/> "
# #print " temp2 ",temp2, " <br/> "
# #print " temp3 ",temp3, " <br/> "
# #print " temp4 ",temp4, " <br/> "
# #print " temp5 ",temp5, " <br/> "
# # end debugging
# print "     Discharge = ", discharge, " [L]^3/[T] <br/>"
# print "</body>"
# print "</html>"
# 
# # end of script
# ```
# :::

# ## Computing Diameter from Specified Discharge
# 
# A rearrangement of the previous model can provide a way to estimate diameter to convey a particular discharge.
# 
# $
# D=0.66[ k_s^{1.25}(\frac{LQ^2}{g h_f})^{4.75}+\nu Q^{9.4} (\frac{L}{g h_f})^{5.2}]^{0.04} 
# $
# 
# applying the same Computational Thinking principles, a similar tool can be built for frequent use, pretty much reusing the same scripts but a different computation engine to solve for diameter.  The scripting is left as an exercise.  
# 
# A web-based version is located at [http://54.243.252.9/toolbox/pipehydraulics/DiameterGivenDischarge/DGivenQ.html](http://54.243.252.9/toolbox/pipehydraulics/DiameterGivenDischarge/DGivenQ.html)

# ## Readings
# 
# 1. Gupta, R. S. 2017. Hydrology and Hydraulic Systems. Waveland Press, Inc. pp 1-19 [http://54.243.252.9/ce-3372-webroot/3-Readings/WaterDemand-Gupta.pdf](http://54.243.252.9/ce-3372-webroot/3-Readings/WaterDemand-Gupta.pdf)
# 
# 2. Nickerson G. 2008. "Water Distribution Systems" in Land Development Handbook, Ed. S.O. Dewberry, Dewberry Inc., McGraw-Hill [http://54.243.252.9/ce-3372-webroot/3-Readings/water-distribution.pdf](http://54.243.252.9/ce-3372-webroot/3-Readings/water-distribution.pdf)