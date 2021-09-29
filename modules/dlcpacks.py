import configparser
import shutil
import time
import os
import shutil
config = configparser.ConfigParser()
config.read('./settings.ini')


def dlcpackOrganiser():
  x = 0
  dlcpacks_import_path = config.get("IMPORTPATH", "dlcpacks")
  dlcpacks_expo_path = config.get('EXPORTPATH', 'dlcpacksdir')
  dlclist_expo_path = config.get('EXPORTPATH', 'dlclistdir')
  dlcpacks_list = os.listdir(dlcpacks_import_path)
  f = open(dlclist_expo_path + "dlclist.txt", "a")

  while x < len(dlcpacks_list):
    print(x)
    try:
      shutil.move(dlcpacks_import_path  + dlcpacks_list[x], dlcpacks_expo_path)
    except:
      print("failed to move " + dlcpacks_list[x])
      time.sleep(2)

    print("a")
    vehicleItem = "\t\t<Item>dlcpacks:/"+dlcpacks_list[x]+"/</Item>\n"
    f.write(vehicleItem)
    x += 1
  print("return")
  return


    #

#