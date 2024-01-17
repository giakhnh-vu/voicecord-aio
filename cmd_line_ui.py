uis = {
  "banner": [
    " =============================================================================================== ",
    "                                                                                                 ",
    "   88  d8P d8888P d8P d8888b d8888P   d8888P d8888P d8888b   d888b    dB88    d888888P  d8888P   ",
    "   88 dBP dB'.BP     dB              dB     dB'.BP     dBP  dB'.BP   dBP88      dBP    dB'.BP    ",
    "   88dBP dB'.BP dBP dB     dBBBBP   dB     dB'.BP dBBBBP   dB'.BP   dBP 88     dBP    dB'.BP     ",
    "   88BP dB'.BP dBP dB     dBP      dB     dB'.BP dBP'BB.  dB'.BP   dBBBB88    dBP    dB'.BP      ",
    "   88P dBBBBP dBP dBBBBP dBBBBP   dBBBBP dBBBBP dBP  dBP dBBBP    dBP   88 dBBBBBBP dBBBBP       ",
    "                                                                                                 ",
    " ====================================== Made by DarkStarX ====================================== ",
    "                                                                                                 "
  ], "main_menu": [
    " ======================= ",
    "  [ 1 ] Load             ",
    "  [ 2 ] Change Settings  ",
    "  [ 0 ] Exit VC AIO      ",
    " ======================= "
  ], "setting_menu": [
    " ============================== ",
    "  [ 1 ] Change Default Setting  ",
    "  [ 2 ] Change Profile Setting  ",
    "  [ 0 ] Return                  ",
    " ============================== "
  ], "default_menu": [
    " ================================= ",
    "  [ 1 ] Change Default Status      ",
    "  [ 2 ] Change Default Guild ID    ",
    "  [ 3 ] Change Default Channel ID  ",
    "  [ 4 ] Change Default Self Mute   ",
    "  [ 0 ] Return                     ",
    " ================================= "
  ], "profile_menu": [
    " ========================================= ",
    "  [ 1 ] Enable / Disable Selected Profile  ",
    "  [ 2 ] Create / Remove Profile            ",
    "  [ 3 ] Use Default Setting                ",
    "  [ 4 ] Select Profile                     ",
    "  [ 5 ] Change Profile Token               ",
    "  [ 6 ] Change Profile Status              ",
    "  [ 7 ] Change Profile Guild ID            ",
    "  [ 8 ] Change Profile Channel ID          ",
    "  [ 9 ] Toggle Profile Self Mute           ",
    "  [ 0 ] Return                             ",
    " ========================================= "
  ]
}



def get_ui(name): print("\n".join(uis[name]))
