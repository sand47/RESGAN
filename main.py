from snapImage import *
import pyautogui

def main():
    
    # while condition
    # take screenshot and crop the map
    env = snapImage()
    map_img = env.cropImage()

    # finding location of activity spots
    coordinate = env.location(map_img)
    print(coordinate)
    # clicking on the coordinates location
    #pyautogui.click(x=coordinate[0], y=coordinate[1])
    

if __name__ == "__main__":
    main()
