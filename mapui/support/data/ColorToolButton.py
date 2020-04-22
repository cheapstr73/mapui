from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 

###########################################################################################################################
#This class will subclass the QToolButton control to display a colored box (to represent the current color) and a drop
#menu to allow for selecting a new color for both the fill and the outline of the box. This is a slightly more compact
#way of allowing the user to select colors and outlines for symbology.
###########################################################################################################################
class ColorToolButton(qtw.QToolButton):
    #Class constructor...
    def __init__(self, fill=qtg.QColor(0,0,0), border=qtg.QColor(0,0,0)):
        super(ColorToolButton, self).__init__()
        self.__CurrentFillColor  = fill
        self.__CurrentBorderColor = border 

        #Set up couple of icons to show in the drop menu
        self.fillIcon = qtg.QIcon('./support/icons/color2.png')
        self.borderIcon = qtg.QIcon('./support/icons/color3.png') 

        #Create a new menu and add menu actions..
        menu = qtw.QMenu()       
        self.chooseFillAction = qtw.QAction(self.fillIcon, "Choose Fill", self)
        self.chooseBorderAction = qtw.QAction(self.borderIcon, "Choose Border", self)
        menu.addAction(self.chooseFillAction)
        menu.addAction(self.chooseBorderAction)

        #Set the functions to call when the menu item is selected
        self.chooseFillAction.triggered.connect(self.ChooseFillColor)
        self.chooseBorderAction.triggered.connect(self.ChooseBorderColor)    
        self.setPopupMode(qtw.QToolButton.MenuButtonPopup)
        self.setMenu(menu)

        #Create a layout to draw the colored box in
        self.cLayout = qtw.QHBoxLayout()  
        self.colorBox = ShowColor(self.__CurrentFillColor, self.__CurrentBorderColor)
        self.cLayout.addWidget(self.colorBox)
        self.setLayout(self.cLayout)  


    def setCurrentFillColor(self, fc):
        self.__CurrentFillColor = fc 
        self.PaintColor() 

    def getCurrentFillColor(self):
        return self.__CurrentFillColor  

    def setCurrentBorderColor(self, bc):
        self.__CurrentBorderColor = bc
        self.PaintColor()
    
    def getCurrentBorderColor(self):
        return self.__CurrentBorderColor

    def disableMenuItem(self, idx):
        pass
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

    def ChooseFillColor(self):
        cChooser = qtw.QColorDialog(self)    
        cChooser.setCurrentColor(self.getCurrentFillColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:            
            self.setCurrentFillColor(cChooser.selectedColor())
            self.PaintColor()         
         
    def ChooseBorderColor(self):
        cChooser = qtw.QColorDialog(self)  
        cChooser.setCurrentColor(self.getCurrentBorderColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:
            self.setCurrentBorderColor(cChooser.selectedColor())
            self.PaintColor()

    def PaintColor(self):
        self.clearLayout(self.cLayout)
        self.colorBox = ShowColor(self.getCurrentFillColor(), self.getCurrentBorderColor())
        self.cLayout.addWidget(self.colorBox)

###########################################################################################################################
#This class is responsible for painting the rectangle on the button.
###########################################################################################################################
class ShowColor(qtw.QWidget):
    def __init__(self, newFillColor, newBorderColor):
        super(ShowColor, self).__init__()
        self.newFillColor = newFillColor 
        self.newBorderColor = newBorderColor 
        self.update()
        
    def paintEvent(self, e):
        painter = qtg.QPainter()
        painter.begin(self)
        self.__drawRectangle(painter)
        painter.end()

    def __drawRectangle(self,p):
        p.setPen(self.newBorderColor)
        p.setBrush(self.newFillColor)
        p.drawRect(0,0,20,17) 
    
        