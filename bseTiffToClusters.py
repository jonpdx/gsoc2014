# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

# Import Libraries
import time as time
import numpy as np
import scipy as sp
import pylab as pl
import Image
#
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import Ward


# Get SEM BSE Tiff Data
tiffFile = ('/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif')
im = Image.open(tiffFile)
im.show()


# Get SEM Data
#
#get the file path
#tifPath = '/home/jon/Desktop/gsoc2014/semImages/'
#tifFile = 'CML0615(13).tif'
#tifPathAndFile = tifPath + tifFile
#
#import in the tif
#imFull = Image.open(tifPathAndFile)
#imFull.show()

imFull  = Image.open(tiffFile)

[xmax, ymax] = imFull.size
print xmax
print ymax

#crop the tiff
#x1, y1, x2, y2
#starts in bottom left corner and works to upper right corner
#for starts x1 = 0 , y1 = 0  END xN = max, yN = max
#while x < xmax , while y < ymax ; increase x by 250, increase y by 250 For roughly 50 images
x1 = 0
y1 = 0
x2 = 250
y2 = 250
box=(x1, y1, x2, y2)
#
im_crop=imFull.crop(box)
#
im_crop.show()

#reassign im
im = im_crop
imarray = np.array(im)

# Convert Tif into "LENA"
lena = im

X = np.reshape(lena, (-1, 1))

# Define the structure A of the data. Pixels connected to their neighbors.
connectivity = grid_to_graph(*imarray.shape)

# Compute clustering
print "Compute structured hierarchical clustering..."
#
st = time.time()
#
n_clusters = 100  # number of regions
#
ward = Ward(n_clusters=n_clusters, connectivity=connectivity).fit(X)
label = np.reshape(ward.labels_, imarray.shape)

# Path names for images
#
#saved file path
figurePath = '/home/jon/Desktop/'
#saved file ext
figureExt = '.png'

############
# Plot the crop bse image
pl.figure(figsize=(5, 5))
pl.imshow(lena, cmap=pl.cm.gray)
#
pl.xticks(())
pl.yticks(())
#
#saved file name
figureNameContour = 'cropped bse image'
#
#saved path and file and ext
figurePathNameContourExt = figurePath + figureNameContour + figureExt
#
pl.savefig(figurePathNameContourExt)
#
pl.show()
###########


##############
# Plot the contour results of image
pl.figure(figsize=(5, 5))
pl.imshow(lena, cmap=pl.cm.gray)
#
for l in range(n_clusters):
    pl.contour(label == l, contours=1,
            colors=[pl.cm.spectral(l / float(n_clusters)), ])
#
pl.xticks(())
pl.yticks(())
#
#saved file name
figureNameContour = 'testContour'
#
#saved path and file and ext
figurePathNameContourExt = figurePath + figureNameContour + figureExt
#
pl.savefig(figurePathNameContourExt)
#
pl.show()


######

# Plot the reasign grain results of image
pl.figure(figsize=(5, 5))
pl.imshow(label, cmap=pl.cm.gray)
#
pl.xticks(())
pl.yticks(())
#
#saved file name
figureNameShade = 'testShade'
#
#saved path and file and ext
figurePathNameShadeExt = figurePath + figureNameShade + figureExt
#
pl.savefig(figurePathNameShadeExt)
pl.show()

# <codecell>


