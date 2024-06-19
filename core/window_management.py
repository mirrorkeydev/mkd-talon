from talon import Module

mod = Module()

@mod.action_class
class Actions:
    def move_window_to_next_display(): "Moves window to next display."
    def move_window_to_last_display(): "Moves window to last display."
    def snap_window_full(): "Full screens the current window."
    def snap_window_center(): "Centers the current window."
    def snap_window_down(): "Un-maximizes (not necessarily minimizes) the window."
    def snap_window_up(): "Maximizes the window."