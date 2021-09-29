import requests
from os import error
import configparser
config = configparser.ConfigParser()
config.read('./settings.ini')

dlcpacksdir = config.get('MISC', 'PATCHDAYVER')

def getVersion():
  try:
    r = requests.get('https://files.charlieschuyler.com/patchday.json')
    return r.json()["current-release"]
  except:
    return dlcpacksdir + "  :   [Offline]"


