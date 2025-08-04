import unittest
import os
from ArtistFolder import ArtistFolder

class TestMAIN(unittest.TestCase):
    def test_should_fail_on_bad_CUEparameterFILE(self):
        curDir = os.getcwd()
        artistFolder = ArtistFolder(f"{curDir}/tests/testData/BadDir")
        cueFilePath = f"{curDir}/tests/testData/BadDir/NoFILEParameterIn.cue"
        result = artistFolder.checkCUE(cueFilePath)
        self.assertEqual(result, False, "Should return False on bad CUE file")

if __name__ == "__main__":
  unittest.main()