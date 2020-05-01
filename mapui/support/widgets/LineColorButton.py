from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg 

class LineColorButton(qtw.QToolButton):
    def __init__(self, color=qtg.QColor(0,0,0)):
        super(LineColorButton, self).__init__()
        
        self.setFixedHeight(30)
        self.layout = qtw.QHBoxLayout()
        self.btnLayout = qtw.QHBoxLayout()
        self.spinLayout = qtw.QHBoxLayout()

        btn = ShowColor(qtg.QColor(255,0,0), 1, self.height())
        self.btnLayout.addWidget(btn)
        self.clicked.connect(self.chooseColor)
        self.layout.addLayout(self.btnLayout)

        #Set up the spin control properties...
        self.spinner = qtw.QDoubleSpinBox()
        self.spinner.setFixedWidth(55)
        self.spinner.setMinimum(.25)
        self.spinner.setMaximum(99.50)
        self.spinner.setSingleStep(.25)
        #Make sure the background is transparent...
        pal = self.spinner.palette()
        pal.setColor(9, qtg.QColor(222,0,0, 1))
        self.spinner.setPalette(pal)
        self.spinner.valueChanged.connect(self.valueChanged)
        self.spinLayout.addWidget(self.spinner)
        self.layout.addLayout(self.spinLayout)

        self.setLayout(self.layout)
        self.setFixedWidth(110) 
        self.setCurrentLineColor(color)

    def valueChanged(self):
        self.setCurrentLineWeight(self.spinner.value())
        self.paintLine() 

    def chooseColor(self):
        cChooser = qtw.QColorDialog(self)  
        cChooser.setCurrentColor(self.getCurrentLineColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:
            self.setCurrentLineColor(cChooser.selectedColor())
            self.paintLine()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None: 
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout()) 

    def paintLine(self):
        self.clearLayout(self.btnLayout)
        self.btnLayout.addWidget(ShowColor(self.getCurrentLineColor(), self.spinner.value(),self.height()))

    def setCurrentLineColor(self, color):
        self.__lineColor = color 
        self.paintLine() 

    def getCurrentLineColor(self):
        return self.__lineColor

    def setCurrentLineWeight(self, weight):
        self.__lineWeight = weight 
        self.spinner.setValue(weight)

    def getCurrentLineWeight(self):
        return self.__lineWeight

###########################################################################################################################
#This class is responsible for painting the rectangle on the button.
###########################################################################################################################
class ShowColor(qtw.QWidget):
    def __init__(self, newBorderColor, width, h):
        super(ShowColor, self).__init__()
        self.newFillColor = newBorderColor 
        self.newBorderColor = newBorderColor 
        self.width = width
        self.h = h
        self.update()
        
    def paintEvent(self, e):
        painter = qtg.QPainter()
        painter.begin(self)
        self.__drawRectangle(painter)        
        painter.end()

    def __drawRectangle(self,p):
        pen = qtg.QPen(self.newBorderColor)
        #Exagerate the width for display puposes...
        pen.setWidth(self.width * 1.5)
        p.setPen(pen)
        p.setBrush(self.newBorderColor)
        p.drawLine(5,10,45,10)
