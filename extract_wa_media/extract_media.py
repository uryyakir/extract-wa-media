from typing import cast, Optional, List, NamedTuple, Union
import logging
import os
import sqlite3
import shutil
import pandas as pd
from functools import lru_cache
from tqdm import tqdm
# local modules
from extract_wa_media.constants import Constants, CLIConstants, LoggerConstants


logger = logging.getLogger(LoggerConstants.LOGGER_NAME)


class Video(NamedTuple):
    name: str
    file_path: str
    group_id: str
    group_name: str


class ExtractWAMedia:
    def __init__(self, **kwargs: Union[str, List[str]]) -> None:
        # parsing passed attributes
        self._db_path = cast(str, kwargs[CLIConstants.WA_DATABASE_PATH.value])
        self._output_directory = cast(str, kwargs[CLIConstants.OUTPUT_DIRECTORY.value])
        self._filtered_extensions = cast(List[str], kwargs[CLIConstants.FILTERED_EXTENSIONS.value])
        # database attributes
        self._conn = sqlite3.connect(os.path.join(self._db_path, Constants.CHAT_STORAGE_FILE))
        self._cursor = self._conn.cursor()
        self._group_name_matching_data: Optional[pd.DataFrame] = None
        # make output directory
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

        os.mkdir(self.output_dir)

    @property
    def media_dir(self) -> str:
        return os.path.join(self._db_path, Constants.MESSAGE, Constants.MEDIA)

    @property
    def output_dir(self) -> str:
        return os.path.join(self._output_directory, Constants.OUTPUT_FOLDER_NAME)

    @lru_cache()
    def _get_group_name_by_id(self, group_id: str) -> str:
        assert self._group_name_matching_data is not None
        return self._group_name_matching_data.loc[group_id, Constants.GROUP_NAME_KEY]

    def _get_chat_id_to_name_matches(self) -> None:
        with open(os.path.join(Constants.PKG_DIR, Constants.GROUP_TO_ID_QUERY_FILE), 'r') as query_file:
            self._group_name_matching_data = pd.read_sql_query(
                query_file.read(),
                self._conn
            ).set_index(Constants.GROUP_ID_KEY)
            logger.info("successfully queried group id to group name matches")

    @staticmethod
    @lru_cache()
    def _extract_group_id(root_dir: str) -> str:
        match = Constants.EXTRACT_GROUP_NAME_RE.search(root_dir)
        assert match
        return match.group(1)

    def _extract_recursively(self) -> List[Video]:
        video_paths: List[Video] = []
        for root, _, files in os.walk(self.media_dir):
            for file in files:
                if any([file.endswith(extension) for extension in self._filtered_extensions]):
                    group_id = ExtractWAMedia._extract_group_id(root_dir=root)
                    video_paths.append(
                        Video(
                            name=file,
                            file_path=os.path.join(root, file),
                            group_id=group_id,
                            group_name=self._get_group_name_by_id(group_id=group_id)
                        )
                    )

        logger.info(f"found {len(video_paths)} videos!")
        return video_paths

    def _transfer_videos(self, videos: List[Video]) -> None:
        for video in tqdm(videos):
            os.makedirs(os.path.join(self.output_dir, video.group_name), exist_ok=True)
            shutil.copy(
                video.file_path,
                os.path.join(
                    self.output_dir,
                    video.group_name,
                    video.name
                )
            )

    def run(self) -> None:
        self._get_chat_id_to_name_matches()
        videos = self._extract_recursively()
        self._transfer_videos(videos)
        logger.info(f"done copying all videos to {self.output_dir}!")


def _main(**kwargs: Union[str, List[str]]) -> int:
    extract_wa_videos = ExtractWAMedia(**kwargs)
    extract_wa_videos.run()
    return 0
