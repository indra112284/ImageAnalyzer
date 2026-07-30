"""
base_image_handler.py

Parent class for image handling.
This class demonstrates Inheritance.
"""


class BaseImageHandler:
    """
    Parent class for all image handlers.
    """

    def __init__(self):
        print("BaseImageHandler initialized")

    def validate_image(self, image_path):
        """
        Base validation method.

        Child classes should override this method.
        """
        raise NotImplementedError(
            "Child class must implement validate_image()."
        )