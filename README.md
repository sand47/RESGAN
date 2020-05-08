# Modified Pix2Pix architecture for StarCraft video remastering in PyTorch

We would like to sincerly thank the authors of Pix2Pix for using their open-sourced source code in PyTorch. 

The Pix2Pix code was written by [Jun-Yan Zhu](https://github.com/junyanz) and [Taesung Park](https://github.com/taesung), and supported by [Tongzhou Wang](https://ssnl.github.io/).

Kindly refer, [original Pix2Pix page] (https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) for installtion of package. 

# Our Contribution 

## Data Preprocessing: 

The snapImage folder contains the automated python script to capture images while playing the game video from the StarCraft game and the images under unqiue name each time it is runned are stored in two folder named cartoon and SD. Once, we have these images collected over several video stored in the different set folder we can combine together these data by creating a two new subdirectories cartoon and SD folder inside the combineData folder. These subdirectories should each have their own subdirectories train, val, test, etc. In ./combineImage/cartoon/train, put training images. In ./combineImage/SD/train, put the corresponding images in style B. Repeat same for other data splits (val, test, etc).

Corresponding images in a pair {A,B} must be the same size and have the same filename, e.g., ./combineImage/cartoon/train/1.jpg is considered to correspond to /combineImage/SD/train/1.jpg.

Once the data is formatted this way, call:
```
python datasets/combine_A_and_B.py --fold_A ./combineImage/cartoon/train --fold_B ./combineImage/SD/train --fold_AB ./combineImage
```

## Training 

To train code use, 
```
python train.py --dataroot ./dataset/starcraft --name experimentname --model pix2pix --direction AtoB --no_flip --checkpoints_dir trained_model --netG resnet_9blocks --ngf 256 --no_dropout 
```
To test the model, 
```
python test.py --dataroot ./dataset/starcraft/ --model pix2pix --name experimentname.8  --ngf 256 --direction AtoB  --netG resnet_9blocks --checkpoints_dir trained_model --no_dropout 
```

`NOTE`: The research is still under work and the end to end model will be released soon. 
## Reference citation: 

@inproceedings{CycleGAN2017,
  title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networkss},
  author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  year={2017}
}
