import cv2

vidcap = cv2.VideoCapture('starcraftOldVideo.mp4')
success,image = vidcap.read()

framecount = 0
framerate = 30
count = 0
success = True
# crop coordinates
r0 = 0;r1 = 0;r2 = 637;r3 = 315

#if img exist save every 2 seconds 
while success:

    framecount +=1
    success,image = vidcap.read()
    image = image[r1:r1+r3, r0:r0+r2]
    cv2.imwrite("ipimageall/ip%d.jpg" % count, image)     # save frame as jpg file
    count += 1
    '''
    if framecount ==(framerate*): # save every 2 seconds 
        image = image[r1:r1+r3, r0:r0+r2]
        cv2.imwrite("ipimages/ip%d.jpg" % count, image)     # save frame as jpg file
        count += 1
        framecount = 0 
   '''
    
