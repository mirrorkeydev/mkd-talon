disk: key(ctrl-s)
nope: edit.undo()

wipe word left:
    edit.extend_word_left()
    edit.delete()

wipe word right:
    edit.extend_word_right()
    edit.delete()