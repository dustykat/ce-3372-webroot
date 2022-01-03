#!/usr/bin/env python
# coding: utf-8

# # Pumping Systems
# 
# Water moves from higher to lower energy
# - Path of least resistance
# - Head is energy per unit weight of a fluid 
# - Pumps are used to add energy to move water to a higher elevation, or over a barrier, or to increase system pressure. 
# 

# ## Background
#  
# A pump is a mechanical device that transfers energy into a liquid; used to 
# 
# - Lift from lower to higher elevation (Lift stations)
# - Increase pressure (Booster stations)
# 
# ![](pumpone.png)
# 
# The gas phase equivalent is a Compressor 

# Pumps range substantially in size depending on application
# 
# - Small <br>
# ![](pumplittle.png)
# - Big <br>
# ![](pumpbig.png)

# ## Types
# 
# ### Positive (Fixed) Displacement Pumps 
# - Fixed volume of fluid is displaced each cycle regardless of 
# system static head/pressure 
# - Lower flow rates and higher head than non-positive pumps 
# 
# ### Variable Displacement Pumps  
# - Varying volume of fluid is displaced dependent on system static 
# head/pressure (back pressure) 
# 
# ### Examples of Fixed Displacement Pumps 
# - Screw Pumps 
# - Progressive Cavity Pumps 
# - Reciprocating Pumps 
# 
# ### Images of Positive Displacement Pumps
# - Screw Pumps ![](screwpump.png) 
# - Progressive Cavity Pumps ![](cavitypump.png)
# - Reciprocating Pumps ![](pistonpump.png)
# 
# 
# ### Examples of Variable Displacement Pumps 
# - Centrifugal (Radial-Flow) Pumps 
# - Propeller Pumps (Axial-Flow) 
# - Jet Pumps (Mixed-Flow) 
# 
# ![](pumpclassification.png)
# 
# ### Images of Variable Displacement Pumps 
# - Centrifugal (Radial-Flow) Pumps ![](centifrugalpump.png)
# - Propeller Pumps (Axial-Flow) ![](axialfrowpump.png)
# 
# :::{note}
# A couple of explainatory videos are listed below.
# 
# - [Explaination of Centrifugal Pump](https://www.youtube.com/watch?v=BaEHVpKc-1Q)
# - [Lab-Scale model of a flexible impeller pump(Variable-Cavity;Positive Displacement)](https://www.youtube.com/watch?feature=player_detailpage&v=ECv1VwW6RTo#t=122)
# 
# :::

# ## Pump Selection
# 
# A primary design activity is selecting or sizing a pump for a specific application.  The protocol is:
# 
# - Design conditions are specified by system hydraulics (i.e. energy equation at desired flow rate)
# - Pump is selected from manufacturer catalogs that appears to meet nominal conditions
# - A hydraulic system curve (Head vs Discharge) is prepared
# - The system curve (or equation) is plotted onto the pump curve (manufacturer supplied)
# - The matching point where the two curves intersect is the anticipated operating point
# 
# A few secondary checks are:
# - Is there some head range remaining? 
# - Flow range remaining?  
# - Is pump efficiency close to optimal for the particular pump?
# - Is Net Positive Suction Head Available (NPSHa) large enough for the particular pump at the operating point (and start-up)?
# 
# ### System Curve
# 
# A system (characteristic) curve is a plot of required head versus flow rate in a hydraulic system.  
# The curve depicts how much energy is needed to maintain a steady flow under the supplied conditions.
# 
# The curve is constructed at the pump location and relates the required added head (at a particular flowrate) needed to be supplied by some pump. 
# 
# $$ H_p(Q) = h_{elev} + h_{loss}(Q)$$
# 
# For example if the system schematic is
# 
# ![](system-schematic.png)
# 
# An equation of required head and discharge is
# 
# ![](system-equation.png)
# 
# The equation tells us that the added head has to be at least 30 meters just to keep the reservoirs at the two levels shown, if any flow is to occur the pump must supply more than 30 meters of head at a prescribed flow rate.  The zero flow head value is called the shutoff head.  The equation plots as the figure below
# 
# ![](system-curve.png)

# ### Pump Curve(s)
# 
# Pump curves are supplied by the manufacturer and convey performance of a specific pump. 
# Information ususally includes:
# - Discharge (Q) on the x-axis
# - Head ($H_p$) on the left y-axis
# - Pump power input on the right y-axis
# - Pump efficiency (wire-to-water) as a percentage
# - The speed of the pump (RPM)
# - The required Net Positive Suction Head ($NPSH_r$)
# 
# #### An example pump curve is shown below
# 
# ![](pump-curve.png)
# 
# #### Another example curve for a different pump
# 
# ![](pump-curve-two.png)

# ### Comparing Different Pumps
# 
# ![](pumpA-B.png)
# 
# ### Multiple Pumps
# 
# Various multi-pump combinations can be employed to meet hydraulic needs - a lot of flexibility can be achieved with a few pumps and ingenious plumbing.
# 
# ![](multi-pumps-one.png)
# 
# #### Parallel Pumps
# 
# Parallel pumps add discharge for a given working head.
# 
# ![](parallelpumps.png)
# 
# #### Series Pumps 
# 
# Series pumps add head for a given discharge.
# 
# ![](seriespumps.png)
# 

