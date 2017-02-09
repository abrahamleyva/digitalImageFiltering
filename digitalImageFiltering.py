#Author: Abraham Medina
#Link to github https://github.com/abrahamleyva/digitalImageFiltering
from PIL import Image #Import Pillow Library
import os.path #Library for finiding number of fliles in a directory

def median(arr): #Finds the median of an array
    arr = sorted(arr) #Sorts the array
    if len(arr) == 0:
        return None
    elif len(arr) % 2 == 0:
        return (arr[len(arr) / 2 - 1] + arr[len(arr) / 2]) / 2
    else:
        return arr[len(arr) / 2]
        
path = 'images' #setting path to the directory that holds the images
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]) - 1 #num_files is set to the number of images in a directory
        
imgArr = [None] * num_files #Defines an empty array for the raw images
for i in range(0, num_files):
    imgArr[i] = Image.open("images/" + str(i + 1) + ".png") #Sets the raw images to the array

width, height = imgArr[0].size #Saves the size of the images

#Creats an empty array of size num_files for each color
redArr = [None] * num_files
greenArr = [None] * num_files
blueArr = [None] * num_files

#Inicializes variables for the final RGB for every pixel
finalR = 0;
finalG = 0;
finalB = 0;

imgArr[1].save("images/final.png") #Creats a copy of the first image
newImg = Image.open("images/final.png") #Opens and saves the new raw image
finalPix = newImg.load() #Makes the new image able to be processes
pixArr = [None] * num_files #Defines an empty array of images that can be processed

print("Processing...")

for i in range(0, num_files):
    pixArr[i] = imgArr[i].load() #Sets the processable images to pixArr

for y in range(0, height): #Goes through vertical pixels
    for x in range(0, width): #Goes through horizontal pixels
        for a in range(0, num_files): #Goes through every image
            pix = pixArr[a] #Sets a particular processable image to a temp variable
            redArr[a], greenArr[a], blueArr[a] = pix[x, y] #Takes pixel info from  the temp image and sets it to multiple arrays
            
        finalR = median(redArr) #Gets median red value and sets it to the final red variable
        finalG = median(greenArr) #Gets median green value and sets it to the final green variable
        finalB = median(blueArr) #Gets median blue value and sets it to the final blue variable
        
        finalPix[x, y] = (finalR, finalG, finalB) #Sets the median RGB values to the pixel of the final image
newImg.save("images/final.png") #Saves the final image
print("Complete!")