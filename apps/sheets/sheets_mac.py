from talon import Context, actions

from .sheet_captures import Cell, CellRange

ctx = Context()

ctx.matches = r"""
os: mac
app: google_sheets
"""

@ctx.action_class("user")
class SheetsActions:
    def select_cell(cell: Cell):
        actions.key("cmd-j")
        actions.key("backspace")
        actions.sleep("50ms")
        actions.user.insert_formatted(cell.column, "ALL_CAPS")
        actions.insert(cell.row)
        actions.sleep("50ms")
        actions.key("enter")

    def select_cell_range(cell_range: CellRange):
        actions.key("cmd-j")
        actions.key("backspace")
        actions.sleep("50ms")
        actions.user.insert_formatted(cell_range.start.column, "ALL_CAPS")
        actions.insert(cell_range.start.row)
        actions.insert(":")
        actions.user.insert_formatted(cell_range.end.column, "ALL_CAPS")
        actions.insert(cell_range.end.row)
        actions.sleep("50ms")
        actions.key("enter")
