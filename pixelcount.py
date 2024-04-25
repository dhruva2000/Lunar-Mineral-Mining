from PIL import Image
import numpy as np

def analyze_image_colors(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    
    # Convert the image into a numpy array
    img_array = np.array(img)
    # Reshape the array to a 2D array where each row represents a pixel
    pixels = img_array.reshape(-1, 3)
    
    # Find unique colors and their counts
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
    
    # Convert color data to a human-readable format and calculate percentage
    color_info = []
    total_pixels = img.size[0] * img.size[1]
    for color, count in zip(unique_colors, counts):
        # percentage = (count / total_pixels) * 100
        color_info.append({
            # "color": tuple(color),
            "count": count,
            # "percentage": percentage
        })
    
    return color_info

region = './quantized/region.png'
heat = './quantized/heat.png'
slope = './quantized/slope.png'
tio2 = './quantized/tio2.png'

regionresult = analyze_image_colors(region)
heatresult = analyze_image_colors(heat)
sloperesult = analyze_image_colors(slope)
tio2result = analyze_image_colors(tio2)

print("Region result: ", regionresult)
print("Heat result: ", heatresult)
print("Slope result: ", sloperesult)
print("Tio2 result: ", tio2result)