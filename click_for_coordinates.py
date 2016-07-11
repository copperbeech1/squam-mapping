#!/usr/bin/python

import numpy as np
import cv2
import argparse
import os

img = None
img_fresh = None
vertices = []
x_scale_factor = 0
y_scale_factor = 0


def render_image():
    print("rendering image...")

    global img, x_scale_factor, y_scale_factor

    new_w = 2000
    new_h = 1200

    x_scale_factor = float(img.shape[1]) / float(new_w)
    y_scale_factor = float(img.shape[0]) / float(new_h)

    img_for_display = cv2.resize(img, (2000, 1200))
    cv2.imshow('image', img_for_display)


def add_point(pt_xy):
    print("adding point...")

    assert type(pt_xy)==tuple
    assert len(pt_xy)==2

    global vertices
    
    vertices.append(pt_xy)

def delete_last_point():
    print("deleting last vertex...")

    global vertices
    del vertices[-1]

def export_points():
    print("exporting points...")
    
    global vertices

    print("printing vertices...")
    for v in vertices:
        print(v)

    print("done")

def render_polygon():
    print("rendering polygon...")
    global img, vertices

    img = img_fresh.copy()

    cv2.line(img, (0, 0), (500, 500), (0, 255, 0))

    cv2.polylines(img, np.int32([np.array(vertices)]), 1, (255, 0, 0))
    render_image()

def click_handler(event, x, y, flags, param):

    scaled_x = int(round( float(x) * float(x_scale_factor) ))
    scaled_y = int(round( float(y) * float(y_scale_factor) ))

    if event == cv2.EVENT_LBUTTONUP:
        print("left-button-up")
        add_point((scaled_x, scaled_y))

def main():
    print("starting main()...")

    global img, img_fresh

    parser = argparse.ArgumentParser(description='Simple map processor')
    parser.add_argument('-i', type=str, required=True, help='input image file path')

    args = parser.parse_args()

    print("args: ", args)

    img = cv2.imread(args.i)
    img_fresh = img.copy()

    #img_for_display = cv2.resize(img, (2000, 1200))

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_handler)
    #cv2.imshow('image', img_for_display)
    
    render_image()
    

    while(1):
        k = cv2.waitKey(0) & 0xFF
        print("k = "+str(k))
        if k == ord('q'):
            break
        
        elif k == ord('e'): # 'e' = export points
            export_points()

        elif k == ord('d'): # 'd' = delete last point
            delete_last_point()

        elif k == ord('r'): # 'r' = render polygon
            render_polygon()

            

if __name__ == "__main__":
    main()
