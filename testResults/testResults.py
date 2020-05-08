from helper import * 

testPath = "testimage/"
trainPath = "trainimage/"

def main():

    #test loss
    DeleteRealA(testPath)
    fake,real = GetData(testPath)
    filename,test_loss = FindL1(fake,real)
    SaveToExcel(filename,test_loss)
    print("Avg. test loss \t ")
    print(sum(test_loss)/len(test_loss))
    # train loss
    DeleteRealA(trainPath)
    trainloss() # plot the training loss 
    fake,real = GetData(trainPath)
    filename,train_loss = FindL1(fake,real)
    #SaveToExcel(filename,train_loss)
    #test_loss =[]
    #combined plot
    print("Avg. train_loss  \t ")
    print(sum(train_loss)/len(train_loss))
    historPlot(train_loss,test_loss)

    # video to image -> pass it to trained model for inference
    #video()
    
    
if __name__=="__main__":

    main()

   
    
    
    
    
    
    
