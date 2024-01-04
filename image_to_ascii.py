
# TODO https://www.askpython.com/python/examples/turn-images-to-ascii-art-using-python

import PIL.Image

def image_to_ascii(filename=None, can_print=False, textfile=None):
    img_flag = True
    if filename:
        path = filename
    else:
        path = input("Enter the path to the image field : \n")
        
    try:
        img = PIL.Image.open(path)
        img_flag = True
    except:
        print(path, "Unable to find image ")
        return
    
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    
    img = img.convert('L')
    
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    
    if print:
        print(ascii_image)

    if textfile:
        # with open("ascii_image.txt", "w") as f:
        with open(textfile, "w") as f:
            f.write(ascii_image)