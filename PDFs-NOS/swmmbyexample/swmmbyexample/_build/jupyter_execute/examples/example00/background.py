#!/usr/bin/env python
# coding: utf-8

# # Background
# 
# Connecting to a remote desktop is usually simple, in this example there is one step where you get a security warning that you have to ignore (actually you are setting a session exception).  The warning is a consequence of the server certificate which is self-signed, hence not linked to any accepted certificate authority.
# 
# Once the connection is made, a simple SWMM model is constructed and run.  
# 
# :::{note}
# The goal is to show how to access the shared environment, and not so much how to use SWMM; that task is for subsequent examples.
# :::
# 
