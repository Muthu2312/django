# your_app/utils.py

import cv2
import numpy as np
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

# your_app/utils.py

import cv2
import numpy as np
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

def process_image(image_file):
    # Read the image using OpenCV
    image_array = np.frombuffer(image_file.read(), np.uint8)
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Perform image processing (Example: convert to grayscale)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert the processed image back to Django ImageField format
    _, buffer = cv2.imencode('.jpg', gray_img)
    img_str = buffer.tobytes()
    
    # Use the original image file name and content type for the processed image
    processed_image_file = InMemoryUploadedFile(
        ContentFile(img_str),
        None,
        f'{image_file.name.split(".")[0]}_processed.jpg',
        'image/jpeg',
        len(img_str),
        None
    )

    return processed_image_file

