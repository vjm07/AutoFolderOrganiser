import sys, os, json
sys.path.append(os.getcwd())



def load_file() -> dict:
    filePath = os.path.join(os.getcwd(), 'settings.json')
    if not os.path.isfile(filePath):
        raise FileNotFoundError("Expected 'settings.json' in the same folder as this executable but found none.")
    
    with open(filePath, 'r') as file:
        settings = json.load(file)
    
    unit = settings['interval']['unit'] 
    value = settings['interval']['value'] 
    
    if unit not in ["seconds", "minutes", "hours", "days"]:
        raise IOError("interval unit must be in seconds, minutes, hours or days")

    if not isinstance(value, int):
        raise IOError("value must be int.")
    
    if not os.path.exists(settings['downloadDir']):
        raise KeyError("Could not find 'downloadDir' in settings...")
    
    for key in settings['targetDirs'].keys():
        if not os.path.isdir(key):
            raise NotADirectoryError("All directories in targetDirs must be valid.")
    
    return settings