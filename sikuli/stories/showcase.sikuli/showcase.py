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
    ensure_view("list")

    # enter dual mode
    select_prev_tab()
    type("u", KEY_CMD)

    grab_dual_window()
    
    # exit dual mode
    type("u", KEY_CMD)
    
    close_tab()
    close_tab()
    
def grab_folders_on_top():
    click("../../shared/binaryage-item.png")
    ensure_view("list")
    
    # grab window with folders on top
    grab_window()

def grab_show_system_files():
    click("../../shared/macintosh-hd-icon.png")
    ensure_view("list")

    # grab window with system files
    toggle_system_files()
    grab_window()

    # return to initial state
    toggle_system_files()

#######################################################     
    
switchApp("Finder")

grab_main()
grab_visor()
grab_dual_mode()
grab_folders_on_top()
grab_show_system_files()