app: google_sheets
-
tag(): browser # to enable rango in Sheet's PWA

# Ex: `take air two` selects A2
take <user.cell>: user.select_cell(cell)

# Ex: `take air two past bat 4` selects A2:B4
take <user.cell_range>: user.select_cell_range(cell_range)

please <user.prose>:
    key(alt-/)
    insert(prose)