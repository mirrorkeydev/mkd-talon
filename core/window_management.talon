display next: user.move_window_to_next_display()
display last: user.move_window_to_last_display()

snap full: user.snap_window_full()
snap center: user.snap_window_center()

snap down: user.snap_window_down()
snap up: user.snap_window_up()

snapper <number>:
    user.move_window_to_screen(number)
    user.snap_window_up()