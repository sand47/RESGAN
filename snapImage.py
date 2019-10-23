import cv2
import pyautogui
import numpy as np
import random

class snapImage:

    def __init__(self):
        self.id = 0
        self.keyCoordinate =[]
    
    def cropImage(self):

        # take screenshot
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite("screenshot/screenshot"+str(self.id)+".png",image)
        
        # crop image using the below coordinates
        r0 = 286;r1 = 814;r2 = 221;r3 = 223
        map_img = image[r1:r1+r3, r0:r0+r2]
       
        #save map_imgs if needed 
        cv2.imwrite("crop/crop_test"+str(self.id)+".png",map_img)
        self.id+=1
        
        return map_img

    def find_contour(self,mask):
        '''
        Appends the first coordinate of a contours to key Coordinate list. A contours has a list of coordinates which contours the object
        Thus we can pick the first coordinate.

        '''
        ret,thresh = cv2.threshold(mask, 40, 255, 0)
        contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       
        for i in range(len(contours)):
            cntx = contours[i][0]
            pt = (cntx[0][0],cntx[0][1])
            self.keyCoordinate.append(pt)
        
 
    def location(self,img):
        '''
        Finds the coordinate of active locations of  AI vs AI mode players using the color
        of the player which is predefined.We first mask the map using given color and find the
        coordinates and append it to the keyCoordinate list and return a random index.

        '''

        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # human player mask
        #pink_lower = np.array([142,192,200])
        #pink_upper = np.array([162,212,280])
        #pink_mask = cv2.inRange(img, pink_lower,pink_upper)
        #self.find_contour(pink_mask)

        # AI player 1 
        yellow_lower  = np.array([20,188,206])
        yellow_upper = np.array([40,208,286])
        yellow_mask = cv2.inRange(img, yellow_lower,yellow_upper)
        self.find_contour(yellow_mask)

        # AI player 2 
        red_lower = np.array([-10,235,164])
        red_upper = np.array([10,255,244])
        red_mask = cv2.inRange(img, red_lower,red_upper)
        self.find_contour(red_mask)
               
        return random.choice(self.keyCoordinate)

    def display(self,image):
        cv2.imshow("Image", image)
        cv2.waitKey(0) # waits until a key is pressed
        cv2.destroyAllWindows() # destroys the window showing image


       
    def test_center_coordinate(self,image):
       
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

        return coord
     
