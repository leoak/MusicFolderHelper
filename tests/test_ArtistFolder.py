import unittest
from ArtistFolder import ArtistFolder

class TestMaClasse(unittest.TestCase):

  def test_instanciation_fail_if_path_is_NOT_String(self):       
    with self.assertRaises(TypeError):
      artistFolder = ArtistFolder(20)

  def test_instanciation_fail_with_unknown_path(self):
    with self.assertRaises(FileNotFoundError):
      artistFolder = ArtistFolder("FooBar")

if __name__ == "__main__":
  unittest.main()