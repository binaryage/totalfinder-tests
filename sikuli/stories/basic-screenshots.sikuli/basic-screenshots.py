import time

switchApp("Finder")
time.sleep(0.5)

def take_shot():
    type("4", KEY_CMD + KEY_SHIFT)
    type(" ")
    time.sleep(0.2)
    mouseDown(Button.LEFT)
    mouseUp(Button.LEFT)

#######################################################     
# grab the main screenshot with tabs
# we need to do 2x screenshot with shadow to capture chrome+child windows
def grab_main():
    hover("../../shared/tab-plus.png")
    take_shot()
    hover("../../shared/search-box.png")
    take_shot()
    time.sleep(0.5)

#######################################################     
# grab the dual-mode screenshot
# we need to do 3x screenshot with shadow to capture chrome+both child windows
def grab_dual_mode():
    # enter dual mode
    type("u", KEY_CMD)

    hover("../../shared/tab-plus.png")
    take_shot()

    # in dual mode we need to grab left and right finder windows
    o = findAll("../../shared/search-box.png")
    if o[0]:
        hover(o[0])
        take_shot()

    if o[1]:
        hover(o[1])
        take_shot()
    
    # exit dual mode
    type("u", KEY_CMD)


#######################################################     
# do screens of menus
def grab_menus():
    def next_menu():
        press(KEY_RIGHT)
        time.sleep(0.2)
        hover("../../shared/selected-top-menu-item.png")
        time.sleep(0.2)
        take_shot()

    click("../../shared/system-apple.png")
    time.sleep(1)
    hover("../../shared/next-menu.png")

    next_menu() # Finder menu
    next_menu() # File menu
    next_menu() # Edit menu
    next_menu() # View menu
    next_menu() # Go menu
    next_menu() # Window menu
    next_menu() # Help menu

    press(KEY_ESC)

#######################################################     
# shots of TotalFinder preference panes
def grab_preferences():
    def step():
        click("../../shared/pref-next-page.png")
        time.sleep(0.5)
        take_shot()
        
    time.sleep(1)
    type(",", KEY_CMD)
    time.sleep(1)

    switchApp("Finder")

    # Visor
    click("../../shared/pref-totalfinder-icon.png")
    time.sleep(0.5)
    take_shot()
    
    step() # Asepsis
    step() # Tweaks
    step() # About

#######################################################     
    
grab_main()
grab_dual_mode()
grab_menus()
grab_preferences()