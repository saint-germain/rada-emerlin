import numpy as np
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
path = 'mock test/'
files = np.array([f for f in glob.glob(path + "*.png", recursive=True)])
df=pd.read_csv("custom_screen_guide.csv")
CSlist=np.unique(df.CustomScr)
for CS in CSlist:
    imlist=df.PlotRef[df.CustomScr==CS]
    plfiles=[]
    for i in imlist:
        plfiles+=[files[np.array([str(i) in file for file in files])][0]]
    if len(imlist)==4:
        im1=np.hstack((mpimg.imread(plfiles[0]),mpimg.imread(plfiles[1])))
        im2=np.hstack((mpimg.imread(plfiles[2]),mpimg.imread(plfiles[3])))
        imag=np.vstack((im1,im2))
        plt.imsave(path+CS+'.png',imag,format='png')
    if len(imlist)==1:
        imag=mpimg.imread(plfiles[0])
        plt.imsave(path+CS+'.png',imag,format='png')
