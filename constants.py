"""
constants.py

Stores project constants.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_FOLDER = os.path.join(BASE_DIR, "dataset")

REPORT_FOLDER = os.path.join(BASE_DIR, "report")

LOG_FOLDER = os.path.join(BASE_DIR, "logs")

PROCESSED_FOLDER = os.path.join(BASE_DIR, "processed")

REPORT_FILE = os.path.join(REPORT_FOLDER, "report.txt")

LOG_FILE = os.path.join(LOG_FOLDER, "analyzer.log")

SUPPORTED_FORMATS = (
    ".jpg",
    ".jpeg",
    ".png"
)