import cv2
import tqdm
from itertools import compress
import os
import multiprocessing

import ray
 
def is_corrupted_img(file):
    try:
        img = cv2.imread(file)
        return img is None
    except:
        return True

def read_files(path, exts):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if file.lower().endswith(exts):
                file = os.path.join(r, file)
                file = os.path.abspath(file)
                file = file.replace(os.sep, "/")
                files.append(file)
    return files

def search_corrputed_imgs(path,
                          exts=("jpg",
                                "png",
                                "jpeg",
                                "bmp",
                                "tif",
                                "tiff")
                          ):
    exts = tuple(exts)
    imgs = read_files(path, exts)
    
    
    corrupted_imgs = []
    if len(imgs) > 0:
        ray.init()
        with multiprocessing.Pool() as p:
            is_corrupted = list(tqdm.tqdm(p.imap(is_corrupted_img, imgs), total=len(imgs)))
            corrputed_imgs = list(compress(imgs, is_corrupted))
        ray.shutdown()
        
    return corrputed_imgs
        