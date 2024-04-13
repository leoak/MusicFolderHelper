import os

class ArtistFolder:

  def __init__(self, path):
    if not isinstance(path, str):
      raise TypeError(f"Le nom {path} doit être une chaîne de caractères")
    self.path = path
    if os.path.exists(self.path):
      print(f"Le répertoire {self.path} existe")
    else:
      raise FileNotFoundError(f"Le répertoire {self.path} n'existe pas")

if __name__ == "__main__":
  try:
    myClass = ArtistFolder(10)
  except TypeError as e:
    print(f"Erreur d'instanciation: {e}")
  else:
    print("Hello World")
