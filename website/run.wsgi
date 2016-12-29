import os 
import sys 
 
sys.path.append('/home/khannegan/apps/website') 
sys.path.append('/home/khannegan/apps/website/lib/python2.7/site-packages')

activate_this = "/home/khannegan/apps/website/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from home import app as application
print "about to launch..."
if __name__ == '__main__':
    app.run()
