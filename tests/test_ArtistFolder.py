import unittest
import os
from ArtistFolder import ArtistFolder

class TestArtistFolder(unittest.TestCase):

  def test_instanciation_fail_if_path_is_NOT_String(self):      
    with self.assertRaises(TypeError):
      artistFolder = ArtistFolder(20)

  def test_instanciation_fail_with_unknown_path(self):
    with self.assertRaises(FileNotFoundError):
      artistFolder = ArtistFolder("FooBar")

  def test_getDir_should_return_artistName(self):
    curDir = os.getcwd()
    artistFolder = ArtistFolder(f"{curDir}/tests/testData/FooBar")
    artist = artistFolder.getDir()
    self.assertEqual(artist, "FooBar")

  def test_hasMD5_should_return_false_no_md5_file(self):
    curDir = os.getcwd()
    artistFolder = ArtistFolder(f"{curDir}/tests/testData/FooBar")
    self.assertEqual(artistFolder.hasMD5(), False)

  def test_hasMD5_should_return_true_if_md5_file(self):
    curDir = os.getcwd()
    artistFolder = ArtistFolder(f"{curDir}/tests/testData/GoodDir")
    self.assertEqual(artistFolder.hasMD5(), True)

  def test_getDir_should_return_artistName_with_space(self):
    curDir = os.getcwd()
    artistFolder = ArtistFolder(f"{curDir}/tests/testData/Unknown Artist")
    artist = artistFolder.getDir()
    self.assertEqual(artist, "Unknown Artist")

  def test_when_has_no_CUE_file(self):
    curDir = os.getcwd()
    artistFolder = ArtistFolder(f"{curDir}/tests/testData/FooBar")
    self.assertFalse(artistFolder.hasCueFile())
    self.assertEqual(len(artistFolder.CUEFiles), 0)
  
  def test_hasCUE_should_return_true_if_CUE_file(self):
    curDir = os.getcwd()
    artistFolder = ArtistFolder(f"{curDir}/tests/testData/GoodDir")
    self.assertTrue(artistFolder.hasCueFile(), True)
    self.assertEqual(len(artistFolder.CUEFiles), 1)

if __name__ == "__main__":
  unittest.main()