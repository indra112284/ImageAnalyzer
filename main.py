"""
main.py

Entry point of the Image Dataset Analyzer Project.
"""

import os

from image_analyzer import DatasetAnalyzer
from report_generator import ReportGenerator
from constants import DATASET_FOLDER, REPORT_FILE
from logger import log_info, log_error


def main():

    print("=" * 60)
    print("        IMAGE DATASET ANALYZER")
    print("=" * 60)

    log_info("Project Started")

    # Check dataset folder
    if not os.path.exists(DATASET_FOLDER):

        print("\nDataset folder not found!")

        print(f"Expected Path : {DATASET_FOLDER}")

        log_error("Dataset folder not found.")

        return

    try:

        # Analyze Images
        analyzer = DatasetAnalyzer(DATASET_FOLDER)

        report_data = analyzer.analyze()

        # Generate Report
        report = ReportGenerator()

        report.generate(report_data)

        # Display Summary
        print("\nAnalysis Completed Successfully!\n")

        print(f"Total Files      : {report_data['total_files']}")
        print(f"Valid Images     : {report_data['valid_images']}")
        print(f"Invalid Images   : {report_data['invalid_images']}")

        print("\nImage Format Summary")
        print("-" * 30)

        if report_data["format_count"]:

            for image_format, count in report_data["format_count"].items():

                print(f"{image_format:<10} : {count}")

        else:

            print("No valid images found.")

        print("\nReport Saved At")

        print(REPORT_FILE)

        print("\nProject Completed Successfully.")

        log_info("Project Completed Successfully")

    except Exception as error:

        print("\nUnexpected Error")

        print(error)

        log_error(str(error))


if __name__ == "__main__":
    main()