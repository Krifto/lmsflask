import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from pylms.server import Server
from pylms.player import Player


#def lmstest():
sc = Server(hostname="192.168.178.24", port=9090)
sc.connect()

print "Logged in: %s" % sc.logged_in
print "Version: %s" % sc.get_version()

from flask import Flask, render_template
app = Flask(__name__)

commands = ('play', 'pause', 'stop', 'volume_up', 'volume_down')


def player_info_string(player):
    return "Name: %s | Mode: %s | Time: %s | Connected: %s | WiFi: %s" % (player.get_name(), player.get_mode(), player.get_time_elapsed(), player.is_connected, player.get_wifi_signal_strength())


@app.route('/')
def hello_world():
    return render_template('lmsflask.html', players=sc.get_players())


@app.route('/<player_name>/<cmd>')
def player_control(player_name, cmd):
    player = sc.get_player(player_name)
    if not player:
        return "error, player not found"
    if cmd in commands:
        if cmd == 'play':
            player.play()
        elif cmd == 'stop':
            player.stop()
        elif cmd == 'volume_up':
             player.volume_up()
        elif cmd == 'volume_down':
             player.volume_down()
    return render_template('lmsflask.html', players=sc.get_players())


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')


