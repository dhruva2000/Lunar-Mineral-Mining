import cv2
import numpy as np


def interpolate(value, start, end):
    """Interpolate a value between a start and end point."""
    return start + (end - start) * value

'''
min_value should be 0k and max_value should be 400k for temp
min_value should be 0 and max_value should be 45 for slope
'''
def color_to_value(color, min_value, max_value, scale):

    #slope_min = rgb(67,0,71)
    #slope_max = rgb(255,255,255)
    #temp_min = rgb(244,81,255)
    #temp_max = rgb(255,255,255)

    # Define variables
    norm_min_color = np.array([0,0,0]) / 255.0
    norm_max_color = np.array([255,255,255]) / 255.0

    if scale == 'slope':
        norm_min_color = np.array([67,0,71]) / 255.0
        norm_max_color = np.array([255,255,255]) / 255.0
    if scale == 'temp':
        norm_min_color = np.array([244,81,255]) / 255.0
        norm_max_color = np.array([255,255,255]) / 255.0
    if scale == 'tio2':
        norm_min_color = np.array([68,68,68]) / 255.0
        norm_max_color = np.array([255,255,255]) / 255.0

    norm_color = np.array(color) / 255.0
    
    # Calculate the relative position of the color in the gradient
    # Avoid division by zero for a color that matches exactly the min_color
    denom = (norm_max_color - norm_min_color)
    denom = np.where(denom == 0, 1, denom)  # Protect against division by zero
    relative_position = (norm_color - norm_min_color) / denom
    
    # Use the position to interpolate between the min and max values
    # If the color is exactly min_color, set position to 0 (start of scale)
    relative_position = np.where(denom == 1, 0, relative_position)
    
    # Assuming the color gradient is linear and the scale is uniform
    value = np.mean(relative_position)  # Mean position for RGB
    
    # Interpolate the numerical value
    numerical_value = interpolate(value, min_value, max_value)
    return numerical_value



image1 = cv2.imread('./slope.png') #change this to slope or heat
image2 = cv2.imread('./heat.png') #change this to slope or heat
image3 = cv2.imread('./tio2.png') #change this to slope or heat
# Assuming the image is already in the color space you're mapping from
height, width, channels = image.shape

# Initialize an array for your scalar values
slope_map = np.zeros((height, width))
tio2_map = np.zeros((height, width))
heat_map = np.zeros((height, width))

for i in range(height):
    for j in range(width):
        # Extract the color at the current pixel
        color = image1[i, j]
        color2 = image2[i, j]
        color3 = image3[i, j]

        # Convert the color to a value
        slope = color_to_value(color, 0, 45, 'slope')
        heat = color_to_value(color2, 0, 400, 'heat')
        tio2 = color_to_value(color3, 1, 11, 'tio2')


        # Assign the value in your map
        slope_map[i, j] = slope
        heat_map[i, j] = heat
        tio2_map[i, j] = tio2

# 'value_map' now contains the scalar values for each pixel 