from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import glob
import os

directory = (glob.glob("downloads/*/"))
print(directory)
try:
   if not os.path.exists("final_save"):
            os.makedirs("final_save")
except OSError:
    print ('Error: Creating directory final_save')

i=0
for d in directory:
    image_dir = (glob.glob(d+"/*"))
    image_dir = image_dir[0]
    print(image_dir)
    img = Image.open(image_dir) # opening the image using the folder which is named using keyword
                                                    # will have to name pictures consistently
    width, height = img.size # get size of image
    draw = ImageDraw.Draw(img) 
    font = ImageFont.truetype("arial.ttf", int(((width+height)/2)/30)) # set font 
    message="The flowers were dangling from the vine." # set the message to write. Eventually move it to be the sentence in which the keyword appears
    w, h = font.getsize(message) # size of text we wrote
    draw.text(((width-w)/2, (9*(height-h))/10), message,font=font) # set the text to be in the center bottom of the screen
    img.save('final_save/'+str(i)+'.jpg') # save the new image. Eventually save it in a folder along with all the other images
    i+=1