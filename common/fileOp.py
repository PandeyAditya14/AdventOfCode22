from pathlib import Path

data_folder = Path("input/")

def readFileLine (filename):
    filepath=  data_folder / filename
    fileObj = open(filepath , "r")
    fileContent = fileObj.read().splitlines() # We can use readlines but it contains \n
    fileObj.close()
    return fileContent

def readFile(filename):
    filepath=  data_folder / filename
    fileObj = open(filepath , "r")
    fileContent = fileObj.read()
    fileObj.close()
    return fileContent