#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


IMG_EXTENSIONS = [ # supported image format
    '.bmp',
    '.gif',
    '.jpg',
    '.jpeg',
    '.png',
    '.pbm',
    '.pgm',
    '.ppm',
    '.xbm',
    '.xpm',
]


def get_images_files(directory_path):
    images = []
    for f in next(os.walk(directory_path))[2]:
        ext = os.path.splitext(f)[1]
        if ext in IMG_EXTENSIONS:
            images.append(os.path.join(directory_path, f))
    return images


def get_images_files_recursive(directory_path):
    images = []
    for root, dirs, files in os.walk(directory_path):
        for f in files:
            ext = os.path.splitext(f)[1]
            if ext in IMG_EXTENSIONS:
                images.append(os.path.join(root, f))
    return images


if __name__ == "__main__":
    path = os.path.expanduser("~/.rwbox/images")
    for image in get_images_files(path):
        print(image)
    for image in get_images_files_recursive(path):
        print(image)
