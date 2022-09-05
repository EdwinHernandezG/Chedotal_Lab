#!/usr/bin/env python
# coding: utf-8

# In[2]:


from vedo import Mesh, Plotter
from skimage.morphology import skeletonize 
from skimage import data 
from skimage.morphology import medial_axis, skeletonize, skeletonize_3d
from scipy.ndimage import zoom
import tifffile as tf
import time 
import numpy as np 
import skan 
import napari
from skimage.util import map_array 

voxel = 0.01
#with script from https://forum.image.sc/t/create-2d-tiff-stack-from-3d-model/67419 

surf = Mesh('I:/SmoothedLaplacianMeshmixer.obj').normalize().wireframe()

vol = surf.binarize(spacing=(voxel,voxel,voxel))

### To visualize the isosurface ###

vol.alpha([0,0.6]).c('blue')
iso = vol.isosurface().color("blue5")

plt = Plotter(N=2, axes=9)
plt.at(0).show(vol, surf, __doc__)
plt.at(1).show("..the volume is isosurfaced:", iso)
plt.interactive().close()

vol.write("kidney.tif")
skel_input = tf.imread("kidney.tif")

##### Skeletonize and Visualize #####
#input variables 
res = voxel*1000 #from cm to microns

#skeletonize it 
binary_skeleton = skeletonize_3d(skel_input) 
skeleton = skan.Skeleton(binary_skeleton, spacing=res)
tf.imwrite('skeleton-skel-10um-test.tif', binary_skeleton)

all_paths = [
        skeleton.path_coordinates(i)
        for i in range(skeleton.n_paths)
        ]

paths_table = skan.summarize(skeleton)
paths_table['path-id'] = np.arange(skeleton.n_paths)
paths_table['random-path-id'] = np.random.default_rng().permutation(skeleton.n_paths)

#################   Visualization   #################
viewer = napari.Viewer(ndisplay=3)

#color coded by branch length (longer=yellow, shorter=purple)
skeleton_layer = viewer.add_shapes(
        all_paths,
        shape_type='path',
        properties= paths_table,
        edge_width= 1.0,
        edge_color='branch-distance',
        edge_colormap='viridis',
        face_color= 'branch-distance',
        face_colormap='viridis'
)

input_layer = viewer.add_image(skel_input, opacity = 0.2)


# In[3]:





# In[ ]:




