import PIL
from PIL import ImageFont,Image,ImageDraw
import os
import numpy as np
import random
import csv
import argparse
font = ImageFont.truetype('/Library/Fonts/Arial.ttf',30)

parser= argparse.ArgumentParser()

parser.add_agrument('type')

args=parser.parse_args()
gt_name = args.type+'.csv'

#get data dirs
cwd= os.getcwd()
input_dir= cwd + '/background/'
output_dir=cwd + '/results/'

images=os.listdir(input_dir)

#number of iters
iters=1000


with open('vin_list.txt','r') as f:
    texts=f.read()
    texts=texts.split('\n')

with open(gt_name, 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow([17, 1])

for i in range(iters):
    for imageFile in images:
        try:
            im = Image.open(input_dir + imageFile)

        except :
            continue

        #randomly text a
        n=random.randint(0,len(texts))
        text=texts[n]

        im=im.resize((230,50))
        drawer = ImageDraw.Draw(im)
        drawer.text((5,5),text,(255,255,255),font=font)

        name = imageFile.split('.')
        outfile = output_dir + name[0] +str(i)+'.' + name[1]
        im.save(outfile)
        print(outfile)

        with open('gt_path.csv','a') as f:
            writer=csv.writer(f,delimiter='\t')
            writer.writerow([outfile,text])
