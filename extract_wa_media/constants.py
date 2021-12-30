from enum import Enum
import re
import pathlib


class Constants:
    PKG_DIR = pathlib.Path(__file__).parent
    # two possible group pattern
    # 1. Chat with specific contact, e.g. `.../Media/972509166900@s.whatsapp.net/...`
    # 2. Chat with group, e.g. `.../Media/972549092412-1613907189@g.us/...`
    EXTRACT_GROUP_NAME_RE = re.compile(r"[/\\](\d+(-\d+)?@(s.whatsapp.net|g.us))[/\\]")
    # WA database constants
    GROUP_ID_KEY = "ZCONTACTJID"
    GROUP_NAME_KEY = "ZPARTNERNAME"
    GROUP_TO_ID_QUERY_FILE = "chat_id_to_name.sql"
    MESSAGE = "message"
    MEDIA = "media"
    CHAT_STORAGE_FILE = "ChatStorage.sqlite"
    DEFAULT_RELEVANT_EXTENSIONS = [".mp4"]
    OUTPUT_FOLDER_NAME = "extracted_WA_media"


class CLIConstants(Enum):
    CLI_DESCRIPTION = """
    A quick tool that makes it easy to extract all media from your iOS whatsapp database.
    This can be useful for merging media from an old backup into your current device.
    """
    WA_DATABASE_PATH = "db_path"
    OUTPUT_DIRECTORY = "output_directory"
    FILTERED_EXTENSIONS = "filtered_extensions"


class LoggerConstants:
    LOGGER_NAME = "logger"
