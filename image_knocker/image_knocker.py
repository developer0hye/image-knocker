import os
import argparse
from .image_knock import search_corrputed_imgs

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, default="./", help="Dataset Path")
    parser.add_argument("--exts", 
                        type=str, 
                        action="store",
                        nargs="+",
                        default=["jpg",
                                 "png",
                                 "jpeg",
                                 "bmp",
                                 "tif",
                                 "tiff"],
                        help="Image File Extension List")
    parser.add_argument("--output-path", type=str, default="./", help="Where to save corrupted image file list")
    parser.add_argument('--nosave', action='store_true', help='Only print corrupted image file list without saving file')
    args = parser.parse_args()
    
    assert os.path.isdir(args.path)
    
    print(bcolors.OKGREEN + f"Knocking... Root Path: {os.path.abspath(args.path)}" + bcolors.ENDC)
    
    corrupted_imgs = search_corrputed_imgs(path=args.path,
                                           exts=args.exts)
  
    if len(corrupted_imgs) == 0:
        print(bcolors.OKGREEN + "There are no corrupted image files! All images were loaded successfully using PIL.Image.open!" + bcolors.ENDC)
    else:
        corrupted_imgs = "\n".join(corrupted_imgs)
        
        print(bcolors.FAIL + "Corrupted image files are detected!" + bcolors.ENDC)
        print(bcolors.WARNING + corrupted_imgs + bcolors.ENDC)
        
        output = os.path.join(os.path.abspath(args.output_path), "corrupted_imgs_list.txt")
        
        if args.nosave == False:
            print(f"Corrupted image file list is saved to {output}")
            with open(output, mode="w", encoding="UTF-8") as f:
                f.write(corrupted_imgs + "\n")

if __name__ == "__main__":
    main()