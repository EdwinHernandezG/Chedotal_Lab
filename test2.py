from skimage.io import imread
import napari_accelerated_pixel_and_object_classification  # version 0.12.3
import napari
if 'viewer' not in globals():
    viewer = napari.Viewer()

image0_C = imread(
    "F:/CI2A/Image Analysis/Aixa/Pilar/split/C1-Reunion Edwin 160223.lif - M156 40x s3 Hopx Sox2.tif")
viewer.add_image(
    image0_C, name='C1-Reunion Edwin 160223.lif - M156 40x s3 Hopx Sox2')


# Apply object segmentation

image2_O = napari_accelerated_pixel_and_object_classification.Apply_object_segmentation(
    image0_C, image1_CP)
viewer.add_labels(
    image2_O, name='Result of Object segmentation (apply pretrained, APOC)')
