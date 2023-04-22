# Open an Image in Python with PIL.

# Importing Pillow Libraries
from PIL import Image

# Variable with image path.
im_dir="data/page_01.jpg"

# Using Image class's open function to open image by sending variable with path. 
im=Image.open(im_dir)

# Show Image.
im.show()    

# Print metadata of the image.
print(im)

# Rotate and show image
im.rotate(180).show()

# Saving image.
im.save("saved/page_01.jpg")