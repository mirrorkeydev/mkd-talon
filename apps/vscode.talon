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
searcher: user.vscode("search.action.openNewEditorToSide")
