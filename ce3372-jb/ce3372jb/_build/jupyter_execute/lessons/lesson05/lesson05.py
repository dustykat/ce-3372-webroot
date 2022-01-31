#!/usr/bin/env python
# coding: utf-8

# # Pipeline Hydraulics
# 
# ## Example: Steady Discharge between Reservoirs (using on-line tools)
# 
# Here we examine a relatively simple hydraulics question - what is the discharge in the pipe for the situation depicted
# 

# ## Problem Statement 
# 
# ![image.png](ex1-1.png)
# 
# ### Known Values
# 
# Use tables and references to find known values
# 
# - Roughness height:
# 
# ![image.png](ex1-2.png)
# 
# [Link to tool](http://54.243.252.9/toolbox/Databases/RoughnessHeight/RoughnessHeight.html)
# 
# - Millimeters to Feet
# 
# ![image.png](ex1-3.png)
# 
# [Link to tool](http://54.243.252.9/toolbox/ordinarytools/UnitsConverterTool/UnitsConverterTool.html)
# 
# - Water Properties
# 
# ![image.png](ex1-4.png)
# 
# [Link to tool](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html)
# 
# - Minor Loss Coefficients
# 
# ![image.png](ex1-5.png)
# 
# ### Consolidate Values for Data Input
# 
# ![image.png](ex1-6.png)
# 
# ### Apply Tool
# 
# ![image.png](ex1-7.png)
# 
# [Link to tool](http://54.243.252.9/toolbox/pipehydraulics/Q2Reservoir/Q2Reservoir.html)
# 
# 
# ### Or using our Jupyter Script
# 
# Our script below applied to the same inputs

# In[1]:


# modified from getQfromH.py
# ipython module for pipeline hydraulics
# computation engine #########################
# import built in functions for log, sqrt
from math import log,sqrt
# Define the prototype function
def jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss):
    egl_slope = head_loss/pipe_length
    t1 = sqrt(grabity*pipe_diameter*egl_slope)
    t2 = roughness/(3.7*pipe_diameter)
    t3 = 1.78*viscosity
    jainQ = (-0.965*pipe_diameter**2)*t1*log(t2 + t3/(pipe_diameter*t1))
    return jainQ
# values from Example
pipe_diameter = 2.0
pipe_length = 10680.0
roughness = 0.00328
viscosity = 1.41e-05
grabity = 32.2
head_loss = 20.0
# disable above and insert interface engine here
#
# now perform computation and construct output
discharge = jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss)
# Echo inputs, and outputs
print ("Pipe Diameter : ", pipe_diameter)
print ("Pipe Length : ", pipe_length)
print ("Pipe Roughness Height : ", roughness)
print ("Liquid Viscosity : ", viscosity)
print ("Gravitational acceleration constant : ",grabity) 
print ("Head loss : ",head_loss)
print ("Discharge : ",discharge)


# > Results are close, but not identical. Why? *The JupyterLab script did not include the minor loss terms*

# ## Linking Systems 
# 
# A hydraulic system can be analysed as a set of linked components to make an otherwise complicated system easier to analyze.
# 
# - Idea is to decompose into smaller (hydraulically) independent parts, analyze the parts then reassemble (integrate) the parts to answer questions about the whole system
# 
# ### Example: Rural Water Supply to a Village School
# 
# ![image.png](africa-system.png)
# 
# The figure is an aerial image of a pipeline system with preliminary engineering sketches of the system (lower left panel) and a detail sketch of the terminal small storage tank (upper right panel). The 3,200 meter long pipeline lifts 25C water ( $\rho= 997 kg/m^3$,$\nu= 8.94 E-7 m^2/s$) from a treatment plant on the downstream face of Gulameta Dam through a 127 millimeter high-density polyethylene (HDPE) pipe (ks =0.0015 mm) to a large diameter at-grade cylindrical storage tank. A secondary, 800 meter long pipeline carries water from the large diameter storage tank to a small, cylindrical (D = 1 meter), elevated storage tank at the village school. Both storage tanks have float valves to prevent overflow and maintain the indicated water pool elevations.
# 
# Analyze proposed system to determine anticipated behavior under various situations:
# 
# - Float valve fails at school
# - Outlet valve accidently left open
# - Pump operation under worst failure mode
# - Pump fails, time until system fails/drains
# - Float valve limited
# - Oultet valve limited

