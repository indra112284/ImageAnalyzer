"""
report_generator.py

Generates the analysis report.
"""

import os

from constants import REPORT_FOLDER, REPORT_FILE
from logger import log_info


class ReportGenerator:
    """
    Generates report.txt containing image details and summary.
    """

    def __init__(self):

        os.makedirs(REPORT_FOLDER, exist_ok=True)

    def generate(self, report_data):
        """
        Generate report file.
        """

        with open(REPORT_FILE, "w") as file:

            file.write("=" * 60 + "\n")
            file.write("           IMAGE DATASET ANALYZER REPORT\n")
            file.write("=" * 60 + "\n\n")

            file.write("IMAGE DETAILS\n")
            file.write("-" * 60 + "\n\n")

            # Write details of every image
            for image in report_data["images"]:

                file.write(f"Image Name      : {image['Image Name']}\n")
                file.write(f"Format          : {image['Format']}\n")
                file.write(f"Mode            : {image['Mode']}\n")
                file.write(f"Width           : {image['Width']}\n")
                file.write(f"Height          : {image['Height']}\n")
                file.write(f"Resolution      : {image['Resolution']}\n")
                file.write(f"Total Pixels    : {image['Total Pixels']}\n")
                file.write(f"Aspect Ratio    : {image['Aspect Ratio']}\n")
                file.write(f"File Size (KB)  : {image['File Size (KB)']}\n")
                file.write(f"Grayscale Image : {image['Grayscale Image']}\n")

                file.write("-" * 60 + "\n")

            # Summary
            file.write("\n")
            file.write("=" * 60 + "\n")
            file.write("SUMMARY\n")
            file.write("=" * 60 + "\n")

            file.write(f"Total Files      : {report_data['total_files']}\n")
            file.write(f"Valid Images     : {report_data['valid_images']}\n")
            file.write(f"Invalid Images   : {report_data['invalid_images']}\n\n")

            file.write("FORMAT COUNT\n")
            file.write("-" * 60 + "\n")

            if report_data["format_count"]:

                for image_format, count in report_data["format_count"].items():

                    file.write(f"{image_format:<10} : {count}\n")

            else:

                file.write("No valid images found.\n")

            file.write("=" * 60 + "\n")

        log_info("Report generated successfully.")