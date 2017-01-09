import os 
import sys 
 
sys.path.append('/home/khannegan/apps/website') 
sys.path.append('/home/khannegan/apps/website/lib/python2.7/site-packages')

activate_this = "/home/khannegan/apps/website/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

import logging
logger = logging.getLogger()
hdlr = logging.FileHandler('/home/khannegan/apps/website/logs/server_scripts.log',mode='a', encoding=None, delay=False)
formatter = logging.Formatter('%(asctime)s - %(levelname)s -  %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
stream1 = logging.StreamHandler(stream=sys.stdout)
stream1.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream1)

def my_handler(type, value, traceback):
    logger.exception("Untrapped exception: {0}".format(str(value)))
    logger.error(format_exception(type, value, traceback))

# Install exception handler
sys.excepthook = my_handler

logging.info("Initializing home application through import of folder...")
from home import app as application
logging.info("Launching application...")
if __name__ == '__main__':
    app.run()
