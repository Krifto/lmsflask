from pylms.server import Server
from pylms.player import Player
import os

def lmstest():
    sc = Server(hostname="nook-color-android", port=9090)
    sc.connect()

    print "Logged in: %s" % sc.logged_in
    print "Version: %s" % sc.get_version()

    players = sc.get_players()
    for player in players:
        info = "Name: %s | Mode: %s | Time: %s | Connected: %s | WiFi: %s" % (player.get_name(), player.get_mode(), player.get_time_elapsed(), player.is_connected, player.get_wifi_signal_strength())
    #sq.stop()
        print(info)
    #return info
    #print sq.get_track_title()
    #print sq.get_time_remaining()




from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    lmstest()
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')


