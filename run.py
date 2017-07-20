import sys
import getpass
if not "C:/Users/"+getpass.getuser()+"/Documents/gitfolder/Gui_miniGame" in sys.path:
    sys.path.append("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/Gui_miniGame")
import JKPgame.Gui_mini as Gui
reload (Gui)