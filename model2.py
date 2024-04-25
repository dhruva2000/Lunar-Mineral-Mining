import cv2
import numpy as np
def interpolate(value, start, end):
    """Interpolate a value between a start and end point."""
    return start + (end - start) * value

def color_to_value(color, min_value, max_value):
    # Normalize the color and min/max colors to a 0-1 range
    norm_color = np.array(color) / 255.0
    norm_min_color = np.array([75,10,100]) / 255.0 #change this one
    norm_max_color = np.array([255,255,255]) / 255.0 #change this one
    
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



image = cv2.imread('/Users/dhruvareddy/Downloads/LOLA_slope.png') #change this one

# Assuming the image is already in the color space you're mapping from
height, width, channels = image.shape

# Initialize an array for your scalar values
value_map = np.zeros((height, width))

for i in range(height):
    for j in range(width):
        # Extract the color at the current pixel
        color = image[i, j]

        # Convert the color to a value
        value = color_to_value(color, 0, 45)

        # Assign the value in your map
        value_map[i, j] = value

print(value_map)

# 'value_map' now contains the scalar values for each pixel 