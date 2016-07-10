#!/usr/bin/python

import numpy as np
import cv2
import argparse

def main():
    print("starting main()...")

    parser = argparse.ArgumentParser(description='Simple map processor')
    parser.add_argument('-i', type=str, required=True, help='input image file path')

    args = parser.parse_args()

    print("args: ", args)

    img = cv2.imread(args.i)

    print("img.shape = "+str(img.shape))

    #img_for_display = cv2.resize(img, (

    cv2.imshow('input image', img)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
