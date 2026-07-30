"""
image_utils.py

Utility functions for extracting image information.
"""

import os


def get_image_name(image_path):
    """
    Returns the image file name.
    """
    return os.path.basename(image_path)


def get_image_format(image):
    """
    Returns image format.
    """
    return image.format


def get_image_mode(image):
    """
    Returns image mode (RGB, L, RGBA, etc.).
    """
    return image.mode


def get_image_width(image):
    """
    Returns image width.
    """
    return image.width


def get_image_height(image):
    """
    Returns image height.
    """
    return image.height


def get_resolution(image):
    """
    Returns image resolution.
    """
    return image.size


def get_total_pixels(image):
    """
    Returns total number of pixels.
    """
    return image.width * image.height


def get_aspect_ratio(image):
    """
    Returns aspect ratio rounded to 2 decimal places.
    """
    return round(image.width / image.height, 2)


def get_file_size(image_path):
    """
    Returns image size in KB.
    """
    size = os.path.getsize(image_path)
    return round(size / 1024, 2)


def analyze_image(image, image_path):
    """
    Collect all image details in a dictionary.
    """

    return {
        "Image Name": get_image_name(image_path),
        "Format": get_image_format(image),
        "Mode": get_image_mode(image),
        "Width": get_image_width(image),
        "Height": get_image_height(image),
        "Resolution": get_resolution(image),
        "Total Pixels": get_total_pixels(image),
        "Aspect Ratio": get_aspect_ratio(image),
        "File Size (KB)": get_file_size(image_path)
    }