from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 

class ColorButton(qtw.QPushButton):
    #Class constructor...
    def __init__(self, fill=qtg.QColor(117,161,221)):
        super(ColorButton, self).__init__()
        self.__CurrentFillColor  = fill
        self.setFixedWidth(55)
        #Create a layout to draw the colored box in
        self.cLayout = qtw.QHBoxLayout()  
        self.colorBox = ShowColor(self.__CurrentFillColor)
        self.cLayout.addWidget(self.colorBox)
        self.setLayout(self.cLayout)

        self.pressed.connect(self.ChooseFillColor) 
        
    def ChooseFillColor(self): 
        cChooser = qtw.QColorDialog(self)    
        cChooser.setCurrentColor(self.getCurrentFillColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:            
            self.setCurrentFillColor(cChooser.selectedColor())
            self.PaintColor()     
  
    def setCurrentFillColor(self, fc):
        self.__CurrentFillColor = fc 
        self.PaintColor() 

    def getCurrentFillColor(self):
        return self.__CurrentFillColor 
       
    ###########################################################################################################################
    #This will clear the current colored box in order to make room for a new one...
    ###########################################################################################################################
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None: 
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def PaintColor(self):
        self.clearLayout(self.cLayout)
        self.colorBox = ShowColor(self.getCurrentFillColor())
        self.cLayout.addWidget(self.colorBox) 
    
###########################################################################################################################
#This class is responsible for painting the rectangle on the button.
###########################################################################################################################
class ShowColor(qtw.QWidget):
    def __init__(self,  newFillColor):
        super(ShowColor, self).__init__()
        self.newFillColor = newFillColor 
        self.update()
        
    def paintEvent(self, e):
        painter = qtg.QPainter()
        painter.begin(self)
        self.__drawRectangle(painter)        
        painter.end()

    def __drawRectangle(self,p):
        p.setPen(qtg.QColor(180,180,180))
        p.setBrush(self.newFillColor)
        p.drawRect(1,1,39,16) 
