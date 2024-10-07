from talon import Context, ui
from multiprocessing import Process
import os, re, subprocess, multiprocessing

ctx = Context()
ctx.matches = r"""
os: mac
"""
    
@ctx.action_class("user")
class UserActions:
    # Doesn't work, just quits talon.
    def restart_talon():
        talon_app = ui.apps(pid=os.getpid())[0]
        #mac_app_name = re.match(r"(\/Applications.+\.app)", talon_app.exe)[1]
        #open_command = f"sleep 2 && open '${mac_app_name}'"

        # Talon will not launch if Talon is already running. Thus we try to spawn
        # a new subprocess that will sleep for two seconds (waiting for us to
        # kill this talon) and then attempt to open talon.

        # Failed attempts graveyard:

        # Multiprocessing:
        #process = multiprocessing.Process(target=os.system, args=([open_command]), daemon=False)
        #process.start()
        
        # Subprocess:
        #subprocess.Popen(open_command, shell=True)
        
        talon_app.quit()
