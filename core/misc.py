from talon import Module, ui
import os

mod = Module()

@mod.action_class
class Actions:
    def restart_talon(): "Reboots talon."
    def quit_talon():
        "Quits talon."
        talon_app = ui.apps(pid=os.getpid())[0]
        talon_app.quit()
