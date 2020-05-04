from PyQt5 import QtWidgets as qtw 
from PyQt5 import uic
import sys

###########################################################################################################################
#This class is the view for a simple about box window
###########################################################################################################################
class about(qtw.QDialog):
    def __init__(self, *args, **kwargs):
        super(about, self).__init__(*args, **kwargs) 
        uic.loadUi('./support/interfaces/about.ui', self) 
        
        #Keep from resizing...
        self.setFixedHeight(260)
        self.setFixedWidth(410)
        self.btn_close.clicked.connect(self.close)
        
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = about()
    sys.exit(app.exec())