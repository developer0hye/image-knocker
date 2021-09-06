# image-knocker

Knock your images before these make you painful.

# Background

One day, I had runned my deep learning model training program and got off work at Friday.

When I checked the trainning process at Monday after arriving at work, the program was terminated because of some images that cannot be opened by image processing libraries like PIL.

![img](https://user-images.githubusercontent.com/35001605/132240388-d54b710f-4d87-461c-855e-cbab155a3a4c.png)

I developed this project to check images that cannot be opened by image processing libraries before running computer vision applications.

`image-knocker` is very fast!

# Install

```
pip install image-knocker
```

# Usage

```console
foo@bar:~$ image-knocker --path dataset_path/ --exts png jpg jpeg
```

if `corrupted image` in `dataset`:

![image](https://user-images.githubusercontent.com/35001605/132241444-fffa8eda-cccd-44e6-9f43-5943c4ae2614.png)

else:

![image](https://user-images.githubusercontent.com/35001605/132238630-39fcd964-1603-4c71-9e38-f0643ea04817.png)



