# defines the default app actions for windows

from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""

@ctx.action_class("user")
class UserActions:
    def move_window_to_next_display():
        actions.key("shift-super-left")

    def move_window_to_last_display():
        actions.key("shift-super-right")