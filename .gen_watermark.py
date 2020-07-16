#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import sys
import glob
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

mark_file = ".watermark.file"

def get_imgs_files(file_dir):
    imgs = []
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            if f.endswith('jpg'):
                imgs.append(os.path.join(root, f))
            if f.endswith('JPG'):
                imgs.append(os.path.join(root, f))
            if f.endswith('jpeg'):
                #imgs.append(os.path.join(root, f))
                print("JPEG:", root + f)
            if f.endswith('png'):
                imgs.append(os.path.join(root, f))
            if f.endswith('PNG'):
                imgs.append(os.path.join(root, f))
    return imgs

def add_watermark_text(img):
    wm_text = "https://winddoing.github.io"

    w = img.size[0]
    h = img.size[1]
    wm_font_sz = max(16, int(w/30))
    wm_text_len = len(wm_text)

    font_type = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", wm_font_sz)
    draw = ImageDraw.Draw(img)
    draw.text(xy=(w/4, h/2), text=wm_text, fill=(220,220,220), font=font_type)

def watermark(images_dir):
    imgs_files = get_imgs_files(images_dir)

    for file in imgs_files:
        #print(file)
        im = Image.open(file)
        if len(im.getbands()) < 3:
            im = im.convert('RGB')
            print(file)

        add_watermark_text(im)
        print(file)

        im.save(file)


if __name__ == '__main__':
    watermark('public/images/')
