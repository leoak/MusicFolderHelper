import os

from CUEFile import CUEFile

class ArtistFolder:

  def __init__(self, path):
    if not isinstance(path, str):
      raise TypeError(f"The path parameter {path} must be a string")
    self.path = path
    if not os.path.exists(self.path):
      raise FileNotFoundError(f"Le répertoire {self.path} n'existe pas")
    self.artistDir = os.path.basename(path)
    self.md5File = f"{self.path}/{self.artistDir}.md5"
    self.CUEFiles = []
    self.setCUEFiles()

  def setCUEFiles(self):  
    try:
      items = os.listdir(self.path)
      for item in items:
        item_path = os.path.join(self.path, item)
        if os.path.isfile(item_path) and item.endswith('.cue'):
          self.CUEFiles.append(CUEFile(item_path))
      if self.CUEFiles:
        return True
      else:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

  def getDir(self):
    return self.artistDir

  def hasCueFile(self):
    return len(self.CUEFiles) > 0  
  
  def checkCUE(self):
    if not self.hasCueFile():
      return False
    else:
      return self.CUEFiles[0].checkCUE()
      
  def hasMD5(self):
    return os.path.isfile(self.md5File)
  
if __name__ == "__main__":
  try:
    myClass = ArtistFolder(10)
  except TypeError as e:
    print(f"Instanciation Error: {e}")
  else:
    print("Another error occurred")
