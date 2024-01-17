from flask import Flask
from waitress import serve
from threading import Thread

app = Flask('')

@app.route('/')
def main(): return '<meta http-equiv="refresh" content="0; URL=https://phantom.is-a.dev/support"/>'
def run(): serve(app, host="0.0.0.0", port=8080)
def keep_alive(): Thread(target=run).start()
