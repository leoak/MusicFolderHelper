import unittest
import os

from CUEFile import CUEFile

class TestCUEFile(unittest.TestCase):

    def test_instanciation_fail_if_path_is_NOT_String(self):      
        with self.assertRaises(TypeError):
            acuefile = CUEFile(20)

    def test_instanciation_path_is_set(self):
        curDir = os.getcwd()
        cueFilePath= f"{curDir}/tests/testData/GoodDir/IsoAlbum1.cue"
        cueFile = CUEFile(f"{cueFilePath}")
        self.assertEqual(cueFile.path, cueFilePath)

    def test_checkCUE_raises_Error_on_nonexisting_CUEfile(self):
        curDir = os.getcwd()
        cueFilePath = f"{curDir}/tests/testData/NonExistingCUEFile.cue"
        cueFile = CUEFile(f"{cueFilePath}")
        with self.assertRaises(FileNotFoundError):
            result = cueFile.checkCUE()
    
    def test_checkCUE_should_fail_on_BAD_CUEparameterFILE(self):
        curDir = os.getcwd()
        cueFilePath= f"{curDir}/tests/testData/BadDir/NoFILEParameterIn.cue"
        cueFile = CUEFile(f"{cueFilePath}")
        result = cueFile.checkCUE()
        self.assertFalse(cueFile.isValid, "Should be False on bad CUE file")

    def test_checkCUE_should_not_fail_on_GOOD_CUEparameterFILE(self):
        curDir = os.getcwd()
        cueFilePath= f"{curDir}/tests/testData/GoodDir/IsoAlbum1.cue"
        cueFile = CUEFile(f"{cueFilePath}")
        result = cueFile.checkCUE()
        self.assertTrue(cueFile.isValid, "Should be True on good CUE file")

if __name__ == "__main__":
  unittest.main()