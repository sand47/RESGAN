import matplotlib.pyplot as plt

filepath = 'loss_log.txt'

epoch,G_GAN,G_L1,D_real,D_fake,lineBuff= [],[],[],[],[],[]


with open(filepath) as fp:
   line = fp.readline()
   prev_epoch = 1
   while line:
       
       flag = line.strip()
         
       if flag[0]=="=":
        pass
       
       else:
        curr_epoch = int(flag[8:11].replace(",",""))
        lineBuff.append(flag)   
        if curr_epoch!=prev_epoch:
          prev_epoch = curr_epoch
          
          flag = lineBuff[-2]
          print(flag)
          ind = flag.find('G_GAN')
          l1 = flag.find('G_L1')
          dreal = flag.find('D_real')
          dfake = flag.find('D_fake')
        
          G_GAN.append(float(flag[ind+7:ind+12]))
          G_L1.append(float(flag[l1+6:l1+12]))
          D_real.append(float(flag[dreal+7:dreal+13]))
          D_fake.append(float(flag[dfake+7:dfake+13]))

        else:
          pass
 
      
       line = fp.readline()


epoch_count = range(1, len(G_L1) + 1)

fig, ax = plt.subplots(1,1) 
ax.plot(epoch_count,G_L1,'C1',label='G_L1')
ax.plot(epoch_count,G_GAN,'b',label='G_GAN')
ax.plot(epoch_count,D_fake,'r',label='D_Fake')
ax.plot(epoch_count,D_real,'g', label='D_REAL')
plt.legend(loc='best')
plt.show()
