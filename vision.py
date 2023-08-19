import cv2 as cv
import numpy as np
import os
import pyautogui
import time

class Vision:

    # properties
    needle_img_paths = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):               
        self.needle_img_paths = [os.path.join(needle_img_path , filename) for filename in os.listdir(needle_img_path)]      
        self.method = method

    def find(self, haystack_img, threshold=0.5, debug_mode=None):      
        #haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)
        
        all_points = []
        for needle_img_path in self.needle_img_paths:
            needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
            needle_w = needle_img.shape[1]
            needle_h = needle_img.shape[0]

            needle_img = needle_img[...,:3]
            needle_img = cv.cvtColor(needle_img, cv.COLOR_RGB2BGR)
            result = cv.matchTemplate(haystack_img, needle_img, self.method)

            locations = np.where(result >= threshold)
            locations = list(zip(*locations[::-1]))
            #print(locations)
            rectangles = []
            for loc in locations:
                rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
                rectangles.append(rect)
                rectangles.append(rect)
            rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    
            for (x, y, w, h) in rectangles:
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                all_points.append((center_x, center_y))               
                
                if debug_mode == 'rectangles':
                    cv.rectangle(haystack_img, (x, y), (x + w, y + h), color=(0, 255, 0), lineType=cv.LINE_4, thickness=2)
                elif debug_mode == 'points':                    
                    cv.drawMarker(haystack_img, (center_x, center_y), color=(255, 0, 255), markerType=cv.MARKER_CROSS, markerSize=40, thickness=2)

        if debug_mode:           
            cv.namedWindow('Matches',cv.WINDOW_AUTOSIZE)
            #cv.resizeWindow('Matches', haystack_img.shape[0], haystack_img.shape[1])
            cv.imshow('Matches', haystack_img)          
           

        return all_points

         