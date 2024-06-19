from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
"""

@ctx.action_class("user")
class UserActions:
    # NOTE: you need Rectangle for these to work.
    def move_window_to_next_display():
        actions.key("ctrl-alt-cmd-right")

    def move_window_to_last_display():
        actions.key("ctrl-alt-cmd-left")

    def snap_window_full():
        actions.key("shift-cmd-up")

    def snap_window_center():
        actions.key("ctrl-alt-c")