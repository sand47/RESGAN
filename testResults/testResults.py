import os
from PIL import Image
import numpy as np
import pandas as pd
    
def DeleteRealA():
    
    for root, dirs, files in os.walk("images/"):
        for filename in files:
           if filename[-10:] =="real_A.png":
                removefile = "images/"+filename
                os.remove(removefile)
                
def GetData():
    
    fake = []
    real =[]
    for root, dirs, files in os.walk("images/"):
        for filename in files:
            
            if filename[-10:] =="fake_B.png":
                fake.append("images/"+filename)
             
            if filename[-10:] =="real_B.png":
                real.append("images/"+filename)

    return fake,real

def FindL1(fake,real):

    l1 =[]
    filename =[]
    for i in range(len(fake)):
        
        a=np.array(Image.open(fake[i]).convert('RGB')).ravel()
        b=np.array(Image.open(real[i]).convert('RGB')).ravel()

        # Calculate the sum of the absolute differences divided by number of elements
        MAE = np.sum(np.abs(np.subtract(a,b,dtype=np.float))) / a.shape[0]
        filename.append([fake[i][7:],real[i][7:]])
        l1.append(MAE)

    return filename,l1

def SaveToExcel(filename,l1):
    df = pd.DataFrame.from_dict({'L1 loss':l1,'FileName':filename})
    df.to_excel('testResult.xlsx',header= True,index =False)
    

if __name__=="__main__":
    DeleteRealA()
    fake,real = GetData()
    filename,l1 = FindL1(fake,real)
    SaveToExcel(filename,l1)
    
    
    
    
