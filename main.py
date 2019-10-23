from snapImage import *
#import location
import pyautogui

def main():
    
    # take screenshot and crop the map
    sys = snapImage()
    #img = sys.cropImage()
    
    coordinate = sys.test_center_coordinate()
    
    # finding location of activity spots
    #coordinate = sys.location(img)
    print(coordinate)
    
    # clicking on the coordinates location
    #pyautogui.click(x=coordinate[0], y=coordinate[1])
    

if __name__ == "__main__":
    main()
