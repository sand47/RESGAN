import matplotlib.pyplot as plt

filepath = 'loss_log.txt'
epoch = []
G_GAN = []
G_L1 = []
D_real = []
D_fake = []

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       flag = line.strip()
       if cnt>1:
           ind = flag.find('G_GAN')
           l1 = flag.find('G_L1')
           dreal = flag.find('D_real')
           dfake = flag.find('D_fake')
           G_GAN.append(float(flag[ind+7:ind+12]))
           G_L1.append(float(flag[l1+6:l1+12]))
           D_real.append(float(flag[dreal+7:dreal+13]))
           D_fake.append(float(flag[dfake+7:dfake+13]))

       cnt += 1
       line = fp.readline()


x_ticks_labels = [0,10,20,30,40,50]

fig, ax = plt.subplots(1,1) 

ax.plot(G_L1,'C1',label='G_L1')
ax.plot(G_GAN,'b',label='G_GAN')
ax.plot(D_fake,'r',label='D_Fake')
ax.plot(D_real,'g', label='D_REAL')

ax.set_xticklabels(x_ticks_labels, rotation='vertical', fontsize=18)

plt.legend(loc='best')
plt.show()


# (epoch: 21, iters: 960, time: 0.107, data: 0.000) G_GAN: 3.792 G_L1: 6.567 D_real: 0.014 D_fake: 0.079

