from talon import Module, actions, ui

mod = Module()

@mod.action_class
class Actions:
    def mouse_move_center_window():
        """Move the mouse cursor to the center of the active window"""
        rect = ui.active_window().rect
        actions.mouse_move(rect.center.x, rect.center.y)
