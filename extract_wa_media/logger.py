import logging
import sys
# local modules
from extract_wa_media.constants import LoggerConstants


class Logger:
    @staticmethod
    def setup_logger() -> None:
        logger = logging.getLogger(LoggerConstants.LOGGER_NAME)
        logger_handler = logging.StreamHandler(sys.stdout)

        logger_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s]: %(filename)s{line: %(lineno)d} - %(message)s"
        )
        logger_handler.setFormatter(logger_formatter)
        logger.setLevel(logging.INFO)
        logger_handler.setLevel(logging.INFO)
        # set handler
        logger.addHandler(logger_handler)
