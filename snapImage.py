import time
import cv2
import pyautogui
import numpy as np
from os import walk

class snapImage:
    def __init__(self):
        #pass
        self.i = 0 
        self.test = 0 
        
    def cropImage(self):

        # take screenshot
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite("screenshot/img"+str(self.i)+".png",map_img)
        # crop location from these below coordinates
        r0 = 288;r1 = 812;r2 = 218;r3 = 224
        map_img = image[r1:r1+r3, r0:r0+r2]

        #save map_imgs if needed 
        cv2.imwrite("crop/crop_test"+str(self.i)+".png",map_img)
        time.sleep(1)
        self.i+=1
        
        return map_img

    def location(self,image):
       
        # find red,blue,green locatons
        
        lower_red = np.array([0,0,220])  # BGR-code of your lowest red
        upper_red = np.array([10,10,255])   # BGR-code of your highest red
        mask = cv2.inRange(image, lower_red, upper_red) 
        #mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255)) for Green 
        #blue_lower=np.array([150,150,0],np.uint8)
        #blue_upper=np.array([180,255,255],np.uint8)
        #mask = cv2.inRange(image, blue_lower, blue_upper) 

        #get all non zero values
        coord=cv2.findNonZero(mask)
        #print(coord)

        # add condition to find important coordinates


        return coord
    def test(self,path):
        #path = "screenshot/"
        for (dirpath, dirnames, filenames) in walk(mypath):
            for f in filenames:
                image = cv2.imread(path+f)
                r0 = 286;r1 = 814;r2 = 221;r3 = 223
                crop = pre_image[r1:r1+r3, r0:r0+r2]
                cv2.imwrite("test/crop_test"+str(p)+".png",crop)
                self.test +=1

    def display(self,image):
        cv2.imshow("Image", image)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows() # destroys the window showing image

