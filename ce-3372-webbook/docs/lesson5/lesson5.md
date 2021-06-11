## CE 3372 Water Systems Design
### Lesson 5. Pipeline Head Loss Models

Water moves from higher to lower energy

- Path of least resistance
- Head is energy per unit weight of a fluid 
- Pumps are used to add energy to move water to a higher elevation or over a barrier 

- Gravity flow: Change in elevation provides the required energy 
- Pressure flow: Change in pressure provides the required energy 

Flowing water encounters friction/resistance; hence there is loss of energy along a flow path. 
The mean section velocity is related to cross sectional flow area and volumetric discharge as:

$$ \bar{V} = \frac{Q}{A} $$

#### Continunity at Different Sections

#### Continunity at Junctions

#### Energy Equation


#### Example: Time to Drain a Storage Tank


```python

```

#### Example: Steady Discharge between Two Reservoirs


```python

```

### Head Loss Models (for losses in closed conduits)

### Darcy-Weisbach

#### Reynolds' "$Re_d$" Number

#### Darcy-Weisbach "$f$" Factor


```python

```

### Hazen-Williams

#### Hazen-Williams "C" Factor

#### Hydraulic Radius




```python

```

### Chezy-Mannings

#### Mannings "n" 

#### Hydraulic Radius




```python

```

### Fitting (Minor) Losses

---
---
## Computing Discharge from Specified Head Loss

### Computational Thinking/Data Science Approach (ENGR 1330)

CT/DS Approach

* State the programming problem
* Known (Inputs)
* Unknown (Outputs)
* Governing Equation(s)
* Test the tool

#### State the programming problem

Build a tool that takes inputs for the Jain equation and produces an estimate of discharge

Build an interface (notebook) that accepts the inputs, calls the function, and returns the computed discharge

#### Known (Inputs)
Engineer will specify: 

* Diameter, D; 
* Length of pipe, L; 
* Roughness height, e; 
* Viscosity, $\nu$; 
* Gravitational acceleration constant, g;
* Head loss

#### Unknown (Outputs)
The tool will compute and report Discharge, Q.

#### Governing Equation(s)
A compact form of the equation to be evaluated is
\begin{equation}
Q=-0.965 D^2 \sqrt{\frac{gDh_f}{L}}ln( \frac{k_s}{3.7D}+\frac{1.78\nu}{D\sqrt{\frac{gDh_f}{L}}} )
\end{equation}
####  Test the tool


```python
#computation engine
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
```


```python
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
```

    Enter Pipe Diameter 
     1
    Enter Pipe Length 
     1000
    Enter Pipe Roughness Height 
     0.0026
    Enter liquid viscosity 
     5e-5
    Enter gravitational acceleration constant (unit system appropriate) 
     32
    Enter head loss 
     40



```python
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
```

    Pipe Diameter :  1.0
    Pipe Length :  1000.0
    Pipe Roughness Height :  0.0026
    Liquid Viscosity :  5e-05
    Gravitational acceleration constant :  32.0
    Head loss :  40.0
    Discharge :  7.8110495900862835


#### Refine the Tool for Generalization

The refinement step would wrap the three parts above into a single function/notebook for simple use/reuse. If we save all three parts to a single file, we can access the script as we wish (using a JupyterLab magic function trick below.  The run command is obvious, but the -i means run interactive, and we supply the script name) 


```python
%run -i getQfromH.py
```

    Enter Pipe Diameter 
     1
    Enter Pipe Length 
     1000
    Enter Pipe Roughness Height 
     0.0026
    Enter liquid viscosity 
     5e-5
    Enter gravitational acceleration constant (unit system appropriate) 
     32
    Enter head loss 
     40


    Pipe Diameter :  1.0
    Pipe Length :  1000.0
    Pipe Roughness Height :  0.0026
    Liquid Viscosity :  5e-05
    Gravitational acceleration constant :  32.0
    Head loss :  40.0
    Discharge :  7.8110495900862835


Lastly, we can put the script onto a server and access via a web interface.


```python

```
