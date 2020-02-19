import PIL
import matplotlib.pyplot as plt
import PIL.ImageDraw
import os.path

#variable to change the border thickness of the images
x = 20

def frameImage(originalImage, borderThickness=x):
    '''Puts a frame around the image that you select.
    The thickness of the border may be changed with the variable x above.
    Also, squares will be placed on the corners of the border.
    Text is also created and is centered on the bottom border of the picture frame.
    The function is used to show the features that were not possible with the frameAllImages() and frameOneImage() functions.'''
    
    #get the selected image from the current directory
    directory = os.path.dirname(os.path.abspath(__file__))
    original_file = os.path.join(directory, originalImage)
    original_img = PIL.Image.open(original_file)
    image_small = original_img.resize((200, 300))
    
    #creates the frame by adding a rectangle on each side
    draw = PIL.ImageDraw.Draw(image_small)
    width, height = image_small.size
    draw.polygon( [(0, 0), (0, height), (borderThickness, height),(borderThickness, 0)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255)) #left
    draw.polygon( [(0, 0), (0, borderThickness),(width, borderThickness),  (width, 0)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#top
    draw.polygon( [(0, height), (0, height-borderThickness), (width, height-borderThickness),(width, height)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#bottom
    draw.polygon( [(width, 0), (width-borderThickness, 0), (width-borderThickness, height),(width, height)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#right
    
    #adds text to the bottom of the picture frame
    center = (.5*width-45)
    draw.text((center, (height-(.5*borderThickness)-5)), 'The Smith Family', fill=(255, 255, 255, 0), font=None)

    #draws a pink square on the corners of the image's borders
    draw.polygon( [(0, 0), (0, borderThickness), (borderThickness, borderThickness), (borderThickness, 0)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#top left
    draw.polygon( [(0, height), (0, height-borderThickness), (borderThickness, height-borderThickness), (borderThickness, height)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#bottom left
    draw.polygon( [(width, 0), (width-borderThickness, 0), (width-borderThickness, borderThickness), (width, borderThickness)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#top right
    draw.polygon( [(width, height), (width, height-borderThickness), (width-borderThickness, height-borderThickness), (width-borderThickness, height)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#bottom right
    
    #shows the new image on the plot
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(image_small, interpolation='none')
    fig.show()
    
def frameOneImage(originalImage, borderThickness=x):
    '''Puts a frame around the image that you select.
    The thickness of the border may be changed with the variable x above.
    Also, squares will be placed on the corners of the border.
    Text is also created and is centered on the bottom border of the picture frame.'''

    #Was intended to get the selected image from the current directory, yet failed because originalImage was not a PIL.Image file to begin with
    '''directory = os.path.dirname(os.path.abspath(__file__))  
    original_file = os.path.join(directory, originalImage)
    original_img = PIL.Image.open(original_file)
    image_small = original_img.resize((200, 300))'''
    
    
    #creates the frame by adding a rectangle on each side
    width, height = originalImage.size
    draw = PIL.ImageDraw.Draw(originalImage)
    draw.polygon( [(0, 0), (0, height), (borderThickness, height),(borderThickness, 0)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255)) #left
    draw.polygon( [(0, 0), (0, borderThickness),(width, borderThickness),  (width, 0)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#top
    draw.polygon( [(0, height), (0, height-borderThickness), (width, height-borderThickness),(width, height)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#bottom
    draw.polygon( [(width, 0), (width-borderThickness, 0), (width-borderThickness, height),(width, height)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#right
    
    #adds text to the bottom of the picture frame
    center = (.5*width-45)
    draw.text((center, (height-(.5*borderThickness)-5)), 'The Smith Family', fill=(255, 255, 255, 0), font=None)
    
    #draws a pink square on the corners of the image's borders
    draw.polygon( [(0, 0), (0, borderThickness), (borderThickness, borderThickness), (borderThickness, 0)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#top left
    draw.polygon( [(0, height), (0, height-borderThickness), (borderThickness, height-borderThickness), (borderThickness, height)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#bottom left
    draw.polygon( [(width, 0), (width-borderThickness, 0), (width-borderThickness, borderThickness), (width, borderThickness)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#top right
    draw.polygon( [(width, height), (width, height-borderThickness), (width-borderThickness, height-borderThickness), (width-borderThickness, height)], fill=(255,192,203, 255), outline=(0, 0, 0, 255))#bottom right
    
    #shows the new image on the plot
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(originalImage, interpolation='none')
    fig.show()
    
def get_images(directory=None):
    '''Returns PIL.Image objects for all the images in directory.
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory'''
    
    #if the directory is not stated, then use the current working directory.
    if directory == None:
        directory = os.getcwd()
        
    #makes empty lists to store information about the image files
    image_list = []
    file_list = []
    
    '''takes the things in the directory and puts them into a list. 
    For the items in the directory, the images are added to the image list and are opened as PIL images, 
    and the file list directly stores the information in the directory_list.'''
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    
def frameAllImages(directory=None):
    '''Saves a modfied version of each image in directory.
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have a picture frame, a shape drawn on as a mask, and text.'''
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  
    
    # Go through the images and save modified versions
    for n in range(len(image_list)):
        print n
        filename, filetype = os.path.splitext(file_list[n])
        
        #Was intended to add the frame with the default thickness to the images, but failed because the frameOneImage function's originalImage was not a PIL.Image and the methods of the class won't work.
        curr_image = image_list[n]
        new_image = frameOneImage(curr_image) 
        
        #Intended to save the altered image, but failed because the save method is only for the PIL.Image class, not PIL.ImageDraw.
        '''new_image_filename = os.path.join(new_directory, filename + '.jpg')
        new_image.save(new_image_filename)'''
