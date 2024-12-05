#!/usr/bin/env python
# coding: utf-8

# # 1. Introduction
# 
# :::{admonition} Course Website
# [http://54.243.252.9/ce-3372-webroot/](http://54.243.252.9/ce-3372-webroot/)
# :::

# ## Readings 
# 
# 1. [Introduction to Water Resources Engineering Pages 1-33 from Wurbs,R.A., and James, W.P. (2002) Water Resources Engineering, Prentice Hall.](http://54.243.252.9/ce-3372-webroot/3-Readings/Wurbs1-33/Wurbs1-33.pdf)
# 
# 2. [Introduction to Water Resources Engineeirng Pages 1-11 from Mays, L.W. (2011) Water Resources Engineering, J. Wiley and Sons.](http://54.243.252.9/ce-3372-webroot/3-Readings/Mays1-11/Mays1-11.pdf)
# 
# 3. [Introduction to Water Resources Engineering Pages 1-8 from Chin, D. A. (2006) Water-Resources Engineering, Pearson-Prentice Hall.](http://54.243.252.9/ce-3372-webroot/3-Readings/Chin1-8/Chin1-8.pdf)

# ## Videos
# 
# 1. [none](https://www.youtube.com/watch?v=9NYs3Y-IjGw)

# ## Lesson Outline
# 1. Course Overview
# 2. Types of Water Systems
# 3. Photo Essay
# 4. Software

# 
# ## Overview
# The title of the course is water systems design.  The catalog description is: 
# > CE 3372.  Water Systems Design (3:3:0).Prerequesite: CE 33051, 33542.Hydraulic analysis and design of municipal water distribution, stormwater collection, and wastewater collection systems.  Oral and written presentations.  (Writing Intensive)
# 
# The general scope of the course is:
# 
# - Examination of design guidance documents for drinking water distribution systems, a review of pipeline hydraulics, demand estimation, then a design project related to a drinking water distribution system. 
# - The computer program EPANET is presented to provide a tool for the hydraulic modeling component of drinking water system design.
# - Examination of design guidance for stormwater collection systems, presents a review of open channel hydraulics (as related to storm sewers),  capacity (hydrology)  estimation,  then  a  design  project  related  to  a  stormwater  collection system.
# - The computer program SWMM 5 is presented to provide a tool for the hydrologic/hydraulic modeling component of the stormwater collection system design.
# - Examination of design guidance for wastewater collection systems, then  a  design  project  related  to  a  stormwater  collection system.
# 
# The graded components of the course are:
# 
# - Quizzes (administered on a learning management system); individual activity
# - Exercises (collected on a learning management system); group activity
# - Exams (administered on a learning management system); individual activity
# - A design  report  (Three parts; collected  on  a  learning  management  system);  group activity
# - A design  presentation  (administered  on  a  learning  management  system);  group activity

# ---
# 
# ## Water Systems Definition(s)
# The course title is Water Systems Design, so a natural question is what is meant by a water system?  In this course it refers to a water distribution system that conveys raw or treated water to customers, a storm water collection system that conveys storm water away from infrastructure to reduce flooding damages and activities of daily life inconvenience,and wastewater collection systems that convey wastewater to treatment facilities for eventual release of the water back into the environment (or intentional reuse).
# 
# Water systems can be classified into three main categories (Chin, 2006; Mays, 2011):
# 
# 1.  Water-control  systems  –  to  control  the  spatial  and  temporal  distribution  ofsurface runoff from rainfall events (drainage engineering).  They can also servea use role if the captured rainwater is used later on for water supply (rainwaterharvesting).
# 2.  Water-use system – to support human habitation and include water-treatmentsystems, water-distribution systems, wastewater-collection systems, and wastewater-treatment systems.
# 3.  Environmental restoration system – to manage spatial and temporal distributionof water (quality and quantity) in support of non-human habitation.

