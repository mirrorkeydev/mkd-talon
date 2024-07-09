from dataclasses import dataclass

from talon import Module, actions

mod = Module()

@dataclass
class Cell:
    column: str
    row: int

@mod.capture(rule="<user.letters> <user.number_string>")
def cell(m) -> Cell:
    """A spreadsheet cell."""
    return Cell(column=m.letters, row=m.number_string)
