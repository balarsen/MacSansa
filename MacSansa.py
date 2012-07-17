#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys

from PySide import QtGui, QtCore

from Sansa import Ui_MainWindow


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText('playlist1.m3u')
        self.ui.pushButtonOK.clicked.connect(self.makePlaylist)
        self.ui.pushButtonCancel.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
    def makePlaylist(self):
        """
        write out the file
        """
        print sys.argv
        if len(sys.argv) > 1:
            with open(os.path.join(os.path.expanduser('~'), 'Desktop', self.ui.lineEdit.text()), 'w') as fp:
                fp.write('#EXTM3U')
                fp.write('\n')
                for v in sys.argv[1:]:                    
                    fp.write(v)
                    fp.write('\n')
            QtCore.QCoreApplication.instance().quit

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
