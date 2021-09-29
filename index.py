from modules.scripts import scriptOrganiser
from modules.dlcpacks import dlcpackOrganiser
from modules.version import getVersion
from modules.settings import optionsOut
from modules.about import about

import configparser
import time
import os

config = configparser.ConfigParser()



def home():
  os.system('cls')
  print("    ")
  print("    ")
  print(" Latest Patch Day    :    " + getVersion())
  print("    ")
  print("    ")
  print("    ")
  print(" 1.    Install Scripts")
  print(" 2.    Install DlcPacks")
  print(" 3.    Options")
  print(" 4.    About")
  print("--")
  print(" 5.    Verify Directorys")
  print("    ")


def main():
  config.read('./settings.ini')
  path = [config.get('EXPORTPATH', 'asidir'),config.get('EXPORTPATH', 'pdbdir'),config.get('EXPORTPATH', 'luadir'),config.get('EXPORTPATH', 'dlcpacksdir'),config.get('EXPORTPATH', 'dlclistdir'), config.get('IMPORTPATH', 'scripts'), config.get('IMPORTPATH', 'dlcpacks')]
  for x in range(1,7):
    if not os.path.isdir(path[x]):
      os.makedirs(path[x]) 
  home()



if __name__=="__main__": 
  main()


while True:
  userOptions = input(" Select an option    :  ")
  if userOptions == "1":
    if scriptOrganiser():
      print("successfully installed scripts")
      print("Please place dlclist.xml located in \"" + config.get('EXPORTPATH', 'dlclistdir') + "\" in *Grand Theft Auto directory*\\mods\\update\\update.rpf\\common\\data   - using open IV")
      time.sleep(2)
  elif userOptions == "2":
    dlcpackOrganiser()
  elif userOptions == "3":
    optionsOut()
    main()
  elif userOptions() == "4":
    about()
  elif userOptions == "5":
    main()
  home()    