# ---
# 
# ### Water Control Systems
# Spatial and temporal distribution of surface runoff from rainfall events (drainage engineering)
# 
# - Flood control 
# - Storm water harvesting 
# - Capacity is based on AREA served 
# - Hydrologicaly dominated designs 
# 
# ---
# 
# ### Water Use Systems
# Spatial and temporal distribution in support of human habitation 
# 
# - Water supply/treatment/distribution 
# - Waste water collection/treatment/discharge 
# - Capacity is based on POPULATION served 
# - Hydraulically dominated designs 
# 
# ---
# 
# ### Environmental Restoration Systems
# Systems to manage spatial and temporal distribution in support of non-human habitation 
# 
# - Create “desirable” conditions 
# - “Desirable” <= Policy <= Value Judgment
# 

# --- 
# 
# ### Water System Photo Essay
# This brief photo essay is adapted from  
# > “Historical Urban Water Systems” by Dr. Robert Pitt, Department of Civil and Environmental Engineering, University of Alabama, Tuscaloosa, AL  35487  [http://54.243.252.9/ce-3372-webroot/3-Readings/water-system-photo-tour/water-system-photo-tour.pdf](http://54.243.252.9/ce-3372-webroot/3-Readings/water-system-photo-tour/water-system-photo-tour.pdf)
# 
# As we proceed through the tour, using the general definitions above, decide whether the picture represents a water control, water use, or environmental restoration system.  

# --- 
# ## Course Specific Software
# 
# In this course we will use **EPANET** pipe network simulator software with the EPA supplied GUI, and **SWMM 5+** drainage network simulator software with the EPA supplied GUI.
# 
# The remainder of the lesson demonstrates the installation of these tools: 

# ---
# ### Installing EPANET
# 
# EPANET as supplied by [https://www.epa.gov/water-research/epanet](https://www.epa.gov/water-research/epanet) also includes a graphical user interface (GUI) that will allow one to quickly build network simulation models, run them, and present results.  The GUI runs on Windows machines using Intel/AMD hardware.  It can be made to run on other operating systems and architectures, but not easily.
# 
# Follow the guidelines on the [https://www.epa.gov/water-research/epanet](https://www.epa.gov/water-research/epanet) or watch [https://www.youtube.com/watch?v=HoZC4FPBQzI](https://www.youtube.com/watch?v=HoZC4FPBQzI)
# 
# You can also examine [https://epanet22.readthedocs.io/en/latest/2_quickstart.html](https://epanet22.readthedocs.io/en/latest/2_quickstart.html)
# 
# EPANET with the GUI runs in the Windows environment and expects the underlying machine to be an x86-64 chipset.  Generally this means an Intel or AMD-based machine.  
# 
# If you have a Chromebook or Raspberry Pi, or Macintosh EPANET as deployed from the EPA won't install directly.  You can try WINE or other emulators but **YOU ARE ON YOUR OWN!**. 
# 
# An alternative is an Amazon Web Services (AWS) Lightsail instance.  The \$12/month service will run both softwares, and works like ordinary Windows. 

# --- 
# ### Installing SWMM
# 
# #### Check your system
# 
# SWMM with the GUI runs in the Windows environment and expects the underlying machine to be an x86-64 chipset.  Generally this means an Intel- or AMD-based machine.  
# 
# If you have a Chromebook or Raspberry Pi, or Macintosh SWMM as deployed from the EPA won't install directly.  You can try WINE or other emulators but **YOU ARE ON YOUR OWN!**. 
# 
# An alternative for these cases is an Amazon Web Services (AWS) Lightsail instance.  The \$12/month service will run both softwares, and works like ordinary Windows. 

# ---
# 
# #### Download the installer
# 
# URL to installer 
# 
# Screen capture download
# 

# ---
# 
# #### Run the installer
# 
# Screen capture running the installer

# ---
# 
# #### Check the install
# 
# To check the install, simply launch the program. If the GUI opens and renders the program is working.  You can try a simple example if you wish.
# 
# Screen capture check
# 
# URL to SWMM by Example,  load example 1

# ---
# 
# ## Readings
# 

# In[ ]:




