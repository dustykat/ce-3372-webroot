#!/usr/bin/env python
# coding: utf-8

# # Lesson 4. Pipeline Head Loss 
# 
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
# #### Reynolds' "$Re_d$" Number
# 
# #### Darcy-Weisbach "$f$" Factor

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
# ####  Test the tool
# 
# To build and test the tool, cut and paste the code in the next few cells into a Jupyter Notebook and run the cells, you should get output like:
# 
# Screen Capture Here

# ```
# # Computation engine
# # import built in functions for log, sqrt
# from math import log,sqrt
# # Define the prototype function
# def jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss):
#     egl_slope = head_loss/pipe_length
#     t1 = sqrt(grabity*pipe_diameter*egl_slope)
#     t2 = roughness/(3.7*pipe_diameter)
#     t3 = 1.78*viscosity
#     jainQ = (-0.965*pipe_diameter**2)*t1*log(t2 + t3/(pipe_diameter*t1))
#     return jainQ
#     
# # Interface engine
# # Get pipe diameter, use a simple error trap
# yes=0
# while yes == 0:
#     xnow = input("Enter Pipe Diameter \n")
#     try:
#         pipe_diameter = float(xnow)
#         yes =1
#     except:
#         print ("Value should be numeric, try again \n")
# # Get pipe length, use a simple error trap
# yes=0
# while yes == 0:
#     xnow = input("Enter Pipe Length \n")
#     try:
#         pipe_length = float(xnow)
#         yes =1
#     except:
#         print ("Value should be numeric, try again \n")
# # Get roughness, use a simple error trap
# yes=0
# while yes == 0:
#     xnow = input("Enter Pipe Roughness Height \n")
#     try:
#         roughness = float(xnow)
#         yes =1
#     except:
#         print ("Value should be numeric, try again \n")
# # Get viscosity, use a simple error trap
# yes=0
# while yes == 0:
#     xnow = input("Enter liquid viscosity \n")
#     try:
#         viscosity = float(xnow)
#         yes =1
#     except:
#         print ("Value should be numeric, try again \n")
# # Get grabity, use a simple error trap
# yes=0
# while yes == 0:
#     xnow = input("Enter gravitational acceleration constant (unit system appropriate) \n")
#     try:
#         grabity = float(xnow)
#         yes =1
#     except:
#         print ("Value should be numeric, try again \n")
# # Get head loss, use a simple error trap
# yes=0
# while yes == 0:
#     xnow = input("Enter head loss \n")
#     try:
#         head_loss = float(xnow)
#         yes =1
#     except:
#         print ("Value should be numeric, try again \n")
#         
# # Now perform computation and construct output
# discharge = jainQ(pipe_diameter,pipe_length,roughness,viscosity,grabity,head_loss)
# # Echo inputs, and outputs
# print ("Pipe Diameter : ", pipe_diameter)
# print ("Pipe Length : ", pipe_length)
# print ("Pipe Roughness Height : ", roughness)
# print ("Liquid Viscosity : ", viscosity)
# print ("Gravitational acceleration constant : ",grabity) 
# print ("Head loss : ",head_loss)
# print ("Discharge : ",discharge)
# ```

# #### Refine the Tool for Generalization
# 
# The refinement step would wrap the above script into a single function/notebook for simple use/reuse. If we save to a single file, we can access the script as we wish (using a JupyterLab magic function).  

# Lastly, we can put the script onto a server and access via a web interface.

# ## Readings
# 
# 1. Gupta, R. S. 2017. Hydrology and Hydraulic Systems. Waveland Press, Inc. pp 1-19 [http://54.243.252.9/ce-3372-webroot/3-Readings/WaterDemand-Gupta.pdf](http://54.243.252.9/ce-3372-webroot/3-Readings/WaterDemand-Gupta.pdf)
# 
# 2. Nickerson G. 2008. "Water Distribution Systems" in Land Development Handbook, Ed. S.O. Dewberry, Dewberry Inc., McGraw-Hill [http://54.243.252.9/ce-3372-webroot/3-Readings/water-distribution.pdf](http://54.243.252.9/ce-3372-webroot/3-Readings/water-distribution.pdf)
