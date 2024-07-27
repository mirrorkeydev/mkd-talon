disk: edit.save()
nope: edit.undo()

wipe word [left]:
    edit.extend_word_left()
    edit.delete()

wipe word right:
    edit.extend_word_right()
    edit.delete()

talon (restart | reboot): user.restart_talon()
talon quit: user.quit_talon()