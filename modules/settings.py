from modules.version import getVersion
from modules.recovery import resetDefault
import os
import configparser
import time

config = configparser.ConfigParser()



def optionsOut():
  config.read('./settings.ini')

  os.system('cls')
  print("")
  print("")
  print(" 1.    Mods Folder              :    " + config.get('MISC', "modsFolder"))
  print(" 2.    Grand Theft Auto Path    :    " + config.get('MISC', 'gamePath'))
  print(" 3.    Patchday Version         :    " + config.get('MISC', 'patchdayVer'))
  print("--")
  print(" 4.    Core Scripts Path        :    " + config.get('EXPORTPATH', 'asidir'))
  print(" 5.    Scripts Path             :    " + config.get('EXPORTPATH', 'pdbdir'))
  print(" 6.    LUA Path                 :    " + config.get('EXPORTPATH', 'luadir'))
  print(" 7.    dlcpack Path             :    " + config.get('EXPORTPATH', 'dlcpacksdir'))
  print(" 8.    dlclist Path             :   " + config.get('EXPORTPATH', 'dlclistdir'))
  print("--")
  print(" 9.    Help")
  print(" 0.    Home")
  print("--")
  print(" 20.   Reset to defualt settings")
  print("")
  opt = input("Select an option          :    ")
  options(opt)

def options(opt):
  try:
    config.read('./settings.ini')
    #changes mods folder bool
    if opt == "1":
      if config.get('MISC', "modsFolder") == 'True':
        config.set('MISC', 'modsFolder', 'False')
      elif config.get('MISC', 'modsFolder') == 'False':
        config.set('MISC', 'modsFolder', 'True')
    #
    elif opt == "2":
      os.system('cls')
      path = input("Grand Theft Auto V Path > ")
      if(path[-1] == '\\' or path[-1] == '/' ):
        path = path[:-1]
      config.set('MISC', 'gamepath', path + "\\")
      config.set('EXPORTPATH', 'asidir', path + "\\")
      config.set('EXPORTPATH', 'pdbdir', path + '\scripts\\')
      config.set('EXPORTPATH', 'luadir', path + '\\scripts\\addins\\')
      config.set('EXPORTPATH', 'dlcpacksdir', path + '\\mods\\update\\x64\\dlcpacks\\')
      config.set('EXPORTPATH', 'dlclistdir', path + '\\mods\\')
      time.sleep(2)
    #
    elif opt == "3":
      return True
    #
    elif opt == "4":
      os.system('cls')
      path = input("Grand Theft Auto V Cord Scripts Directory > ")
      if(path[-1] == '\\' or path[-1] == '/' ):
        path = path[:-1]
      config.set('EXPORTPATH', 'asidir', path)
    elif opt == "5":
      os.system('cls')
      path = input("Grand Theft Auto V Scripts Directory > ")
      if(path[-1] == '\\' or path[-1] == '/' ):
        path = path[:-1]
      config.set('EXPORTPATH', 'pdbdir', path)
    elif opt == "6":
      os.system('cls')
      path = input("Grand Theft Auto V LUA Scripts Directory > ")
      if(path[-1] == '\\' or path[-1] == '/' ):
        path = path[:-1]
      config.set('EXPORTPATH', 'luadir', path)
    elif opt == "7":
      os.system('cls')
      path = input("Grand Theft Auto V dlcpack Directory > ")
      if(path[-1] == '\\' or path[-1] == '/' ):
        path = path[:-1]
      config.set('EXPORTPATH', 'luadir', path)
    elif opt == "8":
      os.system('cls')
      path = input("Grand Theft Auto V dlclist Directory > ")
      if(path[-1] == '\\' or path[-1] == '/' ):
        path = path[:-1]
      config.set('EXPORTPATH', 'luadir', path)
    elif opt == "9":
      help()

    elif opt == "0":
      return True
    elif opt == "20":
      resetDefault()


    with open('./settings.ini', 'w') as configfile:
      config.write(configfile)
    optionsOut()
  except:
    print("Failed to change option - Please try again")
    time.sleep(8)


def help():
  os.system('cls')
  print(" ")
  print(" Patchday Version (Latest Version :" + getVersion()+")"  )
  print(" Grand Theft Auto Path Automatically Changes Script Directorys")
  print(" Changing directorys to non folders (eg. RPF, ZIP, RAR) will result in the script crashing")
  input("")


