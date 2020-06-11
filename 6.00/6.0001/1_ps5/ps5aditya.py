
"""
# Problem Set 5
# Name: ADITYA MEHROTRA
# Collaborators: NONE
# Time: 3HRS
"""

from PIL import Image
import numpy

def scale_to_0255(num):
    """
    Scales the binary digit 1 or 0 to a 0-255 scale
    """
    if num == 0:
        return 0
    elif num == 1:
        return 255
    return None

def generate_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0],[.558, .442, 0],[0, .242, .758]]
    elif color == 'green':
        c = [[0.625,0.375, 0],[ 0.7,0.3, 0],[0, 0.142,0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0],[0, 0.433, 0.567],[0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0],[0, 1, 0.],[0, 0., 1]]
    return c


def matrix_multiply(m1,m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """

    product = numpy.matmul(m1,m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def convert_image_to_pixels(image):
    """
    Takes an image (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of tuples representing pixels.
    Each pixel is a tuple containing (R,G,B) values.

    Returns the list of tuples.

    Inputs:
        image: string representing an image file, such as 'lenna.jpg'
    Returns: list of pixel values in form (R,G,B) such as
                 [(0,0,0),(255,255,255),(38,29,58)...]
    """
    im = Image.open(image)
    return list(im.getdata())


def convert_pixels_to_image(pixels,size):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels: a list of pixels such as the output of
                convert_image_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
    Returns:
        img: Image object made from list of pixels
    """
    im = Image.new("RGB", size)
    im.putdata(pixels)
    return im


def apply_filter(pixels, color):
    """
    pixels: a list of pixels in RGB form, such as [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing the color
    deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """
    transform = generate_matrix(color)
    list_pixels_new = []
    lst = []
    for pixel in pixels:
        lst = matrix_multiply(transform, pixel)
        new_pixel = (int(lst[0]), int(lst[1]), int(lst[2]))
        list_pixels_new.append(new_pixel)
    return list_pixels_new

def get_BW_lsb(pixels):
    """
    Gets the least significant bit of each pixel in the specified image.
    Inputs:
       pixels: list, a list of pixels in BW form, such as [0, 255, 120, ...]
    returns:
       lsb: a list of least significant bits
    """
    lsb = []
    for pixel in pixels:
        binary = "{0:b}".format(pixel)
        num = int(binary[-1:])
        lsb.append(scale_to_0255(num))
    return lsb


def get_RGB_lsb(pixels):
    """
    Gets the 2 least significant bits of each pixel in the specified color image.
    Inputs:
        pixels: a list of pixels in RGB form, such as [(0,0,0),(255,255,255),(38,29,58)...]
    Returns:
        lsb: a list of least significant bits
    """
    lsb = []
    for pixel in pixels:
        binary1 = "{0:b}".format(pixel[0])
        binary2 = "{0:b}".format(pixel[1])
        binary3 = "{0:b}".format(pixel[2])
        num1 = scale_to_0255(int(binary1[-1:]))
        num2 = scale_to_0255(int(binary2[-1:]))
        num3 = scale_to_0255(int(binary3[-1:]))
        lsb.append((num1, num2, num3))
    return lsb


def reveal_image(filename, mode):
    """
    Extracts the hidden image, calls get lsb function based on parameter

    Inputs: 
        filename: string, input file to be processed
        mode: 'RGB' or '1' based on whether input file is color ('RGB') or black/white ('1'); see PIL Modes
    Returns:
        result: an Image object containing the hidden image
    """
    im_TO_GET_SIZE = Image.open(filename)
    size = im_TO_GET_SIZE.size 
    lsb_list = []
    if mode == '1':
        lsb_list = get_BW_lsb(convert_image_to_pixels(filename))
        im = Image.new('1', size)
    if mode == 'RGB':
        lsb_list = get_RGB_lsb(convert_image_to_pixels(filename))
        im = Image.new('RGB', size)
    im.putdata(lsb_list)
    return im
    



def main():
    #pass

    # UNCOMMENT the following 8 lines to test PART 1

    #im = Image.open('img_29.jpg')    
    #width, height = im.size
    #pixels = convert_image_to_pixels('img_29.jpg')
    #image = apply_filter(pixels,'none')
    #im = convert_pixels_to_image(image, (width, height))
    #im.show()
    #new_image = apply_filter(pixels,'red')
    #im2 = convert_pixels_to_image(new_image,(width,height))
    #im2.show()


    # PART 2
    im = Image.open('hidden2.bmp')
    im.show()    
    reveal_image('hidden2.bmp', 'RGB').show()

if __name__ == '__main__':
    main()
