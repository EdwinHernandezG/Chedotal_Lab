#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:00:47 2022

@author: Edwin_Hernandez-Garzon

"""

#%%
# Call dependencies

import os
import zarr
import tifffile as tf


#%%
# Folder location

Data_folder = '/media/alain/DataWS6/EHG/Explants/Output COUPTFII/Want/results/Trackmate'


#%%

#%%
# File Indexation
c=1

for filename in os.listdir(Data_folder):
    if filename.endswith(".tif"):
        im = tf.imread(filename)
        name= filename+str(c)+'.zarr'
        zarr.convenience.save(name, im)
        c+=1
        print(os.path.join(Data_folder, filename))
        continue
    else:
        continue
