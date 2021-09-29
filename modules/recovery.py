import keyboard
import os
import requests


def resetDefault():
  os.system('cls')
  print('')
  print(' NOTE : THIS ACTION IS NOT REVERSABLE')
  print('')
  print(' Press the "Y" key to continue')
  print(' Press the "N" key to exit')
  print('')
  while True:
    
    if keyboard.is_pressed('y'):
      try:
        if os.path.exists('./settings.ini'):
          os.remove('./settings.ini')
        url = 'https://files.charlieschuyler.com/settings.ini'
        r = requests.get(url, allow_redirects=True)
        open('settings.ini', 'wb').write(r.content)
        
      except:
        print("Error while downloading file. please connect to the internet")
        input("")
      return
    elif keyboard.is_pressed('n'):
      return
      