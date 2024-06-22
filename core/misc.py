from talon import Module

mod = Module()

@mod.action_class
class Actions:
    def restart_talon(): "Reboots talon."
