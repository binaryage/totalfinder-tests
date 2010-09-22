import time

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
    
#######################################################     
# grab the main screenshot with tabs
def grab_main():
    new_tab()
    click("../../shared/applications-icon.png")
    ensure_view("icon")
    new_tab()
    click("../../shared/downloads-item.png")
    select_prev_tab()
    grab_window()

    close_tab()
    close_tab()

#######################################################     
# grab the main screenshot with tabs
def grab_visor():
    close_tab()
    toggle_visor()

    new_tab()
    click("../../shared/applications-icon.png")
    ensure_view("list")
    new_tab()
    click("../../shared/downloads-item.png")
    select_prev_tab()
    grab_window()
    
    hover("../../shared/finder-dock-icon.png")
    take_shot()

    close_tab()
    close_tab()
    close_tab()

    new_tab()

#######################################################     
# grab the dual-mode screenshot
def grab_dual_mode():
    new_tab()
    click("../../shared/binaryage-item.png")
    ensure_view("list")

    new_tab()
    click("../../shared/website-item.png")
    ensure_view("column")

    # enter dual mode
    select_prev_tab()
    type("u", KEY_CMD)

    grab_dual_window()
    
    # exit dual mode
    type("u", KEY_CMD)
    
    close_tab()
    close_tab()
    
def grab_folders_on_top():
    resize(450, 400)
    
    click("../../shared/binaryage-item.png")
    ensure_view("list")
    
    # grab window with folders on top
    grab_window()
    
    # grab window without folders on top
    toggle_folders_on_top()
    grab_window()
    
    # return to initial state
    toggle_folders_on_top()

def grab_show_system_files():
    resize(450, 400)

    click("../../shared/binaryage-item.png")
    ensure_view("list")

    # grab window without system files
    grab_window()

    # grab window with system files
    toggle_system_files()
    grab_window()

    # return to initial state
    toggle_system_files()

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
        sleep(1)
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
    
switchApp("Finder")

grab_main()
grab_visor()
grab_dual_mode()
grab_folders_on_top()
grab_show_system_files()
grab_main_menu()
grab_menus()
grab_preferences()