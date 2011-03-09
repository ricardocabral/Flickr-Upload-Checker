# What

Script for checking if your local photos have alredy been uploaded to Flickr.

# WARNING

It will remove local files that has the same EXIF Creation-date-time tag as the one uploaded to Flickr.

# Requirements

1. python (http://www.python.org)
2. exiftool (http://www.sno.phy.queensu.ca/~phil/exiftool/)
3. flickrapi (http://pypi.python.org/pypi/flickrapi)

# Usage

> python checkupl.py

This will scan all the current directory and it's subdirectories for jpeg images and check against your Flickr account.
This will make one Flickr request for each image in the current dir and its subdirs.

# Credits

Ricardo Niederberger Cabral
ricardo@isnotworking.com
https://github.com/ricardocabral/Flickr-Upload-Checker