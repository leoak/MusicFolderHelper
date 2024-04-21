import sys
from ArtistFolder import ArtistFolder


if __name__ == "__main__":
    theFolder = sys.argv[1]

    artistFolder = ArtistFolder( theFolder )
    artist = artistFolder.getDir()
    hasMD5 = artistFolder.hasMD5()

    print(f"Artist is {artist}")
    print(f"MD5 is {artist}.md5: {hasMD5}")