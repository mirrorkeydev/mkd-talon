from talon import Context, ui
import os

ctx = Context()
ctx.matches = r"""
os: windows
"""

@ctx.action_class("user")
class UserActions:
    # From andreas-talon/core/talon_helpers/talon_helpers.py
    def restart_talon():
        talon_app = ui.apps(pid=os.getpid())[0]
        os.startfile(talon_app.exe)
        talon_app.quit()