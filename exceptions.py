"""
exceptions.py

Custom exception classes for Image Analyzer Project.
"""


class ImageAnalyzerError(Exception):
    """
    Base class for all project exceptions.
    """
    pass


class UnsupportedFormatError(ImageAnalyzerError):
    """
    Raised when an unsupported image format is found.
    """
    pass


class CorruptedImageError(ImageAnalyzerError):
    """
    Raised when an image cannot be opened.
    """
    pass


class EmptyDatasetError(ImageAnalyzerError):
    """
    Raised when the dataset folder has no images.
    """
    pass