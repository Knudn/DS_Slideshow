from PIL import Image

img = Image.open('/share/Skjerm3/TopFuelStartlisteRun1.pdf.jpg')
img.show()
box = (0, 0, 1875, 1300)
img2 = img.crop(box)
img2.save('/share/Skjerm3/TopFuelStartlisteRun1_new_.pdf.jpg')
img2.show()

