import os 
  
def main(): 
    i = 0
    foldername ="./cartoon/set8"
    for filename in os.listdir(foldername): 
        dst = str(i)+foldername + ".png"
        src =foldername+'/'+filename 
        dst =foldername+'/'+ dst 
        os.rename(src, dst) 
        i += 1
  

if __name__ == '__main__': 
      
    
    main() 
