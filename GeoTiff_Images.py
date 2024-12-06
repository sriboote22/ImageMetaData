import rasterio

from rasterio.plot import show
from matplotlib import pyplot as plt


img = rasterio.open('datas/geo.tif')
show(img)

#To find out number of bands in an image
num_bands = img.count
print("Number of bands in the image = ", num_bands)

img_band1 = img.read(1) #1 stands for 1st band.

band_number=1
with rasterio.open('datas/geo.tif') as src:
    print(src.tags(band_number))


#To find out the coordinate reference system
print("Coordinate reference system: ", img.crs)

# Read metadata
metadata = img.meta
print('Metadata: {metadata}\n'.format(metadata=metadata))

#Read description, if any
desc = img.descriptions
print('Raster description: {desc}\n'.format(desc=desc))

#To find out geo transform
print("Geotransform : ", img.transform)