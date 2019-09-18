from google_images_download import google_images_download  # Importing google_images_download module 
from rake_nltk import Rake # Rapid Automatic Keyword Extraction algorithm
# For writing on the images.
from translate import Translator
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import glob
import os
import shutil

# Delete downloads and final_save folders to work with new ones
if os.path.exists("downloads"):
    shutil.rmtree("downloads")
if os.path.exists("final_save"):
    shutil.rmtree("final_save")


r = Rake(min_length=1, max_length=1) # Uses stopwords for english from NLTK, and all punctuation characters.

text = input("Hello!\nI will find images for your keywords and translate your sentence(s) for you.\nTo look up an image for every word, seperate with periods.\n\nWrite your sentence(s) below please:\n")
lang = input("\nWhat language do you want to translate the sentence(s) to?\n")

translator= Translator(from_lang="english",to_lang=lang)

text_sentences=list(text.split("."))

usr=r._generate_phrases(text_sentences)

print(usr)

response = google_images_download.googleimagesdownload()  

search_queries = (usr)
  
  
# download the images using the key words
def downloadimages(query,picture_counter): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urls is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": "Picture of "+query, 
                 "format": "jpg", 
                 "limit":1, 
                 "silent_mode":True,
                 "usage_rights":"labeled-for-reuse",
                 "print_urls":False, 
                 "size": "medium"} 
    try: 
        response.download(arguments,picture_counter) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": "Picture of "+query, 
                     "format": "jpg",
                     "limit":10, 
                     "silent_mode":True,
                     "usage_rights":"labeled-for-reuse",
                     "print_urls":False,  
                     "size": "medium"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
 
 # Writes on images the given text
def image_writer(d,i,text_given):
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
    
    print(str(translator.translate(text_given)))
    trans_message=str(translator.translate(text_given))
    w_trans, h_trans = font.getsize(trans_message) # size of text we wrote

    draw.rectangle(((width-w_trans)/2, (1*(height-h_trans))/10, ((width-w_trans)/2) + w_trans, ((1*(height-h_trans))/10   ) + h_trans), fill='black') #black background for text
    draw.text(((width-w_trans)/2, (1*(height-h_trans))/10), trans_message,font=font) # set the text to be in the center bottom of the screen
    
    img.save('final_save/'+str(i)+'.jpg') # save the new image. Eventually save it in a folder along with all the other images

 # Navigate the folders and drive image_writer
def image_maker(text_given):
    try:
        if not os.path.exists("final_save"):
                    os.makedirs("final_save")
    except OSError:
        print ('Error: Creating directory final_save') 

    directory = (glob.glob("downloads/*/"))
    print(directory)
        
    n=0
    for d in directory:
        image_writer(d,n,text_given[n])
        n+=1

# divides sentences using keywords
def div_sen_key(sen_list,search_queries):
    div_sen=[] # list of divided sentences to put on images
    for sen in sen_list:
        print("Sentence being observed:",sen)
        word_start=0 # index of the word to start with
        word_counter=0 # count words
        for word in list(sen.split(" ")):
            clean_word=word.replace(',','')
            clean_word=clean_word.replace('!','')
            clean_word=clean_word.replace('.','')
            clean_word=clean_word.replace('?','')
            clean_word=clean_word.replace(':','')
            clean_word=clean_word.replace(';','')
            clean_word=clean_word.lower()
            word_counter+=len(word)+1
            if clean_word in search_queries:
                div_sen.append(sen[word_start:word_counter])
                word_start=word_counter
    return div_sen

# Driver Code 
count=0
for query in search_queries: 
    print(query)
    downloadimages(query,count)
    count+=1
print("Sentences after division:",div_sen_key(text_sentences,search_queries))
image_maker(div_sen_key(text_sentences,search_queries))