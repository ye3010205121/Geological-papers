#from __future__ import division
#from skimage import io
#import numpy as np
from PIL import Image
from keras.preprocessing import image
import glob


#datagen = image.ImageDataGenerator(fill_mode='wrap', zoom_range=[4, 4])



#datagen = image.ImageDataGenerator(rotation_range=90)

#datagen = image.ImageDataGenerator(channel_shift_range=10)

datagen = image.ImageDataGenerator(shear_range=10)

#datagen = image.ImageDataGenerator(horizontal_flip=True)

#datagen = image.ImageDataGenerator(vertical_flip=True)


#datagen = image.ImageDataGenerator(rotation_range=30, shear_range=0.5, horizontal_flip=True, vertical_flip=True)


gen_data = datagen.flow_from_directory('/home/yezhang/keras-image-data-augmentation-master/1', 
                                       batch_size=1, 
                                       shuffle=False, 
                                       save_to_dir='/home/yezhang/keras-image-data-augmentation-master/2',
                                       save_prefix='gen',
									   target_size=(247, 400))


for i in range(2):
    gen_data.next()
    


