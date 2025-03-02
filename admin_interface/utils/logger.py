import logging
import os
from datetime import datetime


def setup_logger():
    logger = logging.getLogger('admin_interface')
    logger.setLevel(logging.INFO)

    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # File handler
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # Create file handler with current date in filename
    current_date = datetime.now().strftime('%Y-%m-%d')
    file_handler = logging.FileHandler(f'logs/admin_interface_{current_date}.log')
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger


logger = setup_logger()
