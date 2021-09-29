import os
import shutil
import configparser

config = configparser.ConfigParser()


#get script list

def scriptOrganiser():
  config.read('./settings.ini')
  pdbdir = config.get('EXPORTPATH', 'pdbdir')
  asidir = config.get('EXPORTPATH', 'asidir')
  luadir = config.get('EXPORTPATH', 'luadir')
  scriptImport = config.get('IMPORTPATH', 'scripts')
  fileScriptList = os.listdir("./Files/Scripts")

  print(pdbdir , asidir)
  x = 0
  while x < len(fileScriptList):
    split = fileScriptList[x].split(".")

    if ".pdb" in fileScriptList[x]:
      #moves pdb file
      shutil.move(scriptImport + fileScriptList[x], pdbdir + fileScriptList[x])
      #splits files name between the .
      #checks if dll exists
    if (os.path.exists(scriptImport + split[0] + ".dll")):
      #moves dll file
      shutil.move(scriptImport + split[0] + ".dll", pdbdir + split[0] + ".dll")
    #checks if config folder exists 
    if (os.path.exists(scriptImport + split[0] + ".ini" or os.path.exists(scriptImport + split[0] + ".cfg" or os.path.exists(scriptImport + split[0] + ".xml")))):
      #moves folder
      shutil.move(scriptImport + split[0], pdbdir + split[0])
    print(split[0])
    if (os.path.exists(scriptImport + split[0])):
      #moves folder
      shutil.move(scriptImport + split[0], pdbdir + split[0])

    #checks for .asi file
    elif ".asi" in fileScriptList[x]:
      #moves ASI file
      shutil.move(scriptImport + fileScriptList[x], asidir + fileScriptList[x])
      #splits files name between the "."
      split = fileScriptList[x].split(".")
      #checks if dll exists with the same name.
      if (os.path.exists(scriptImport + split[0] + ".dll")):
        #moves dll file
        shutil.move(scriptImport + split[0] + ".dll", asidir + split[0] + ".dll")
      #checks if config folder exists with the same name. 
      if (os.path.exists(scriptImport + split[0])):
        #moves config folder
        shutil.move(scriptImport + split[0], asidir + split[0])
    #checks for lua files
    elif ".lua" in fileScriptList[x]:
      shutil.move(scriptImport + fileScriptList[x], luadir + fileScriptList[x])
    x+=1
  return True


