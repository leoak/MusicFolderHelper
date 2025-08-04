import os
import re

class CUEFile:
  
    def __init__(self, path):
        if not isinstance(path, str):
            raise TypeError(f"The path parameter {path} must be a string")
    
    def checkCUE(self, file):
        path = os.path.dirname(file)
        print (f"Checking CUE file in: {path}")
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('FILE'):
                    match = re.search(r'FILE "([^"]+)"', line)
                    if match:
                        filename = match.group(1)
                        filepath = os.path.join(path, filename)
                        if os.path.isfile(filepath):
                            print(f"The file '{filepath}' exists.")
                            return True
                        else:
                            print(f"The file '{filepath}' does not exist.")
                            return False
