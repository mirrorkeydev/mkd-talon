from talon import Module, clip, actions
import re

from .sheet_captures import Cell, CellRange

mod = Module()

mod.apps.google_sheets = r"""
tag: browser
browser.host: docs.google.com
browser.path: /^/spreadsheets/.*/
"""
mod.apps.google_sheets = r"""
app.name: Sheets
"""

def get_current_location():
    actions.edit.copy()
    actions.sleep("100ms")
    location = clip.text()
    match = re.match(r"([A-Za-z]+)(\d+)", location)
    old_column = match.group(1)
    old_row = match.group(2)
    return [old_column, old_row]

@mod.action_class
class Actions:
    def select_row(row: int):
        """Maintaining the current column position, select the given row."""
        actions.user.chrome_mod("j")
        old_column, old_row = get_current_location()
        actions.insert(f"{old_column}{row}")
        actions.key("enter")

    def select_column(col: str):
        """Maintaining the current row position, select the given column."""
        actions.user.chrome_mod("j")
        old_column, old_row = get_current_location()
        actions.key("backspace")
        print(old_column, old_row)
        actions.insert(f"{col}{old_row}")
        actions.key("enter")

    def select_cell(cell: Cell):
        """Selects the cell, without placing the cursor inside."""
        actions.user.chrome_mod("j")
        actions.key("backspace")
        actions.sleep("50ms")
        actions.user.insert_formatted(cell.column, "ALL_CAPS")
        actions.insert(cell.row)
        actions.key("enter")

    def select_cell_range(cell_range: CellRange):
        """Selects the cell range, without placing the cursor inside."""
        actions.user.chrome_mod("j")
        actions.key("backspace")
        actions.sleep("50ms")
        actions.user.insert_formatted(cell_range.start.column, "ALL_CAPS")
        actions.insert(cell_range.start.row)
        actions.insert(":")
        actions.user.insert_formatted(cell_range.end.column, "ALL_CAPS")
        actions.insert(cell_range.end.row)
        actions.key("enter")
