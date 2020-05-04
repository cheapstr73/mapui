from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import uic
import sys 
###########################################################################################################################
#This class is the view for a simple working window
###########################################################################################################################

class working(qtw.QDialog):
    def __init__(self, *args, **kwargs):
        super(working, self).__init__(*args, **kwargs) 
        uic.loadUi('./support/interfaces/working.ui', self)   
        self.setModal(True)
        self.setFixedHeight(115)
        self.setFixedWidth(300)
        
    #Start the animated gif spinning
    def start(self):
        self.gif = qtg.QMovie('./support/icons/spinner3.gif')
        self.lbl_spinner.setMovie(self.gif)
        self.gif.start()
    #Stop the animated gif
    def stop(self):
        self.gif.stop()
        self.lbl_status.setText("Process Completed")
        
    #Update the label with new text    
    def write(self, text):
        self.lbl_status.setText(text) 

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = working()
    sys.exit(app.exec())