import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    foldername ="set8"
    for filename in os.listdir(foldername): 
        dst = str(i)+foldername + ".png"
        src =foldername+'/'+filename 
        dst =foldername+'/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
