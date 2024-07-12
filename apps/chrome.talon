app: chrome
-
# Solution from https://superuser.com/a/338543
tab pop out:
    user.chrome_mod("l")
    sleep(50ms)
    user.chrome_mod("c")
    user.chrome_mod("w")
    user.chrome_mod("n")
    user.chrome_mod("v")
    key(enter)

tab close <user.rango_target>:
    tab_title = user.rango_command_without_target("getBareTitle")
    user.rango_command_with_target("activateTab", rango_target)
    user.tab_close_wrapper()
    user.rango_command_without_target("focusTabByText", tab_title)
    
    #user.rango_command_without_target("saveReferenceForActiveElement", "current_tab")
    #user.rango_run_action_on_reference("activateTab", "current_tab")
