# Removing image background
from rembg import remove
from PIL import image

input_path = "zoom.jpg"
output_path = "zoom.png"

inp = image.open (input_path)
output = remove(inp)
output.save(output_path) 
