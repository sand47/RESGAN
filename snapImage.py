import time
import cv2
import pyautogui
import numpy as np

class snapImage:
    def __init__(self):
        #pass
        self.i = 0 
        

    def cropImage(self):

        # take screenshot
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # crop location from these below coordinates
        r0 = 286;r1 = 814;r2 = 221;r3 = 223
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

    def test_center_coordinate(self):

        ## Read
        imgs = cv2.imread("test.png")
        cv2.imshow("Image", imgs)
        cv2.waitKey(0)
        img = cv2.cvtColor(imgs, cv2.COLOR_BGR2HSV)
       
        #blue_lower=np.array([83,243,209])
        #blue_upper=np.array([103,263,289]) #[ 83 243 209] [103 263 289]
        #mask = cv2.inRange(img, blue_lower, blue_upper)  # [ 50 229  88] [ 70 249 168]
        mask = cv2.inRange(img, (50, 229, 88), (70, 249,168))  #for Green 
        result = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Image", mask)
        cv2.waitKey(0)
        
        ret,thresh = cv2.threshold(mask, 40, 255, 0)
        contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
        coordinate = []
        #contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
        for i in range(len(contours)):
            cntx = contours[i][0]
            pt = (cntx[0][0],cntx[0][1])
            coordinate.append(pt)
            
        print(coordinate)    
                       
        if len(contours) != 0:
            #print(contours)
            # draw in blue the contours that were founded
            cv2.drawContours(result, contours, -1, 255, 3)
    
           
        # show the images
        cv2.imshow("Result", np.hstack([imgs, result]))
        cv2.waitKey(0)
    
        cv2.destroyAllWindows() # destroys the window showing image


    def display(self,image):
        cv2.imshow("Image", image)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows() # destroys the window showing image

