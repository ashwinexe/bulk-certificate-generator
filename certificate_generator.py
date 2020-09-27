### make sure to rename the csv as 'data.csv' and certificate template as template.jpg
### also works with excel sheets but pd.read_csv must be changed to pd.read_xslx
import pandas as pd
import os,sys, time
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
data = pd.read_csv("data.csv")
name_list = data["name"].tolist()

if  os.path.exists('output'):
    print('\noutput folder already exists. Certificates in it will be overwritten')
    print('continue? Y/N')
    confirm = input()
    if(confirm == 'y' or confirm == 'Y'):
        print('overwriting the data')
    else:
        exit(0)
else:
    print('\nCertificates will be in output folder.')
    #name ouf the output folder
    os.mkdir('output')

# print('\nProcessing....')
for i in tqdm(name_list):
        im = Image.open("template.jpg")
        d = ImageDraw.Draw(im)
        text_color = (0, 0, 0)
        # look up the windows settings -> fonts,  and type exact keyword to use installed fonts
        font = ImageFont.truetype("corbelli.ttf", 100)
        w, h = d.textsize(i, font)
        horizontal = (im.width - w)
        vertical = (im.height - h)
        
        # you can change location value to relocate the name. text goes right and down if x, y is increased respectively.
        location = (horizontal/2, vertical/2 - 50)
        d.text(location, i, anchor="north", fill = text_color, font = font)
        # you can chnage the format to .jpg too!
        im.save("output/certificate_" + i + ".pdf")

print('Done!')
time.sleep(1)
