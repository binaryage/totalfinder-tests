import time

switchApp("Finder")
type("t", KEY_CMD)
click("../../shared/binaryage-item.png")
click("../../shared/list-view-icon.png")
type("t", KEY_CMD)
click("../../shared/downloads-item.png")
type("[", KEY_CMD + KEY_SHIFT)

def take_shot():
    type("4", KEY_CMD + KEY_SHIFT)
    type(" ")
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

#######################################################     
# grab the dual-mode screenshot
# we need to do 3x screenshot with shadow to capture chrome+both child windows
def grab_dual_mode():
    # enter dual mode
    type("u", KEY_CMD)

    o = findAll("../../shared/website-item.png")
    click(o[1])
    o = findAll("../../shared/column-view-icon.png")
    click(o[1])
    
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
    
    # exit dual mode
    type("u", KEY_CMD)

#######################################################     
# main menu
def grab_main_menu():
    hover("../../shared/system-apple.png")
    take_shot()

#######################################################     
# do screens of menus
def grab_menus():
    def next_menu():
        press(KEY_RIGHT)
        hover("../../shared/selected-top-menu-item.png")
        take_shot()

    click("../../shared/system-apple.png")
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
        take_shot()
        
    switchApp("Finder")
    type(",", KEY_CMD)

    # Visor
    if exists("../../shared/pref-totalfinder-icon.png", 1):
        click("../../shared/pref-totalfinder-icon.png")
    else:
        # toolbar icon is hidden under expansion arrow
        click("../../shared/pref-more-icon.png")
        click("../../shared/pref-more-menu.png")
        hover("../../shared/pref-more-icon.png")
        
    take_shot()
    
    step() # Asepsis
    step() # Tweaks
    step() # About

#######################################################     
    
grab_main()
grab_dual_mode()
grab_main_menu()
grab_menus()
grab_preferences()