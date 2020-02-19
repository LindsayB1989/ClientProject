import PIL
import matplotlib.pyplot as plt
import PIL.ImageDraw
import os.path

#variable to change the border thickness of the images
x = 20

def frameOneImage(originalImage, borderThickness=x):
    '''Puts a frame around the image that you select.
    The thickness of the border may be changed with the variable x above.
    Also, squares will be placed on the corners of the border.
    Text is also created and is centered on the bottom border of the picture frame.'''

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

    #shows the new image on the plot
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(image_small, interpolation='none')
    fig.show()

def showDifference(originalImage, borderThickness=x):
    '''Uses the same methods in the frameOneImage function except for what is displayed on the subplots.
    The original image is shown on the first plot, and the altered image is on the second.
    It helps to compare the images side by side.'''

    #get the selected image from the current directory
    directory = os.path.dirname(os.path.abspath(__file__))  
    original_file = os.path.join(directory, originalImage)
    original_img = PIL.Image.open(original_file)
    image_small = original_img.resize((200, 300))
    ogImage = PIL.Image.open(original_file)

    #creates the frame by adding a rectangle on each side
    draw = PIL.ImageDraw.Draw(image_small)
    width, height = image_small.size
    draw.polygon( [(0, 0), (0, height), (borderThickness, height),(borderThickness, 0)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#left
    draw.polygon( [(0, 0), (0, borderThickness),(width, borderThickness),  (width, 0)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#top
    draw.polygon( [(0, height), (0, height-borderThickness), (width, height-borderThickness),(width, height)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#bottom
    draw.polygon( [(width, 0), (width-borderThickness, 0), (width-borderThickness, height),(width, height)], fill=(0, 0, 0, 255), outline=(0, 0, 0, 255))#right

    #shows the original image on the first plot and the altered image on the second
    fig, axes = plt.subplots(1, 2)
    axes[0].set_title('Original Image')
    axes[0].imshow(ogImage, interpolation='none')
    axes[1].set_title('New Image')
    axes[1].imshow(image_small, interpolation='none')