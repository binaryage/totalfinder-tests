# this file gets prepended before every sikuli script in stories dir by rakefile launcher

# sudo easy_install appscript

from sikuli import *
import time

KEY_ALT = 1
KEY_CMD = 2
KEY_CTRL = 4
KEY_META = 8
KEY_SHIFT = 16
KEY_WIN = 32

KEY_ENTER = 33
KEY_TAB = 34
KEY_ESC = 35
KEY_INSERT = 36
KEY_BACKSPACE = 37
KEY_DELETE = 38
KEY_CAPSLOCK = 39
KEY_SPACE = 40
KEY_F1 = 41
KEY_F2 = 42
KEY_F3 = 43
KEY_F4 = 44
KEY_F5 = 45
KEY_F6 = 46
KEY_F7 = 47
KEY_F8 = 48
KEY_F9 = 49
KEY_F10 = 50
KEY_F11 = 51
KEY_F12 = 52
KEY_F13 = 53
KEY_F14 = 54
KEY_F15 = 55
KEY_HOME = 56
KEY_END = 57
KEY_LEFT = 58
KEY_RIGHT = 59
KEY_DOWN = 60
KEY_UP = 61
KEY_PAGE_DOWN = 62
KEY_PAGE_UP = 63


class Button:
    LEFT = 1
    OTHER = 2
    RIGHT = 3
    
# override Sikuli version
def switchApp(name):
    import os
    import time
    os.system('osascript -e "tell application \\"'+name+'\\" to activate"')
    time.sleep(2)

def sys(cmd):
    import os
    import time
    os.system(cmd)
    time.sleep(1)
    
def sleep(n=0.2):
    import time
    time.sleep(n)

def take_shot():
    type("4", KEY_CMD + KEY_SHIFT)
    type(" ")
    mouseDown(Button.LEFT)
    mouseUp(Button.LEFT)

# we need to do 2x screenshot with shadow to capture chrome+child windows
def grab_window():
    hover("../../shared/tab-plus.png")
    take_shot()
    hover("../../shared/search-box.png")
    take_shot()

# we need to do 3x screenshot with shadow to capture chrome+both child windows
def grab_dual_window():
    hover("../../shared/tab-plus.png")
    take_shot()

    # in dual mode we need to grab left and right finder windows
    o = findAll("../../shared/toolbar-back-forward.png")
    if o[0]:
        hover(o[0])
        take_shot()

    if o[1]:
        hover(o[1])
        take_shot()

def ensure_view(type="list"):
    o = findAll("../../shared/"+type+"-view-icon.png")
    for icon in o: # may be already selected
        click(icon)

def new_tab():
    type("t", KEY_CMD)
    sleep(1)

def close_tab():
    type("w", KEY_CMD)
    sleep(1)

def select_next_tab():
    type("]", KEY_CMD + KEY_SHIFT)

def select_prev_tab():
    type("[", KEY_CMD + KEY_SHIFT)

def resize(w, h):
    sys("osascript -e \"tell application \\\"Finder\\\" to set the bounds of the first window to {100, 100, "+str(100+w)+", "+str(100+h+28)+"}\"")

def toggle_folders_on_top():
    type(";", KEY_CMD + KEY_SHIFT)

def toggle_system_files():
    type(".", KEY_CMD + KEY_SHIFT)

def toggle_visor():
    type("`", KEY_ALT)
    sleep(2)        