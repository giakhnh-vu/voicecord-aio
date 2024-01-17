# Import internal libs
from time import sleep
from json import loads, dumps
from websocket import WebSocket


# Create function(s)
def joiner(setting):
  try:
    ws = WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    for i in [{
      "op": 2,
      "d": {
        "token": setting["token"],
        "properties": { "$os": "Windows 10", "$browser": "Google Chrome", "$device": "Windows" },
        "presence": { "status": setting["status"], "afk": False }
      },
      "s": None,
      "t": None
    }, {
      "op": 4,
      "d": {
        "guild_id": setting["guild_id"],
        "channel_id": setting["channel_id"],
        "self_mute": setting["self_mute"],
        "self_deaf": False
      }
    }]: ws.send(dumps(i))
    print(" [Voicecord AIO] Connected {}#{} to discord with channel id: {}".format(
      setting["info"]["username"],
      setting["info"]["discriminator"],
      setting["channel_id"]
    ))
    sleep(heartbeat / 1000)
    ws.send(dumps({ "op": 1, "d": None }))
  except:
    pass
