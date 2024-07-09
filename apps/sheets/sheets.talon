app: google_sheets
-
tag(): browser # to enable rango in Sheet's PWA

# Navigation

row <user.number_string>: user.select_row(number_string)
col <user.letters>: user.select_column(letters)
# Ex: `call air two` selects A2
cell <user.cell>: user.select_cell(cell)
# Ex: `cell air two past bat fourteen` selects A2:B14
cell <user.cell_range>: user.select_cell_range(cell_range)

# Misc

please <user.prose>:
    key(alt-/)
    insert(prose)