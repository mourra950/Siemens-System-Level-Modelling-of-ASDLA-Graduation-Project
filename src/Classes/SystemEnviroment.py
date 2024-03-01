import os
import sys
class SysEnv:
    def __init__(self) -> None:
        print("Sys ENV Class")
        self.basedir = os.path.dirname(__file__)
        self.publicdir = os.path.normpath(os.path.join(self.basedir,'../../public/'))
        self.srcdir = os.path.normpath(os.path.join(self.basedir,'./../'))