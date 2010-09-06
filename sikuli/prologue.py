# this file gets prepended before every sikuli script in stories dir by rakefile launcher

from sikuli import *

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
    