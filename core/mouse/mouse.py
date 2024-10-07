#https://github.com/AndreasArvidsson/andreas-talon/blob/beff7466031f3cca9acf6658e8247ec2ef3a9205/core/mouse/mouse.py
from talon import Module, actions, ui

mod = Module()

@mod.action_class
class Actions:
    def mouse_move_center_window():
        """Move the mouse cursor to the center of the active window"""
        rect = ui.active_window().rect
        actions.mouse_move(rect.center.x, rect.center.y)
