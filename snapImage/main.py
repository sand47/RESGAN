from snapImage import *
import pyautogui
import time
import argparse
import os
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folderName', required=True, help='path to image')
    args = parser.parse_args()
    os.mkdir("./cantoon/"+str(args.folderName))
    os.mkdir("./SD/"+str(args.folderName))
    sys = snapImage(args.folderName)
    # time to switch over to game console
    time.sleep(4)
    while True:

        # take screenshot and crop the map
        img = sys.cropImage()
        
        # finding location of key spots
        coordinate = sys.location(img)
      
        # clicking on the coordinates location
        # (286,814) are added so that we map to original coordinate
        # from the cropped image 
        pyautogui.click(x=coordinate[0]+286,y=coordinate[1]+814)

        # Take images both SD and cantoon every one second
        sys.dataCollection()
       

if __name__ == "__main__":
    main()
