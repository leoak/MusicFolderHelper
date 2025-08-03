import os

class ArtistFolder:

  def __init__(self, path):
    if not isinstance(path, str):
      raise TypeError(f"Le nom {path} doit être une chaîne de caractères")
    self.path = path
    if not os.path.exists(self.path):
      raise FileNotFoundError(f"Le répertoire {self.path} n'existe pas")
    self.artistDir = os.path.basename(path)
    self.md5File = f"{self.path}/{self.artistDir}.md5" 
    
  def getDir(self):
    return self.artistDir

  def hasCueFile(self):
    try:
      items = os.listdir(self.path)
      for item in items:
        item_path = os.path.join(self.path, item)
        if os.path.isfile(item_path) and item.endswith('.cue'):
          return True
      return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
  def hasMD5(self):
    print (f"Checking {self.md5File}") 
    return os.path.isfile(self.md5File)
  
if __name__ == "__main__":
  try:
    myClass = ArtistFolder(10)
  except TypeError as e:
    print(f"Erreur d'instanciation: {e}")
  else:
    print("Hello World")
