import unittest
import os
from ArtistFolder import ArtistFolder

class TestMAIN(unittest.TestCase):
    def test_should_fail_on_bad_CUEparameterFILE(self):
        curDir = os.getcwd()
        folderPath = f"{curDir}/tests/testData/BadDir"
        artistFolder = ArtistFolder(f"{folderPath}")
        result = artistFolder.checkCUE()
        self.assertFalse(result, "Should return False on bad CUE file")

if __name__ == "__main__":
  unittest.main()