#######################################################     
# grab the main screenshot with tabs
def grab_visor():
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

    grab_screen()

    close_tab()
    close_tab()
    close_tab()

#######################################################     
# grab the main screenshot with tabs
def grab_main():
    new_tab()
    resize(740, 480)
    new_tab()
    click("../../shared/applications-icon.png")
    ensure_view("icon")
    new_tab()
    click("../../shared/downloads-item.png")
    select_prev_tab()
    grab_window()
    resize_center(880, 548)
    grab_screen()

    close_tab()
    close_tab()
    close_tab()

#######################################################     
# grab the dual-mode screenshot
def grab_dual_mode():
    new_tab()
    resize(740, 480)
    new_tab()
    click("../../shared/binaryage-item.png")
    ensure_view("list")

    new_tab()
    click("../../shared/website-item.png")
    ensure_view("list")

    # enter dual mode
    select_prev_tab()
    type("u", KEY_CMD)

    grab_dual_window()
    resize_center(880, 548)
    grab_screen()
    
    # exit dual mode
    type("u", KEY_CMD)
    
    close_tab()
    close_tab()
    
def grab_folders_on_top():
    resize(740, 480)
    click("../../shared/binaryage-item.png")
    ensure_view("list")
    
    # grab window with folders on top
    grab_window()
    resize_center(880, 548)
    grab_screen()

def grab_show_system_files():
    resize(740, 480)
    click("../../shared/macintosh-hd-icon.png")
    ensure_view("list")

    # grab window with system files
    toggle_system_files()
    grab_window()
    resize_center(880, 548)
    grab_screen()

    # return to initial state
    toggle_system_files()

#######################################################     
    
switchApp("Finder")

grab_visor()
grab_main()
grab_dual_mode()
grab_folders_on_top()
grab_show_system_files()