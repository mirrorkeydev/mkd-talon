not mode: sleep
-

parrot(tongue_click):
	core.repeat_command(1)

# # My cluck and palette click sound exactly the same
# parrot(cluck):
# 	user.move_cursor_to_gaze_point()
# parrot(palate_click):
# 	user.move_cursor_to_gaze_point()


parrot(hiss):
	user.noise_debounce("hiss", true)

parrot(hiss:stop):
	user.noise_debounce("hiss", false)

parrot(shush):
	user.noise_debounce("shush", true)

parrot(shush:stop):
	user.noise_debounce("shush", false)
