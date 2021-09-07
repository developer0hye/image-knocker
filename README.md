# image-knocker

Knock your images before these make you painful.

## Background

One day, I had run my deep learning model training program and got off work on Friday. When I checked the training process on Monday after arriving at work, the program was terminated because of some images that cannot be opened by image processing libraries like PIL.

I developed this project to check images that cannot be opened by image processing libraries before running computer vision applications.

`image-knocker` is very fast and simple!

## Install

```
pip install image-knocker
```

## Usage

```console
foo@bar:~$ image-knocker --path dataset_path/ --exts png jpg jpeg
```

## Output


### if `corrupted image` in `dataset`:
```
  Knocking... Root Path: D:\datasets\detection\VOCdevkit
  100%|██████████████████| 34179/34179 [00:03<00:00, 10911.31it/s]
  Corrupted image files are detected!
  D:/datasets/detection/VOCdevkit/outlier.png
  Corrupted image file list is saved to D:\datasets\detection\corrupted_imgs_list.txt
```
### else:
```
  Knocking... Root Path: D:\datasets\detection\VOCdevkit
  100%|██████████████████| 34178/34178 [00:04<00:00, 7792.30it/s]
  There are no corrupted image files! 
  All images were loaded successfully using PIL.Image.open!
```
