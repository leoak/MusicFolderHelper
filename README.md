# MusicFolderHelper

A utility to help managing my audio files and metadata.

My *music albums* are digitally stored as 
* iso+cue files for SACD albums
* flac+cue files for CD albums

My goals are:
- be able to retrieve albums per perfomer
- be able to play albums in historical order (which is tricky due to re-releases or new masterings)
- make sure that my data are consitent

# Run the program
py .\main.py _directory_

# Run the tests
py .\tests\test_ArtistFolder.py

# Step 1 - Checksum
As a user, I want to be able to verify that I have MD5 checksum files for all my music directories.

Given a Music folder containing folders for each artists, I want to know which directories contain an MD5 file.
The name of the MD5 file is the name of the directory:
`MusicFolder/Artist/Artist.md5`
