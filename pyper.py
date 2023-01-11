
import pyperclip as pc
import time


def pyper():
    list = []
    i = 0
    value = pc.paste()
    if value not in list:
        list.append(value)
        a = open("clipboard.txt", "a")
        a.write(str(f"{list[i]}  --> on {time.ctime()}\n"))
        print(str(f"{list[i]}  --> on {time.ctime()}\n"))
        
        i += 1


