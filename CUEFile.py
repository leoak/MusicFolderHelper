import os
import re

class CUEFile:
  
    def __init__(self, path):
        if not isinstance(path, str):
            raise TypeError(f"The path parameter {path} must be a string")
        self.path = path
        self.isValid = False
    
    def checkCUE(self):
        path = os.path.dirname(self.path)

        with open(self.path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('FILE'):
                    match = re.search(r'FILE "([^"]+)"', line)
                    if match:
                        filename = match.group(1)
                        filepath = os.path.join(path, filename)
                        if os.path.isfile(filepath):
                            print(f"The file '{filepath}' exists.")
                            self.isValid = True
                        else:
                            print(f"The file '{filepath}' does not exist.")
                            self.isValid = False
                        return self.isValid
