"""
logger.py

Configures logging for the Image Analyzer Project.
"""

import os
import logging
from constants import LOG_FOLDER, LOG_FILE

# Create logs folder automatically
os.makedirs(LOG_FOLDER, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="w"
)

# Logger object
logger = logging.getLogger("ImageAnalyzer")


def log_info(message):
    """
    Log information messages.
    """
    logger.info(message)


def log_warning(message):
    """
    Log warning messages.
    """
    logger.warning(message)


def log_error(message):
    """
    Log error messages.
    """
    logger.error(message)