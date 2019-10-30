import cv2
import pyautogui
import numpy as np
import random
import time


class snapImage:

    def __init__(self):
        self.id = 0
        self.idHD = 0 
        self.keyCoordinate =[]

        # hide chat in replay
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        time.sleep(2)
    
    def cropImage(self):

        # take screenshot
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
       
        # crop image using the below coordinates
        r0 = 286;r1 = 814;r2 = 221;r3 = 223
        map_img = image[r1:r1+r3, r0:r0+r2]
                 
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
        #yellow_lower  = np.array([20,188,206])
        #yellow_upper = np.array([40,208,286])
        #yellow_mask = cv2.inRange(img, yellow_lower,yellow_upper)
        #self.find_contour(yellow_mask)# [ -1 199  72] [ 19 219 152]
        # purple [134 140 116] [154 160 196]
        
        #brown_lower  = np.array([-1,199,72])
        #brown_upper = np.array([19,219,152])
        #brown_mask = cv2.inRange(img, brown_lower,brown_upper)
        #self.find_contour(brown_mask)

        #purple_lower  = np.array([134,140,116])
        #purple_upper = np.array([154,160,196])
        #purple_mask = cv2.inRange(img, purple_lower,purple_upper)
        #self.find_contour(purple_mask)

        green_lower  = np.array([73,182,140])
        green_upper = np.array([93,203,220])
        green_mask = cv2.inRange(img, green_lower,green_upper)
        self.find_contour(green_mask)

        blue_lower  = np.array([101,230,164])
        blue_upper = np.array([121,250,244])
        blue_mask = cv2.inRange(img, blue_lower,blue_upper)
        self.find_contour(blue_mask)
        
        #orange_lower  = np.array([6,224,208])
        #orange_upper = np.array([26,244,288])
        #orange_mask = cv2.inRange(img, orange_lower,orange_upper)
        #self.find_contour(orange_mask)


        # AI player 2
        #white_lower = np.array([56,13,184])
        #white_upper = np.array([76,33,264])
        #white_mask = cv2.inRange(img, white_lower,white_upper)
        #self.find_contour(white_mask)
        
        #red_lower = np.array([-10,235,164])
        #red_upper = np.array([10,255,244])
        #red_mask = cv2.inRange(img, red_lower,red_upper)
        #self.find_contour(red_mask)
               
        return random.choice(self.keyCoordinate)
    
    def keyPress(self):
        pyautogui.press('f5')
        pyautogui.press('f5')
        
        
        
    def dataCollection(self):

        #time.sleep(1)
        # pass the game in SD
        pyautogui.click(x=1345 ,y=1000)
        self.keyPress()
               
        self.keyPress() #To change to SD
                
        # take game in SD domain
        imageSD = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(imageSD), cv2.COLOR_RGB2BGR)
        r0 = 320;r1 = 5;r2 = 1200;r3 = 759
        SD_image = image[r1:r1+r3, r0:r0+r2]
        cv2.imwrite("SD/"+str(self.idHD)+".png",SD_image)
        time.sleep(1)

        # Press key to change to cantoon 
        pyautogui.press('f5')
        
        time.sleep(1)
        # take image of cantoon
        imageCAN = pyautogui.screenshot()
        imageCAN = cv2.cvtColor(np.array(imageCAN), cv2.COLOR_RGB2BGR)
        r0 = 320;r1 = 5;r2 = 1200;r3 = 759
        Cantoon_image = imageCAN[r1:r1+r3, r0:r0+r2]
        cv2.imwrite("cantoon/"+str(self.idHD)+".png",Cantoon_image)
        self.idHD +=1
        time.sleep(1)
        pyautogui.press('f5')
        # get back to SD    
       # self.keyPress()
        time.sleep(1)    

        # play the game in SD
        pyautogui.click(x=1345 ,y=1000)
        time.sleep(1)
               
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
     
