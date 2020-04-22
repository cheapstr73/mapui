from PyQt5 import QtGui as qtg
class gmtMapOptions():
    def __init__(self):
        self.PageHeight = 8.5
        self.PageWidth = 11.0
        self.PageSizeUnit = 'Inches'
        self.ScalebarInterval = 10
        self.ScalebarLabelX = None
        self.ScalebarLabelY = None
        self.ScalebarPositioning = "Bottom Left"
        self.ScalebarHeight = .2
        self.ScalebarWidth = 6.0
        self.ScalebarSizeUnit = 'Inches'
        self.ScalebarOffsetUnit = 'Inches'
        self.ScalebarOffsetX = 1.0
        self.ScalebarOffsetY = 1.0
        self.ScalebarXPos = 3.5
        self.ScalebarYPos = .6
        self.ScalebarPosUnit = 'Inches'
        self.ScalebarOrientation = 'h'
        self.SymbologyLevel = 0
        self.SymbologyShape = 'Circle'
        self.SymbologySize = 4.0
        self.SymbologySizeUnit = 'Points'
        self.SymbologyFillColor = qtg.QColor(0,0,0)
        self.SymbologyBorderColor = qtg.QColor(0,0,0)

    @property 
    def PageHeight(self):
        return self.__PageHeight
    @PageHeight.setter 
    def PageHeight(self, pageHeight = 8.5):
        self.__PageHeight = pageHeight

    @property 
    def PageSizeUnit(self):
        return self.__PageSizeUnit.title() 
    @PageSizeUnit.setter 
    def PageSizeUnit(self, pageSizeUnit = 'Inches'):
        self.__PageSizeUnit = pageSizeUnit.lower() 

    @property 
    def PageWidth(self):
        return self.__PageWidth
    @PageWidth.setter 
    def PageWidth(self, pageWidth = 11.0):
        self.__PageWidth = pageWidth 
    
    @property 
    def ScalebarInterval(self):
        return self.__ScalebarInterval 
    @ScalebarInterval.setter 
    def ScalebarInterval(self, interval):
        self.__ScalebarInterval = interval 

    @property 
    def ScalebarLabelX(self):
        return self.__ScalebarLabelX
    @ScalebarLabelX.setter 
    def ScalebarLabelX(self, xLabel):
        self.__ScalebarLabelX = xLabel 

    @property 
    def ScalebarLabelY(self):
        return self.__ScalebarLabelY
    @ScalebarLabelY.setter 
    def ScalebarLabelY(self, yLabel):
        self.__ScalebarLabelY = yLabel    

    @property 
    def ScalebarHeight(self):
        return self.__ScalebarHeight 
    @ScalebarHeight.setter 
    def ScalebarHeight(self, height):
        self.__ScalebarHeight = height 

    @property 
    def ScalebarSizeUnit(self):
        return self.__ScalebarSizeUnit.title()
    @ScalebarSizeUnit.setter 
    def ScalebarSizeUnit(self, unit):
        self.__ScalebarSizeUnit = unit.lower()

    @property 
    def ScalebarOffsetUnit(self):
        return self.__ScalebarOffsetUnit
    @ScalebarOffsetUnit.setter 
    def ScalebarOffsetUnit(self, unit):
        self.__ScalebarOffsetUnit = unit

    @property 
    def ScalebarOffsetX(self):
        return self.__ScalebarOffsetX 
    @ScalebarOffsetX.setter 
    def ScalebarOffsetX(self, offset):
        self.__ScalebarOffsetX = offset

    @property 
    def ScalebarOffsetY(self):
        return self.__ScalebarOffsetY
    @ScalebarOffsetY.setter 
    def ScalebarOffsetY(self, offset):
        self.__ScalebarOffsetY = offset
    
    @property 
    def ScalebarOrientation(self):
        return self.__ScalebarOrientation
    @ScalebarOrientation.setter 
    def ScalebarOrientation(self, orientation):
        self.__ScalebarOrientation = orientation

    @property
    def ScalebarPositioning(self):
        return self.__ScalebarPositioning 
    @ScalebarPositioning.setter 
    def ScalebarPositioning(self, position):
        self.__ScalebarPositioning = position 

    @property 
    def ScalebarWidth(self):
        return self.__ScalebarWidth
    @ScalebarWidth.setter 
    def ScalebarWidth(self, width):
        self.__ScalebarWidth = width 
    
    @property 
    def ScalebarXPos(self):
        return self.__ScalebarXPos 
    @ScalebarXPos.setter 
    def ScalebarXPos(self, xPos):
        self.__ScalebarXPos = xPos

    @property 
    def ScalebarYPos(self):
        return self.__ScalebarYPos 
    @ScalebarYPos.setter 
    def ScalebarYPos(self, yPos):
        self.__ScalebarYPos = yPos

    @property 
    def ScalebarPosUnit(self):
        return self.__ScalebarPosUnit.title()
    @ScalebarPosUnit.setter 
    def ScalebarPosUnit(self, unit):
        self.__ScalebarPosUnit = unit.lower()
    
    @property 
    def SymbologyFillColor(self):
        return self.__SymbologyFillColor 
    @SymbologyFillColor.setter 
    def SymbologyFillColor(self, fill):
        self.__SymbologyFillColor = fill

    @property 
    def SymbologyBorderColor(self):
        return self.__SymbologyBorderColor 
    @SymbologyBorderColor.setter 
    def SymbologyBorderColor(self, border):
        self.__SymbologyBorderColor = border 

    @property
    def SymbologyLevel(self):
        return self.__SymbologyLevel
    @SymbologyLevel.setter 
    def SymbologyLevel(self, level):
        self.__SymbologyLevel = level

    @property
    def SymbologyShape(self):
        return self.__SymbologyShape
    @SymbologyShape.setter 
    def SymbologyShape(self, shape):
        self.__SymbologyShape = shape

    @property
    def SymbologySize(self):
        return self.__SymbologySize
    @SymbologySize.setter 
    def SymbologySize(self, size):
        self.__SymbologySize = size
    
    @property
    def SymbologySizeUnit(self):
        return self.__SymbologySizeUnit
    @SymbologySizeUnit.setter 
    def SymbologySizeUnit(self, sizeUnit):
        self.__SymbologySizeUnit = sizeUnit
    
