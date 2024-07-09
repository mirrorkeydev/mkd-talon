from talon import Module

from .sheet_captures import Cell

mod = Module()

mod.apps.google_sheets = r"""
tag: browser
browser.host: docs.google.com
browser.path: /^/spreadsheets/.*/
"""
mod.apps.google_sheets = r"""
app.name: Sheets
"""

@mod.action_class
class Actions:
    def select_cell(cell: Cell):
        """Selects the cell, without placing the cursor inside."""
