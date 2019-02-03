import sys, os
INTERP = "/home/dh_7u75hd/test-app.devhed.com/test_app_ve/bin/python"
#INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from app_entry import entry_point as application

