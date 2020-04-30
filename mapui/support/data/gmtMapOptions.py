from PyQt5 import QtGui as qtg
from support.data.gmtFont import gmtFont

class gmtMapOptions():
    def __init__(self):
        self.PageHeight = 8.5
        self.PageWidth = 11.0
        self.MapClassificationAdd = False
        self.MapClassification = gmtFont()
        self.MapClassificationOffsetX = 0.0
        self.MapClassificationOffsetY = 0.0
        self.MapClassificationOffsetUnit = 'Inches'
        self.MapTitleAdd = True
        self.MapTitle = gmtFont()
        self.MapTitleOffsetX = 0.0
        self.MapTitleOffsetY = 0.0
        self.MapTitleOffsetUnit = 'Inches'
        self.PageSizeUnit = 'Inches'
        self.ScalebarInterval = 10
        self.ScalebarLabelX = None
        self.ScalebarLabelY = None
        self.ScalebarPositioning = 'Bottom Left'
        self.ScalebarHeight = .15
        self.ScalebarWidth = 5.0
        self.ScalebarSizeUnit = 'Inches'
        self.ScalebarOffsetUnit = 'Inches'
        self.ScalebarOffsetX = 1.0
        self.ScalebarOffsetY = 1.0
        self.ScalebarXPos = 3.5
        self.ScalebarYPos = .6
        self.ScalebarPosUnit = 'Inches'
        self.ScalebarOrientation = 'h'
        self.ScalebarIlluminate = False
        self.SymbologyLevel = 0
        self.SymbologyShape = 'Circle'
        self.SymbologySize = 4.0
        self.SymbologySizeUnit = 'Points'
        self.SymbologyFillColor = qtg.QColor(255,0,0)
        self.SymbologyBorderColor = qtg.QColor(0,0,0) 
        self.CoastlineFillColor = qtg.QColor(255,255,255)
        self.CoastlineBorderColor = qtg.QColor(190,190,190)
        self.CoastlineNationalBoundaryColor = qtg.QColor(190,190,190)
        self.CoastlineNationalBoundaryWeight = 1
        self.CoastlineNationalBoundaryType = 'National Boundaries'
        self.CoastlineRiverType = 'None'
        self.CoastlineRiverColor = qtg.QColor(174,211,239)
        self.CoastlineRiverWeight = .5

    @property
    def CoastlineFillColor(self):
        return self.__CoastlineFillColor
    @CoastlineFillColor.setter 
    def CoastlineFillColor(self, fill):
        self.__CoastlineFillColor = fill

    @property
    def CoastlineBorderColor(self):
        return self.__CoastlineBorderColor
    @CoastlineBorderColor.setter 
    def CoastlineBorderColor(self, borderColor):
        self.__CoastlineBorderColor = borderColor
    
    @property 
    def CoastlineNationalBoundaryType(self):
        return self.__CoastlineNationalBoundaryType
    @CoastlineNationalBoundaryType.setter 
    def CoastlineNationalBoundaryType(self, tp):
        self.__CoastlineNationalBoundaryType = tp

    @property 
    def CoastlineNationalBoundaryColor(self):
        return self.__CoastlineNationalBoundaryColor
    @CoastlineNationalBoundaryColor.setter 
    def CoastlineNationalBoundaryColor(self, color):
        self.__CoastlineNationalBoundaryColor = color

    @property 
    def CoastlineNationalBoundaryWeight(self):
        return self.__CoastlineNationalBoundaryWeight
    @CoastlineNationalBoundaryWeight.setter 
    def CoastlineNationalBoundaryWeight(self, w):
        self.__CoastlineNationalBoundaryWeight = w

    @property 
    def CoastlineRiverType(self):
        return self.__CoastlineRiverType
    @CoastlineRiverType.setter 
    def CoastlineRiverType(self, tp):
        self.__CoastlineRiverType = tp

    @property 
    def CoastlineRiverColor(self):
        return self.__CoastlineRiverColor 
    @CoastlineRiverColor.setter 
    def CoastlineRiverColor(self, color):
        self.__CoastlineRiverColor = color 

    @property 
    def CoastlineRiverWeight(self):
        return self.__CoastlineRiverWeight 
    @CoastlineRiverWeight.setter 
    def CoastlineRiverWeight(self, w):
        self.__CoastlineRiverWeight = w

    @property 
    def MapClassificationAdd(self):
        return self.__MapClassificationAdd
    @MapClassificationAdd.setter 
    def MapClassificationAdd(self, add):
        self.__MapClassificationAdd = add 

    @property 
    def MapClassification(self):
        return self.__MapClassification
    @MapClassification.setter 
    def MapClassification(self, classification):
        self.__MapClassification = classification

    @property
    def MapClassificationOffsetX(self):
        return self.__MapClassificationOffsetX 
    @MapClassificationOffsetX.setter 
    def MapClassificationOffsetX(self, offset):
        self.__MapClassificationOffsetX = offset 

    @property
    def MapClassificationOffsetY(self):
        return self.__MapClassificationOffsetY
    @MapClassificationOffsetY.setter 
    def MapClassificationOffsetY(self, offset):
        self.__MapClassificationOffsetY = offset 

    @property
    def MapClassificationOffsetUnit(self):
        return self.__MapClassificationOffsetUnit
    @MapClassificationOffsetUnit.setter 
    def MapClassificationOffsetUnit(self, unit):
        self.__MapClassificationOffsetUnit = unit

    @property 
    def MapTitleAdd(self):
        return self.__MapTitleAdd 
    @MapTitleAdd.setter 
    def MapTitleAdd(self, add):
        self.__MapTitleAdd = add 

    @property 
    def MapTitle(self):
        return self.__MapTitle
    @MapTitle.setter 
    def MapTitle(self, title):
        self.__MapTitle = title

    @property 
    def MapTitleOffsetX(self):
        return self.__MapTitleOffsetX
    @MapTitleOffsetX.setter
    def MapTitleOffsetX(self, offset):
        self.__MapTitleOffsetX = offset
    
    @property 
    def MapTitleOffsetY(self):
        return self.__MapTitleOffsetY
    @MapTitleOffsetY.setter
    def MapTitleOffsetY(self, offset):
        self.__MapTitleOffsetY = offset

    @property 
    def MapTitleOffsetUnit(self):
        return self.__MapTitleOffsetUnit
    @MapTitleOffsetUnit.setter
    def MapTitleOffsetUnit(self, offset):
        self.__MapTitleOffsetUnit = offset

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
    def ScalebarIlluminate(self):
        return self.__ScalebarIlluminate 
    @ScalebarIlluminate.setter 
    def ScalebarIlluminate(self, i):
        self.__ScalebarIlluminate = i

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
    