# ### Suction Requirements
# 
# The most common cause of pumping system failure is poor suction conditions.
# 
# Cavitation occurs when liquid pressure is reduced to the vapor pressure of the liquid, then the liquid flashes to make small gas bubbles, which are unstable and collapse back into liquid - this rapid localized phase change process imparts large destructive energy into the pump impeller and housing and quickly destroys the pump itself in addition to creating loss of priming.
# 
# In a pipe system with a pump, cavitation will occur when the absolute pressure at the inlet (eye) falls below the vapor pressure of the water.
# 
# :::{note}
# The pump destruction described is not usually instant, but does happen pretty fast.  For example weeks to failure when the designer expects years between overhauls.  
# 
# High speed turbopumps  can fail in seconds when they are supposed to run for minutes.  Cavitation is a big deal in things like rocket ships, nuclear power plants (cooling system), and other high-risk applications; less so in Civil Engineering, usually our failures just cost time and money - a lift station failure during a flood could cause death, so we are not risk-free
# :::
# 
# Considerations 
# - Liquid must enter the pump eye under some pressure; this pressure is dictated by the hydraulic system and is called the Available Net Positive Suction Head $NPSH_a$.
# - A centrifugal pump cannot lift water unless it is primed; the first stage impellers must be below the static HGL in the suction pit at startup.
# - The manufacturer supplies a value for the minimum pressure the pump needs to operate; this pressure is called the Required Net Positive Suction Head $NPSH_r$
# - Proper pump operation without cavitation demands that $$ NPSH_r < NPSH_a $$
# - Can calculate $NPSH_a$ from
# 
# ![](npsha-formula.png)
# 
# - An on-line calculator is located at [http://54.243.252.9/toolbox/pipehydraulics/NPSHCalculatorUS/NPSHCalculatorUS.html](http://54.243.252.9/toolbox/pipehydraulics/NPSHCalculatorUS/NPSHCalculatorUS.html) ; the calculator is specific for US Customary Units, but would easily be adaptabe for SI units. The interface looks like
# 
# ![](npsha-calc.png)
# 
# 

# #### NPSHa Example
# 
# #### Problem Statement
# 
# ![](NPSA-ex1.png)
# 
# #### Solution (part 1)
# 
# ![](NPSA-ex2.png)
# 
# #### Solution (part 2)
# 
# ![](NPSA-ex3.png)
# 
# #### Solution (part 3)
# 
# ![](NPSA-ex4.png)
# 
# #### Solution (part 4)
# 
# ![](NPSA-ex5.png)
# 
# We look up the liquid properties at [http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html](http://54.243.252.9/toolbox/fluidmechanics/WaterPropertiesUS/WaterPropertiesUS.html)
# 
# #### Solution (part 5)
# Now insert these intermediate values into the equation for $NPSH_a$ paying close attention to how the equation is written in the calculator (the $H_{static}$ sign is changed in the calculator in comparison to the equation presented above, the remaining terms are unchanged.
# 
# ![](NPSA-soln.png)
# 
# #### Solution Summary
# 
# ![](NPSA-soln2.png)

# ## Summary
# 
# That's our quick overview of pumps as relevant for water systems.  Key points are:
# - Need a system curve (we can get it out of EPANET for complicated layouts)
# - Need some pump curves (internet, vendor websites)
# - Find operating point
# - Judge if there is some excess head and/or flow available (this would be desirable)
# - Judge if close to best possible efficiency for the pump (can vary a little, but it would be dumb to operate a piss-po efficiency)
# - Check suction conditions at startup and operation
# - If all good, then have a pump
# - Remember can run multiple pumps if a single pump is not available (really big pumps can be custom built, but we usually want to use off-the-shelf pumps)

# ## References
# 
# 1. Gupta, R. S. 2017. Hydrology and Hydraulic Systems. Waveland Press, Inc. pp xx-xx
# 2. Pump Selection ; Walker, R. (1973) Pump Selection. Ann Arbor Science pp. 3-9 [http://54.243.252.9/ce-3372-webroot/3-Readings/PumpSelection/](http://54.243.252.9/ce-3372-webroot/3-Readings/PumpSelection/)
# 
# 3. Pump Suction Conditions; Walker, R. (1973) Pump Selection. An Arbor Science pp. 11-31 [http://54.243.252.9/ce-3372-webroot/3-Readings/PumpSuctionConditions/](http://54.243.252.9/ce-3372-webroot/3-Readings/PumpSuctionConditions/)
# 
# 4. Hauser, B. A. (1991). Practical Hydraulics Handbook. Lewis Publishers, Michigan. pp. 296-299
# [http://54.243.252.9/ce-3372-webroot/3-Readings/NPSHExplain/](http://54.243.252.9/ce-3372-webroot/3-Readings/NPSHExplain/)
# 
# 5. City of Houston; List Station Design Guidelines [http://54.243.252.9/ce-3372-webroot/3-Readings/LiftStationCityofHouston/](http://54.243.252.9/ce-3372-webroot/3-Readings/LiftStationCityofHouston/)
# 
# 6. Highway Stormwater Pump Station Design. FHWA-NHI-01-007. [http://54.243.252.9/ce-3372-webroot/3-Readings/LiftStationDesign/](http://54.243.252.9/ce-3372-webroot/3-Readings/LiftStationDesign/)
# 

# In[ ]:




