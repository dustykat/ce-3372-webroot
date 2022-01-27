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
pipe_diameter = float(xnow)
pipe_length = float(xnow)
roughness = float(xnow)
viscosity = float(xnow)
grabity = float(xnow)
head_loss = float(xnow)
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
