from distutils.core import setup
import py2exe

setup(console=['game.pyw'],
      excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
      "pywin.dialogs", "pywin.dialogs.list",
      "Tkconstants","Tkinter","tcl"]
)
