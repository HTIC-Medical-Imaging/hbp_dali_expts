from datetime import datetime

class TicToc(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tic = datetime.now()
        return self

    def __exit__(self, type, value, traceback):
        self.toc = datetime.now()
        self.elapsed = self.toc - self.tic

    def __str__(self):
        return "%s: %s" % (self.name or 'Time', self.elapsed)