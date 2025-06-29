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
_PowerShell_: run_tests.ps1

# Windos integration
- update MusicFolderHelper.reg with the correct paths
- right click on a folder and select "Music Folder Helper"

# Step 1 - Checksum
As a user, I want to be able to verify that I have MD5 checksum files for all my music directories.

Given a Music folder containing folders for each artists, I want to know which directories contain an MD5 file.
The name of the MD5 file is the name of the directory:
`MusicFolder/Artist/Artist.md5`


# Why
## What kind of user

I am the kind of person who, when they want to turn off the light to listen to some music, they will pick an artist and listen to one or multiple albums. When listening to several albums, it will be in chronological order to feel the evolution of the artist.

For these reasons, these are *my* requirements:
* My music library is sorted by artists
* For an artist, the music is sorted by albums
* Music is stored in the best quality format I can have
* I enjoy having assets like album covers
* I want to make sure that my library is not compromised
