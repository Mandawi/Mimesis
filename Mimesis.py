from google_images_download import google_images_download  # Importing google_images_download module 
from rake_nltk import Rake # Rapid Automatic Keyword Extraction algorithm
# For writing on the images.
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import glob
import os

r = Rake(min_length=1, max_length=4) # Uses stopwords for english from NLTK, and all punctuation characters.

text = input("Hello!\nWrite your summary below please:\n")

text_sentences=list(text.split("."))

usr=r._generate_phrases(text_sentences)

usr = [''.join(i) for i in usr]

print(usr)

# creating object 
response = google_images_download.googleimagesdownload()  

search_queries = (usr) # To get keyword phrases ranked highest to lowest.
  
  
def downloadimages(query): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urls is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": str(query), 
                 "format": "jpg", 
                 "limit":1, 
                 "silent_mode":True,
                #  "usage_rights":"labeled-for-reuse",
                 "print_urls":False, 
                 "size": "medium",
                 "aspect_ratio": "wide"} 
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg",
                     "limit":10, 
                     "silent_mode":True,
                    #  "usage_rights":"labeled-for-reuse",
                     "print_urls":False,  
                     "size": "medium",
                     "aspect_ratio": "wide"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
  
def image_maker(text_given):
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
        img = Image.open(image_dir) # opening the image using the folder which is named using keyword
                                                        # will have to name pictures consistently
        width, height = img.size # get size of image
        draw = ImageDraw.Draw(img) 
        font = ImageFont.truetype("arial.ttf", int(((width+height)/2)/30)) # set font 
        message=text_given # set the message to write. Eventually move it to be the sentence in which the keyword appears
        w, h = font.getsize(message) # size of text we wrote
        draw.rectangle(((width-w)/2, (9*(height-h))/10, ((width-w)/2) + w, ((9*(height-h))/10) + h), fill='black') #black background for text
        draw.text(((width-w)/2, (9*(height-h))/10), message,font=font) # set the text to be in the center bottom of the screen
        img.save('final_save/'+str(i)+'.jpg') # save the new image. Eventually save it in a folder along with all the other images
        i+=1

# Driver Code 
for query in search_queries: 
    downloadimages(query)  

image_maker(text)


