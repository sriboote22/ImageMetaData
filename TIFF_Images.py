import tifffile

######## Print all metadata associated with an image ######
# Open the TIFF file
with tifffile.TiffFile('datas/autumn.tif') as tiff:
    # Get the metadata
    metadata = tiff.pages[0].tags

    # Print all the metadata fields
    for tag in metadata.values():
        print(tag.name, tag.value)


### Now, let us extract some metadata and print ####
#First let us see what type of informationis stored in the tiff file.
#Print all attributes stored as part of the tiff_image.pages[0] attribute
tiff_image = tifffile.TiffFile('datas/at3_1m4_03.tif')
# Also try mito-0.2um_pixel.tif and Ti64.10X.tif
# mito-0.2um_pixel.tif has been modified in imageJ.
attributes = dir(tiff_image.pages[0])
print(attributes)

#If the image has been modified in imageJ then imagej_metadata exists
print("Does this image have imageJ metadata? ", tiff_image.is_imagej)
print(tiff_image.imagej_metadata)
# Extract the pixel size information
if tiff_image.imagej_metadata is not None:
    pixel_width = tiff_image.imagej_metadata.get("spacing_x", 1.0)  # Default to 1.0 if not found
    pixel_height = tiff_image.imagej_metadata.get("spacing_y", 1.0)
    print("Pixel spacing in x and y is: ", pixel_width, pixel_height)


#We can also use specific information using its respective tag identifier
# https://www.loc.gov/preservation/digital/formats/content/tiff_tags.shtml


#Let us extract and print some metadata
def extract_tiff_metadata(tiff_path):
    # Open the TIFF image
    tiff_image = tifffile.TiffFile(tiff_path)

    # Extract the image dimensions
    width, height, channels = tiff_image.pages[0].shape  #Shape depends on the image type

    # Extract the color space information
    color_space = tiff_image.pages[0].photometric

    # Extract the bit depth
    bit_depth = tiff_image.pages[0].bitspersample

    # Extract the compression method
    compression = tiff_image.pages[0].compression

    # Extract the image acquisition date and time
    acquisition_date = tiff_image.pages[0].tags.get(306)

    # Extract the image description
    description = tiff_image.pages[0].description

    # Extract the software used
    software = tiff_image.pages[0].software

    # Extract the resolution
    resolution = tiff_image.pages[0].tags.get(282)

    # Extract the camera or device information
    device_info = tiff_image.pages[0].tags.get(271)

    # Extract the GPS coordinates
    gps_info = tiff_image.pages[0].tags.get(34853)

    # Close the TIFF image
    tiff_image.close()

    # Return the extracted metadata
    metadata = {
        'width': width,
        'height': height,
        'color_space': color_space,
        'bit_depth': bit_depth,
        'compression': compression,
        'acquisition_date': acquisition_date,
        'description': description,
        'software': software,
        'resolution': resolution,
        'device_info': device_info,
        'gps_info': gps_info
    }
    return metadata

# Example usage
#tiff_path = 'mito.tif'
tiff_path = 'datas/leaves.tif'
metadata = extract_tiff_metadata(tiff_path)

# Print the extracted metadata
for key, value in metadata.items():
    print(f'{key}: {value}')