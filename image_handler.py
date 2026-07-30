"""
image_handler.py

Handles image reading and processing.
"""

import os
from PIL import Image

from base_imagehandler import BaseImageHandler
from constants import SUPPORTED_FORMATS, PROCESSED_FOLDER
from exceptions import (
    UnsupportedFormatError,
    CorruptedImageError
)
from logger import log_info, log_error
from image_utils import analyze_image


class ImageHandler(BaseImageHandler):
    """
    Child class that inherits from BaseImageHandler.
    """

    def __init__(self):
        super().__init__()
        os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    def validate_image(self, image_path):
        """
        Check whether image format is supported.
        Overrides the parent class method.
        """

        extension = os.path.splitext(image_path)[1].lower()

        if extension not in SUPPORTED_FORMATS:
            raise UnsupportedFormatError(
                f"Unsupported image format: {extension}"
            )

    def read_image(self, image_path):
        """
        Open image, convert to grayscale,
        save grayscale image,
        and return image details.
        """

        self.validate_image(image_path)

        try:

            image = Image.open(image_path)

            image_info = analyze_image(image, image_path)

            grayscale = image.convert("L")

            output_path = os.path.join(
                PROCESSED_FOLDER,
                os.path.basename(image_path)
            )

            grayscale.save(output_path)

            image_info["Grayscale Image"] = output_path

            log_info(f"Processed : {image_info['Image Name']}")

            return image_info

        except Exception:

            log_error(f"Corrupted Image : {image_path}")

            raise CorruptedImageError(
                f"Unable to open image : {image_path}"
            )