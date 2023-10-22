import sys, os
sys.path.append(os.getcwd())

from modules.settings import load_file

settings = load_file()

def get_list_of_files():
    return os.listdir(settings['downloadDir'])
    
def organise_file(filename: str) -> None:
    fileType = filename.split(".")[-1]
    
    for key, value in settings['targetDirs'].items():
        if fileType in value:
            currentFullPath = os.path.join(settings['downloadDir'], filename)
            
            if not os.path.isdir(key):
                raise NotADirectoryError("Given folder wasnt valid.")
            
            targetFullPath = os.path.join(key, filename)
            os.rename(currentFullPath, targetFullPath)