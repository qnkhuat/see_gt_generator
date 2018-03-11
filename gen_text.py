import PIL
from PIL import ImageFont,Image,ImageDraw
import os
import numpy as np
import random
import csv
import argparse
import sys
font = ImageFont.truetype('font/arial.ttf',30)

parser= argparse.ArgumentParser()

parser.add_argument('type')

args=parser.parse_args()
gt_name ='csv/'+ args.type+'.csv'
if args.type == 'train':
    iters =10000
elif args.type=='tests':
    iters=100
else:
    sys.exit('wrong type')

#get data dirs
cwd= os.getcwd()
input_dir= cwd + '/background/'
output_dir=cwd + '/results/'+args.type+ '/'

images=os.listdir(input_dir)

#number of iters


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
        n=random.randint(0,len(texts)-1)
        text=texts[n]

        im=im.resize((330,50))
        drawer = ImageDraw.Draw(im)
        drawer.text((5,5),text,(255,255,255),font=font)

        name = imageFile.split('.')
        outfile = output_dir + name[0] + '_' +str(i)+'.' + name[1]
        im.save(outfile)
        print(outfile)

        with open(gt_name,'a') as f:
            writer=csv.writer(f,delimiter='\t')
            writer.writerow([outfile,text])
