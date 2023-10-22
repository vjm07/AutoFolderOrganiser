import sys, os 
sys.path.append(os.getcwd())

from apscheduler.schedulers.background import BackgroundScheduler
from modules.settings import load_file
from modules.folder_organiser import *

settings = load_file()

unit = settings['interval']['unit'] 
value = settings['interval']['value'] 

def sort():
    allFiles = get_list_of_files()
    for f in allFiles:
        organise_file(f)

scheduler = BackgroundScheduler()

if unit == "seconds":
    scheduler.add_job(sort, 'interval', seconds=value)
elif unit == "minutes":
    scheduler.add_job(sort, 'interval', minutes=value)
elif unit == "hours":
    scheduler.add_job(sort, 'interval', hours=value)
elif unit == "days":
    scheduler.add_job(sort, 'interval', days=value)