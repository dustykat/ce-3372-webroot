# getQfromH.py
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

# interface engine
# Get pipe diameter, use a simple error trap
yes=0
while yes == 0:
    xnow = input("Enter Pipe Diameter \n")
    try:
        pipe_diameter = float(xnow)
        yes =1
    except:
        print ("Value should be numeric, try again \n")
# Get pipe length, use a simple error trap
yes=0
while yes == 0:
    xnow = input("Enter Pipe Length \n")
    try:
        pipe_length = float(xnow)
        yes =1
    except:
        print ("Value should be numeric, try again \n")
# Get roughness, use a simple error trap
yes=0
while yes == 0:
    xnow = input("Enter Pipe Roughness Height \n")
    try:
        roughness = float(xnow)
        yes =1
    except:
        print ("Value should be numeric, try again \n")
# Get viscosity, use a simple error trap
yes=0
while yes == 0:
    xnow = input("Enter liquid viscosity \n")
    try:
        viscosity = float(xnow)
        yes =1
    except:
        print ("Value should be numeric, try again \n")
# Get grabity, use a simple error trap
yes=0
while yes == 0:
    xnow = input("Enter gravitational acceleration constant (unit system appropriate) \n")
    try:
        grabity = float(xnow)
        yes =1
    except:
        print ("Value should be numeric, try again \n")
# Get head loss, use a simple error trap
yes=0
while yes == 0:
    xnow = input("Enter head loss \n")
    try:
        head_loss = float(xnow)
        yes =1
    except:
        print ("Value should be numeric, try again \n")
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
