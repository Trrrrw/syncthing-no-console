from pystray import MenuItem, Icon
from psutil import process_iter
from PIL import Image

import webbrowser
import os
from threading import Thread
from subprocess import Popen, CREATE_NEW_CONSOLE


def terminate_process_by_name(process_name):
    """
    Terminates a process by its name.

    Args:
        process_name (str): The name of the process to terminate.

    Returns:
        None
    """
    for proc in process_iter(['name']):
        if proc.info['name'] == process_name:
            proc.terminate()


def open_web():
    webbrowser.open('http://127.0.0.1:8384/')


def about():
    webbrowser.open('https://github.com/Trrrrw/syncthing_no_console')


def on_quit(app, item):
    terminate_process_by_name("syncthing.exe")
    app.stop()


def start_syncthing():
    command = ['syncthing.exe', '--no-browser', '--no-console']
    syncthing_process = Popen(
        command, shell=True, creationflags=CREATE_NEW_CONSOLE)
    syncthing_process.wait()


image = Image.open(f'{os.path.dirname(__file__)}/icon.png')
menu = (
    MenuItem('打开Web界面', open_web),
    MenuItem('关于', about),
    MenuItem('退出', on_quit),
)
app = Icon('app_name', image, 'Syncthing', menu)

syncthing_thread = Thread(target=start_syncthing)
syncthing_thread.daemon = True
syncthing_thread.start()

app.run()
