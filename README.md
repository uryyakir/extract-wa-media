

# Extract Whatsapp media quickly and easily!
### This tool outputs a directory, containing a subdirectory for each Whatsapp contact / group. Each of these subdirectories will contain all media (images, videos, etc) that was extracted from the backup's WA snapshot.
####  The tool outputs a centralized directory with all of the extracted media. Example output:
```bash
> tree path/to/output/directory/extracted_WA_media
extracted_WA_media
├── Dad
	│ ├── img1.jpg
	│ ├── vid1.mp4
	│ └── vid2.mp4

├── Jerome
	│ ├── img2.jpg
	│ └── vid3.mp4

└── Philip
	├── img3.jpg
	└── vid4.mp4
```

### When is this useful?
1. Easily merge media from old iPhone backup into the current iPhone.
2. You can have all of your Whatsapp media stored locally on your computer, allowing you to easily navigate and examine a centralized collection of your media.

## prerequisites:

To use this tool, all you need to do is extract the `group.net.whatsapp.WhatsApp.shared` folder from your iPhone backup.
That is very simple to do using a tool like *Cok Free iTunes Backup Extractor*. I highly recommend following steps 1-5 in [this](https://www.quora.com/How-can-I-extract-WhatsApp-messages-from-an-iPhone-backup) Quora thread.


## installation:

This package is NOT distributed to pypi, please install the package directly from this repo:<br>
<li>If a virtualenv is activated:</li>

`python3 -m pip install git+git://github.com/uryyakir/extract-wa-media.git#egg=extract_wa_media`
<li>If you want to install globally:</li>

`sudo python3 -m pip install git+git://github.com/uryyakir/extract-wa-media.git#egg=extract_wa_media`


## usage:
When you install the tool, it enables the internal tool's CLI:

```bash
usage: extract_wa_media [-h]
[-fe FILTERED_EXTENSIONS [FILTERED_EXTENSIONS ...]] db_path output_directory

A quick tool that makes it easy to extract all media from your iOS whatsapp database.
This can be useful for merging media from an old backup into your current device.

positional arguments:
db_path - insert path to your WA DB folder, i.e. the path to
    your local `group.net.whatsapp.WhatsApp.shared` folder
output_directory - insert path to the directory to which your media will
    be extracted to

optional arguments:
-fe FILTERED_EXTENSIONS [FILTERED_EXTENSIONS ...], --filtered_extensions FILTERED_EXTENSIONS [FILTERED_EXTENSIONS ...]
    insert a space separated list of the media extensions that you want to extract.
    Please make sure all extensions are prefixed with a dot (`.`). This defaults to `.mp4`
```
Example usage:
`> extract_wa_media /Users/$USER/path/to/group.net.whatsapp.WhatsApp.shared /Users/$USER/Desktop` --> Extract all media files to Desktop

`> extract_wa_media /Users/$USER/path/to/group.net.whatsapp.WhatsApp.shared /Users/$USER/Desktop -fe mp4 jpg thumb` --> Extract all `.mp4`, `.jpg` and `thumb` files to Desktop.
