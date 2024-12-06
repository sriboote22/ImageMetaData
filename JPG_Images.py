from PIL import Image

# Open the image
image = Image.open('datas/1.JPG')

# Extract the EXIF metadata
exif_data = image.getexif()

# Print the EXIF metadata
for tag, value in exif_data.items():
    print(f"{tag}: {value}")


import PIL.ExifTags
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in image._getexif().items()
    if k in PIL.ExifTags.TAGS
}