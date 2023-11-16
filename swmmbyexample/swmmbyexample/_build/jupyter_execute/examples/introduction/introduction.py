#!/usr/bin/env python
# coding: utf-8

# # SWMM by Example
# 
# [EPA Storm Water Management Model (SWMM)](https://www.epa.gov/water-research/storm-water-management-model-swmm) is a computer program that performs hydraulics computations in open conduit and pressure-pipe systems.  It contains rudimentary but useable hydrology components, and some water quality capabilities (Green Infrastructure components and elementary pollutant fate and transport). 
# 
# This JupyterBook is a collection of worked examples (with links to supporting files) for various situations intended as a self-training tool.

# ## Installing SWMM
# 
# A YouTube Video entitled [InstallingSWMM](https://www.youtube.com/watch?v=JKedXZUc8vA&t=10s) shows how to download
# and install EPA-SWMM onto your computer. EPA-SWMM will run fine on a laptop computer, and even a Macintosh that has a guest Windows OS ([VMWare](https://www.vmware.com/products/fusion.html), [Parallels](https://www.parallels.com/pd/general/?gclid=CjwKCAjw79iaBhAJEiwAPYwoCFORJ8sEPl3m0sP2EEj6TExbC4rKqt6LUsS22AVAmTK8PkgnfLqbkxoC_dcQAvD_BwE), [CrossOver](https://www.codeweavers.com/) or [BootCamp](https://support.apple.com/en-us/HT201468))
# 
# ## SWMM On-Line Share Version
# 
# A fully provisioned Windows Implementation of SWMM 5.2.1 is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **SWMM-OnLine**
# - passwd: **peakfq73$hare**
# 
# Users must access using [Remote Desktop Protocol](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac) (Built into Windows, Apple Store has a free Mac application).
# 
# :::{note}
# All the examples in this JupyterBook are created and run in the shared environment.  Input files are stored separately in the JupyterBook root and are accessible independently of the JupyterBook.
# :::
# 
# :::{warning}
# The password is not supposed to be changeable, but if it is changed the author may not get around to resetting it back to original state for quite awhile, so for collective sake, please stay out of the control panel.  Similarily the example input files are stored in a GitHub repository so a pull before exploring the environment is a good practice to reset to original state.  
# :::

# ## References
# 
# 1. SWMM User Manual
# 2. SWMM Tutorial
# 3. OWA SWMM project
# 4. JupyterBook
# 5. GitHub 

# In[ ]:




