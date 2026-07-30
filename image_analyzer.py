"""
image_analyzer.py

Analyzes all images inside the dataset folder.
"""

import os

from image_handler import ImageHandler
from logger import log_info, log_error
from exceptions import EmptyDatasetError


class DatasetAnalyzer:
    """
    Analyze all images present in the dataset folder.
    """

    def __init__(self, dataset_path):

        self.dataset_path = dataset_path
        self.handler = ImageHandler()

        self.results = []

        self.total_files = 0
        self.valid_images = 0
        self.invalid_images = 0

        self.format_count = {}

    def analyze(self):
        """
        Analyze every image in the dataset folder.
        """

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(
                f"Dataset folder not found : {self.dataset_path}"
            )

        files = os.listdir(self.dataset_path)

        if len(files) == 0:
            raise EmptyDatasetError(
                "Dataset folder is empty."
            )

        log_info("Dataset Analysis Started")

        for file_name in files:

            file_path = os.path.join(
                self.dataset_path,
                file_name
            )

            if os.path.isdir(file_path):
                continue

            self.total_files += 1

            try:

                image_info = self.handler.read_image(file_path)

                self.results.append(image_info)

                self.valid_images += 1

                image_format = image_info["Format"]

                self.format_count[image_format] = (
                    self.format_count.get(image_format, 0) + 1
                )

            except Exception as error:

                log_error(str(error))

                self.invalid_images += 1

        log_info("Dataset Analysis Completed")

        return {

            "total_files": self.total_files,

            "valid_images": self.valid_images,

            "invalid_images": self.invalid_images,

            "format_count": self.format_count,

            "images": self.results

        }