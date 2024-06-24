#custom vscode commands go here
app: vscode
-
#Running
python run: user.vscode("python.execInTerminal")

#Diff Viewing
change next: user.vscode("editor.action.dirtydiff.next")
change last: user.vscode("editor.action.dirtydiff.previous")
change chuck: user.vscode("git.revertSelectedRanges")
file diff: user.vscode("git.openChange")

#Searching
# Cursorless magic: actions_custom.csv > `search, search.action.openNewEditor`
searcher [<command>]:
    user.vscode("search.action.openNewEditor")
    insert(command or "")
searchee [<command>]:
    user.vscode("search.action.openNewEditorToSide")
    insert(command or "")

#Explorer
(outline | explorer) rename: key("f2")
file rename: user.vscode("fileutils.renameFile")

#File navigation from editor
file next [<number_small>]:
    user.vscode("workbench.files.action.showActiveFileInExplorer")
    key("down:{number_small or 1} enter")

file last [<number_small>]:
    user.vscode("workbench.files.action.showActiveFileInExplorer")
    key("up:{number_small or 1} enter")

