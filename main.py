from optparse import OptionParser
from utils.fshandler import Target
from MyBot.base import app

if __name__=="__main__":
    parser = OptionParser()
    w = Target()
    app.runDevServer()
    w.run()
