#!/usr/bin/python

import numpy as np
import cv2
import argparse
import os

GRID_SIZE_FT=300

def load_washburn_maps(washburn_dir_path):
    
    map_1 = cv2.imread(os.path.join(washburn_dir_path, "map_1-little_squam.png"))
    map_2 = cv2.imread(os.path.join(washburn_dir_path, "map_2-cotton_cove.png"))
    map_4 = cv2.imread(os.path.join(washburn_dir_path, "map_4-moon_and_bowman_islands.png"))
    map_6 = cv2.imread(os.path.join(washburn_dir_path, "map_6-high_haith.png"))
    map_7 = cv2.imread(os.path.join(washburn_dir_path, "map_7-merrill_islands.png"))
    map_8 = cv2.imread(os.path.join(washburn_dir_path, "map_8-squaw_cove.png"))
    map_9 = cv2.imread(os.path.join(washburn_dir_path, "map_9-yard_islands.png"))
    map_10 = cv2.imread(os.path.join(washburn_dir_path, "map_10-sandwich_bay.png"))
    map_11 = cv2.imread(os.path.join(washburn_dir_path, "map_11-long_island_shortline_detail.png"))
    map_12 = cv2.imread(os.path.join(washburn_dir_path, "map_12-dog_cove.png"))
    
    maps_dict = {1: map_1, 2: map_2, 4: map_4, 6: map_6, 7: map_7, 8: map_8, 9: map_9, 10: map_10, 11: map_11, 12: map_12}

    return maps_dict
    
def load_washburn_map_resolutions():

    map_1_res_x = 3.525 # ft/pixel
    map_1_res_y = 3.515 # ft/pixel

    res_dict = {1: (map_1_res_x, map_1_res_y)}
    
    return res_dict

def draw_grid(image, offset, res_ft_per_pixel, grid_size):

    w = image.shape[1]
    h = image.shape[0]

    interval_px_float_x = float(grid_size) / float(res_ft_per_pixel[1])
    interval_px_float_y = float(grid_size) / float(res_ft_per_pixel[0])
    print("interval_px_x = "+str(interval_px_float_x))
    print("interval_px_y = "+str(interval_px_float_y))

    n_lines_h = int(round(float(h-offset[1]) / interval_px_float_y))
    n_lines_w = int(round(float(w-offset[0]) / interval_px_float_x))

    line_color = (0, 255, 0)

    # draw horizontal lines
    for i in range(0, n_lines_h):
        
        y = int(round(i * interval_px_float_y)) + int(offset[1])

        cv2.line(image, (0, y), (w, y), line_color)
        
    # draw vertical lines
    for i in range(0, n_lines_w):

        x = int(round(i * interval_px_float_x)) + int(offset[0])

        cv2.line(image, (x, 0), (x, h), (0, 0, 255))

    

def main():
    print("starting main()...")

    parser = argparse.ArgumentParser(description='Simple map processor')
    #parser.add_argument('-i', type=str, required=True, help='input image file path')

    args = parser.parse_args()

    print("args: ", args)

    maps_dict = load_washburn_maps("washburn_images")
    map_res_dict = load_washburn_map_resolutions()

    #print("maps_dict: "+str(maps_dict))

    #img = cv2.cvtColor(maps_dict[1], cv2.COLOR_BGR2GRAY)
    img = maps_dict[1]
    

    print("img.shape = "+str(img.shape))

    draw_grid(img, (187, 410), map_res_dict[1], GRID_SIZE_FT)

    img_for_display = cv2.resize(img, (2000, 1200))

    cv2.imshow('input image', img_for_display)

    while(1):
        k = cv2.waitKey(0)
        print("k = "+str(k))
        if k == 1048689:
            break

if __name__ == "__main__":
    main()
