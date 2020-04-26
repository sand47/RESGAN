from helper import * 

testPath = "testimage/"
trainPath = "trainimage/"

def main():

    #test loss
    DeleteRealA(testPath)
    fake,real = GetData(testPath)
    filename,test_loss = FindL1(fake,real)
    print("Avg. test loss \t ")
    print(sum(test_loss)/len(test_loss))
    SaveToExcel(filename,test_loss)

    # train loss
    DeleteRealA(trainPath)
    trainloss() # plot the training loss 
    fake,real = GetData(trainPath)
    filename,train_loss = FindL1(fake,real)
    
    print("Avg. train_loss  \t ")
    print(sum(train_loss)/len(train_loss))

    #combined plot
    historPlot(train_loss,test_loss)

    # video to image -> pass it to trained model for inference
    #video()
    
    
if __name__=="__main__":

    main()

   
    
    
    
    
    
    
