# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

####Import in Libraries
#
from reportlab.pdfgen import canvas
#
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
#
from reportlab.platypus import Image
#
from reportlab.lib.units import cm

####Canvas stuff
canvas = canvas.Canvas("jonsTestForm.pdf", pagesize=letter)
#
canvas.setLineWidth(.3)
#
canvas.setFont('Helvetica', 12)

####Header Info
#
##Lab the Data is From
canvas.drawString(30,750,'Cascade Meteorite Lab')
canvas.drawString(30,735,'Scanning Electron Microscope Analysis')
#
##Info on the image
#
canvas.drawString(300,750, "Backscatter Electron Image from " + "CML0615(13)")
canvas.line(280,747,580,747)
#
canvas.drawString(400,730, "Created by " + "Jon Barnes")
canvas.line(380,727,580,727)
#
canvas.drawString(400,710, "Created on " + "June 18 2014")
canvas.line(380,707,580,707)
#

##Save the Page, make new page
canvas.showPage()
print 'writing page 1'

#### BSE Tiff Image
#Image of BSE Tiff
bseTif = '/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif'
canvas.drawImage(bseTif, 50, 400, width=10*cm, height=10*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,400, "BSE Image of CML0615(13)")

#### BSE Tiff Image Histogram
#Image of BSE Histogram
bseHist = '/home/jon/Desktop/BSE Tiff Histogram, first and last 3 removed.png'
canvas.drawImage(bseHist, 50, 200, width=7*cm, height=7*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,200, "BSE Histogram from CML0615(13)")

##Save the Page, make new page
canvas.showPage()
print 'writing page 2'


#### BSE Cropped Image
#Image of BSE Tiff cropped
bseContour = '/home/jon/Desktop/cropped bse image.png'
canvas.drawImage(bseContour, 50, 500, width=10*cm, height=10*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,500, "BSE Image subsection of CML0615(13)")

#### BSE Tiff Contours
#Image of BSE Tiff
bseContour = '/home/jon/Desktop/testContour.png'
canvas.drawImage(bseContour, 50, 300, width=10*cm, height=10*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,300, "BSE Image Contours for subsection of CML0615(13)")

#### BSE Tiff BSE Mineral Heat Map
#Image of BSE Mineral Heat Map
bseMineralShade = '/home/jon/Desktop/testShade.png'
canvas.drawImage(bseMineralShade, 50, 100, width=7*cm, height=7*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,100, "BSE Shaded map from subsection of CML0615(13)")

##Save the Page, make new page
canvas.showPage()
print 'writing page 3'

####Save the PDF
canvas.save()

# <codecell>


