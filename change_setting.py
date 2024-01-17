from json import dumps
from cmd_line_ui import get_ui



def save_settings(setting):
  with open("settings.json", "w") as file: file.write(dumps(setting, indent=2))

def quick_change(item, name, toggle):
  item[name] = input((
    " Enter your new default {} ({}) - " if toggle == True else " Enter your new profile {} ({}) - "
  ).format(name.replace("_", " "), item[name])) or item[name]

def change_defaults(setting):
  default_setting, choice_result = [ "status", "guild_id", "channel_id", "self_mute" ], {}
  for i in default_setting: choice_result[str(default_setting.index(i)+1)] = quick_change(setting["default"], i, True)
  while True:
    get_ui("default_menu")
    choice = input(" - ")
    if choice == 0: break
    elif choice in [str(i) for i in range(1, 6)]: choice_result[choice]
    else: print(" [ERROR] Wrong Input!")
  save_settings(setting)
  return setting

def change_profiles(setting):
  selected_profile, profile_setting, choice_result = 0, [ "token", "status", "guild_id", "channel_id", "self_mute" ], {}
  for i in profile_setting: choice_result[str(profile_setting.index(i)+1)] = quick_change(setting["profiles"][selected_profile], i, False)
  while True:
    get_ui("setting_menu")
    print(setting["profiles"][selected_profile]["token"])
    choice = input("(Selected profile: {}/{}) > ".format(selected_profile + 1, len(setting["profiles"])))
    if choice == "0": break
    elif choice == "2": setting["profiles"].pop(selected_profile)
    elif choice == "3":
      while True:
        next_selected_profile = 0
        try: next_selected_profile = int(input("Enter the profile you want to select > "))
        except: print(" [ERROR] Wrong Input! Selected Profile 1")
        selected_profile = next_selected_profile
    elif choice in [str(i) for i in range(4, 10)]: choice_result[choice]
    else: print(" [ERROR] Wrong Input!")
  save_settings(setting)
  return setting
