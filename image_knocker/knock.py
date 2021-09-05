import cv2
import os
import multiprocessing

#def check_imgs(files):
    

def read_files(path, exts):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if file.lower().endswith(exts):
                files.append(os.path.join(r, file))
    return files

def knock_knock(path, exts=("jpg", 
                            "png", 
                            "jpeg", 
                            "bmp", 
                            "tif", 
                            "tiff")):
    files = read_files(path, exts)
    
    
knock_knock(path=r"C:\Users\yhkwon\Documents\Projects\PyTorch-Lightning-CenterNet\dataset\VOCdevkit")
    