# **Float Valve at School Fails**
# 
# > Get dimensions
# 
# ![](africa-1.png)
# 
# > Get material properties, and loss coefficients
# 
# ![](africa-2.png)
# 
# > Apply On-Line Tool or JupyterLab script
# 
# ![](africa-3.png)
# 
# The JupyterLab script is shown below, but needs modification for the minor losses. Hence the two values are sort of close, but without all losses the JupyterLab script as shown overestimates the discharge. 

# In[2]:


# modified from getQfromH.py
# ipython module for pipeline hydraulics
# computation engine #########################
# import built in functions for log, sqrt
from math import log,sqrt
# Define the prototype function
def jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss):
    egl_slope = head_loss/pipe_length
    t1 = sqrt(grabity*pipe_diameter*egl_slope)
    t2 = roughness/(3.7*pipe_diameter)
    t3 = 1.78*viscosity
    jainQ = (-0.965*pipe_diameter**2)*t1*log(t2 + t3/(pipe_diameter*t1))
    return jainQ
# values from Example
pipe_diameter = 0.127
pipe_length = 800.0
roughness = 0.000007
viscosity = 1.0e-06
grabity = 9.8
head_loss = 14.3
# disable above and insert interface engine here
#
# now perform computation and construct output
discharge = jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss)
# Echo inputs, and outputs
print ("Pipe Diameter : ", pipe_diameter)
print ("Pipe Length : ", pipe_length)
print ("Pipe Roughness Height : ", roughness)
print ("Liquid Viscosity : ", viscosity)
print ("Gravitational acceleration constant : ",grabity) 
print ("Head loss : ",head_loss)
print ("Discharge : ",round(discharge*1000,3)," liters/sec")


# **School Outlet Valve Left Open**
# 
# Treat as a hole in the tank, assume supply side is unchanged and maintains downstream water level
# 
# ![](africa-44.png)
# 
# > JupyterLab script for hole in tank (future version this book)

# In[ ]:





# **Pump System Requirements**
# 
# > This portion of example moved to after pumps

# In[ ]:





# **Pump System Fails, Time to Drain**
# 
# > This portion of example moved to after pumps

# In[ ]:





# ## References
# 
# 1. Gupta, R. S. 2017. Hydrology and Hydraulic Systems (4-th Ed). Waveland Press, Inc. pp 633-661 
# 
# 2. Nickerson G. 2008. "Water Distribution Systems" in Land Development Handbook, Ed. S.O. Dewberry, Dewberry Inc., McGraw-Hill [http://54.243.252.9/ce-3372-webroot/3-Readings/WaterDistributionSystems/](http://54.243.252.9/ce-3372-webroot/3-Readings/WaterDistributionSystems/)
# 
# 3. Wurbs, R.A., and James, W. P. (2002) "Hydraulics of Pipelines and Pipe Networks" in *Water Resources Engineering, Prentice Hall; pp.130-156; and 156-198*.[http://54.243.252.9/ce-3372-webroot/3-Readings/Wurbs130-198/](http://54.243.252.9/ce-3372-webroot/3-Readings/Wurbs130-198/)
# 
# 3. Roberson, J.A., Cassidy, J.J., and Chaudry, M.H. (1988) Closed Conduits in "Hydraulic Engineering." Houghton Mifflin Co. pp. 240-310 [http://54.243.252.9/ce-3372-webroot/3-Readings/Chapter5/](http://54.243.252.9/ce-3372-webroot/3-Readings/Chapter5/)
# 
