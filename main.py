import sys
from ArtistFolder import ArtistFolder


if __name__ == "__main__":
    theFolder = sys.argv[1]

    artistFolder = ArtistFolder( theFolder )
    artist = artistFolder.getDir()
    hasMD5 = artistFolder.hasMD5()
    hasCUE = artistFolder.hasCueFile()
    hasValidCUE = artistFolder.checkCUE()

    print(f"Artist is {artist}")
    print(f"    MD5 has {artist}.md5: {hasMD5}")
    print(f"    Has at least a CUE file: {hasCUE}")
    if hasCUE:
        if hasValidCUE:
            print("     CUE file is valid.")
        else:
            print("     *** CUE file is not valid.")