from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Heluwu! \n Please contact Xyncross#0001 if you're facing any issues!"


def run():
    app.run(host='0.0.0.0', port=8080)


def host():
    t = Thread(target=run)
    t.start()


#runs an HTTP server for the bot
#uptimebot pings every 5 mins to keep bot active
