from matplotlib import pyplot as plt
from pydicom import dcmread

#  Read the DICOM file
dicom_data = dcmread('datas/MRBRAIN.DCM')

# Access and print the metadata
print("DICOM Metadata:")
print(f"Patient Name: {dicom_data.PatientName}")
print(f"Patient ID: {dicom_data.PatientID}")
print(f"Modality: {dicom_data.Modality}")
print(f"Image Type: {dicom_data.ImageType}")

#Accessing metadata using their tags
# https://www.dicomlibrary.com/dicom/dicom-tags/

# Access the image type metadata using the tag (0008, 0008)
image_type = dicom_data[(0x0008, 0x0008)].value
# Print the image type metadata
print("Image Type:", image_type)

physician_name = dicom_data[(0x0008, 0x0090)].value
print("Physician's Name':", physician_name)

image_array = dicom_data.pixel_array
plt.imshow(image_array, cmap='gray')


## Let us enhance the image for visualization by normalizing pixel values
# between 0 and 1 and the performing histogram equalization
import numpy as np
import cv2
# Normalize the pixel values between 0 and 1
pixel_array = (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))

# Apply histogram equalization
pixel_array = np.uint8(255 * pixel_array)  # Convert back to uint8 for histogram equalization
pixel_array_eq = cv2.equalizeHist(pixel_array)

# Display the image
plt.imshow(pixel_array_eq, cmap='gray')
plt.axis('off')
plt.show()