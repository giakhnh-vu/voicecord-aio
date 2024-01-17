# Import internal lib(s)
from json import loads
from time import sleep
from os import system, listdir
from multiprocessing import Process

# Import external lib(s)
try:
  from requests import get
  from inputimeout import inputimeout, TimeoutOccurred
except:
  system("python3 -m pip install flask websocket websocket-client==1.5.0 requests")
  from requests import get
  from inputimeout import inputimeout, TimeoutOccurred
  system("clear")

# Verify project integrity
for i in [ "change_setting.py", "cmd_line_ui.py", "join_channel.py", "keep_alive.py", "settings.json" ]:
  if not i in listdir():
    print(" [Voicecord AIO] File integrity checker - File missing: {}".format(i))
    SystemExit
  if i == "settings.json":
    with open(i, "r") as file:
      try: loads(file.read())
      except: SystemExit

# Import internal packages
try:
  from cmd_line_ui import get_ui
  from join_channel import joiner
  from keep_alive import keep_alive
  from change_setting import change_default, change_profiles
except:
  from cmd_line_ui import get_ui
  from join_channel import joiner
  from keep_alive import keep_alive
  from change_setting import change_default, change_profiles


# Assign class(es)
class client: default, profiles = {}, []


# Create function(s)
def load_setting():
  # Load settings from settings.json
  with open("settings.json", "r") as file:
    data = loads(file.read())
    client.default, client.profiles = data["default"], []

  # Validate tokens
  for count in len(data["profiles"]):

    try:
      info = get('https://discordapp.com/api/v9/users/@me', headers={ "Authorization": data["profiles"][count]["token"] })
    
      if data["profiles"][count]["enabled"] and info.status_code == 200:
        client.profiles.append({ "token": data["profiles"][count]["token"] })

        for setting in [ "status", "guild_id", "channel_id", "self_mute" ]:
          client.profiles[len(client.profiles) - 1][setting] = data["profiles"][count][setting] if data["profiles"][count]["custom"] else client.default[setting]

        print(" [Voicecord AIO] Token checker - passed: {}".format(data["profiles"][count]["token"]))
    except:
      print(" [Voicecord AIO] Token checker - failed: {} ".format(data["profiles"][count]["token"]))

def main():
  get_ui("banner")
  while True:
    get_ui("main_menu")
    try: menu_choice = inputimeout(" Enter your choice. Automatically choose 1 after 10 seconds - ", 10) or "1"
    except TimeoutOccurred: menu_choice = "1"
    if menu_choice == "1":
      load_setting()
      if len(client.profiles) == 0:
        print(" [Voicecord AIO] Error - No available profile. Please add atlease one profile to start!")
      else:
        break
    elif menu_choice == "2":
      pass
    elif menu_choice == "3":
      print(" [Voicecord AIO] Exitting...")
      SystemExit
    else:
      print(" [Voicecord AIO] Error - Wrong input!")
  while True:
    for i in client.profiles:
      Process(target=joiner, args=(i)).start()
      sleep(30 / len(client.profiles))


# Main point of running this script
if __name__ == "__main__":
  keep_alive()
  main()
