from typing import Any, Dict, Optional, Sequence
import argparse
import os
# local modules
from extract_wa_media.constants import Constants, CLIConstants
from extract_wa_media.logger import Logger
from extract_wa_media.extract_media import _main


def _validate_input(args: Dict[str, Any]) -> bool:
    assert os.path.exists(args[CLIConstants.WA_DATABASE_PATH.value]), "WA DB path was not found"
    assert os.path.exists(args[CLIConstants.OUTPUT_DIRECTORY.value]), "output directory was not found"
    assert all(map(lambda val: val.startswith("."), args[CLIConstants.FILTERED_EXTENSIONS.value])),\
        "Some of the provided extensions do not start with a dot (`.`)"

    return True


def _setup_argparser() -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(description=CLIConstants.CLI_DESCRIPTION.value)
    arg_parser.add_argument(
        CLIConstants.WA_DATABASE_PATH.value,
        help="insert path to your WA DB folder, i.e. the path to your local `group.net.whatsapp.WhatsApp.shared` folder",
    )
    arg_parser.add_argument(
        CLIConstants.OUTPUT_DIRECTORY.value,
        help="insert path to the directory to which your media will be extracted to",
    )
    arg_parser.add_argument(
        f"-{''.join([word[0] for word in CLIConstants.FILTERED_EXTENSIONS.value.split('_')])}",
        f"--{CLIConstants.FILTERED_EXTENSIONS.value}",
        required=False,
        nargs="+",
        help=f"""insert a space separated list of the media extensions that you want to extract.
        Please make sure all extensions are prefixed with a dot (`.`).
        This defaults to `{" ".join(Constants.DEFAULT_RELEVANT_EXTENSIONS)}`""",
        default=Constants.DEFAULT_RELEVANT_EXTENSIONS,
    )

    return arg_parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    arg_parser = _setup_argparser()
    args = arg_parser.parse_args(argv)
    assert _validate_input(args.__dict__)
    Logger.setup_logger()
    return _main(**args.__dict__)


if __name__ == "__main__":
    raise SystemExit(
        main(
            # [
            #     r"/Users/uriyakir/My Drive/group.net.whatsapp.WhatsApp.shared",
            #     r"/Users/uriyakir/Desktop/",
            #     "-fe",
            #     ".mp4",
            #     ".jpg",
            # ]
        )
    )
