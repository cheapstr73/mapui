from PyQt5 import QtGui as qtg
from support.data.gmtFont import gmtFont
###########################################################################################################################
#This class contains alot of properties to support the interface options. For clarity the initialization will call 
#seperate functions to initialize the controls on each tab. For each funcion, the control is initialized in the order
#that it appears on the page from top to bottom, left to right.
###########################################################################################################################
class gmtMapOptions():
    def __init__(self):
        self.setupMapPageTab()
        self.setupMapFrameTab()
        self.setupSymbologyTab()
        self.setupScalebarTab()     

    def setupMapPageTab(self):  
        #Media Size
        self.PageHeight = 8.5
        self.PageWidth = 11.0
        self.PageSizeUnit = 'Inches' 
        self.MapScaleFactor = .9
        
        #Add Title
        self.MapTitleAdd = True      
        self.MapTitle = gmtFont('Helvetica-Bold', 18, qtg.QColor(0,0,0), 'Map Title Here', 15, 0, 'Points')  #Pass in font face, font size, font color, text, X-Offset, Y-Offset, offset unit
        
        #Add Classification
        self.MapClassificationAdd = False
        self.MapClassification = gmtFont('Helvetica-Bold', 14, qtg.QColor(85,170,0), 'UNCLASSIFIED')#Pass in font face, font size, font color, and text

    def setupMapFrameTab(self):
        #Map Frame
        self.MapFrameType = 'Plain'    
        self.MapFrameWidth = 1.0
        self.MapFrameColor = qtg.QColor(0,0,0)
        
        #Frame Annotations (Grid Numbers)
        self.MapFrameFont = gmtFont('Helvetica', 10,qtg.QColor(0,0,0), None, 10, 0) #Pass in font face, font size, font color, No Text, X-Offset, Y-Offset
        
        #Gridlines
        self.GridlineWidth = .5      
        self.GridlineColor = qtg.QColor(0,0,0)
        self.GridlineIntervalX = 10 
        self.GridlineIntervalY = 10
        
        #Grid Ticks
        self.GridTicks = False
        self.GridTickWidth = .5 
        self.GridTickColor = qtg.QColor(0,0,0)
        self.GridTickIntervalX = 0
        self.GridTickIntervalY = 0       
        self.GridTickLength = 5

    def setupSymbologyTab(self):
        #Point Data
        self.SymbologyLevel = 0
        self.SymbologyShape = 'Circle'
        self.SymbologyFillColor = qtg.QColor(255,0,0)
        self.SymbologyBorderColor = qtg.QColor(0,0,0)      
        self.SymbologySize = 4.0
        self.SymbologySizeUnit = 'Points'
        
        #Coastline Data
        self.CoastlineResolution = 'Low'
        self.CoastlineLandFillColor = qtg.QColor(255,255,255)
        self.CoastlineWaterFillColor = qtg.QColor(117,161,221)
        self.CoastlineBorderWeight = .5
        self.CoastlineBorderColor = qtg.QColor(190,190,190)
        
        self.CoastlineNationalBoundaryType = 'National Boundaries' #Political Boundaries
        self.CoastlineNationalBoundaryWeight = 1         
        self.CoastlineNationalBoundaryColor = qtg.QColor(190,190,190)

        self.CoastlineRiverType = 'None' #Rivers
        self.CoastlineRiverWeight = .5
        self.CoastlineRiverColor = qtg.QColor(174,211,239)
        
    def setupScalebarTab(self):
        #Add Scalebar
        self.Scalebar = True 
        self.ScalebarOrientation = 'h'
        self.ScalebarHeight = .15
        self.ScalebarWidth = 5.0
        self.ScalebarSizeUnit = 'Inches'
        
        #Positioning
        self.ScalebarPositioning = 'Bottom Left'
        self.ScalebarXPos = 3.5
        self.ScalebarYPos = .6
        self.ScalebarPosUnit = 'Inches'
        self.ScalebarOffsetX = 1.0
        self.ScalebarOffsetY = 1.0
        self.ScalebarOffsetUnit = 'Inches' 
        
        #Labels & Tick
        self.ScalebarLabelX = None
        self.ScalebarLabelY = None       
        self.ScalebarInterval = 25
        self.ScalebarTickLength = .5
        
        #Add Frame
        self.ScalebarFrame = False
        self.ScalebarFrameBorderWidth = 1.0
        self.ScalebarFrameBorderColor = qtg.QColor(0,0,0)
        self.ScalebarFilled = True
        self.ScalebarFrameFill = qtg.QColor(255,255,255)        
        self.ScalebarPadding = 15
        self.ScalebarRounded = True

        #In Limbo until it finds a home...
        self.ScalebarIlluminate = False
        
    ###########################################################################################################################
    #Here  are the class properties, all listed by tab and order of appearance.
    ###########################################################################################################################      
    
    #########################################################################################
    ###########################################################################  MAP PAGE TAB
    ######################################################################################### 
    @property 
    def PageHeight(self):
        return self.__PageHeight
    @PageHeight.setter 
    def PageHeight(self, pageHeight = 8.5):
        self.__PageHeight = pageHeight
        
    @property 
    def PageWidth(self):
        return self.__PageWidth
    @PageWidth.setter 
    def PageWidth(self, pageWidth = 11.0):
        self.__PageWidth = pageWidth 
        
    @property 
    def PageSizeUnit(self):
        return self.__PageSizeUnit.title() 
    @PageSizeUnit.setter 
    def PageSizeUnit(self, pageSizeUnit = 'Inches'):
        self.__PageSizeUnit = pageSizeUnit.lower() 

    @property 
    def MapScaleFactor(self):
        return self.__MapScaleFactor
    @MapScaleFactor.setter
    def MapScaleFactor(self, factor):
        self.__MapScaleFactor = factor 
        
    #Add Title
    @property 
    def MapTitleAdd(self):
        return self.__MapTitleAdd 
    @MapTitleAdd.setter 
    def MapTitleAdd(self, add):
        self.__MapTitleAdd = add 

    @property 
    def MapTitle(self): #This property holds the font face, font color, font size, and offset values
        return self.__MapTitle
    @MapTitle.setter 
    def MapTitle(self, title):
        self.__MapTitle = title
        
    #Map Classification
    @property 
    def MapClassificationAdd(self):
        return self.__MapClassificationAdd
    @MapClassificationAdd.setter 
    def MapClassificationAdd(self, add):
        self.__MapClassificationAdd = add 

    @property 
    def MapClassification(self): #This property holds the font face, font color, font size, and offset values
        return self.__MapClassification
    @MapClassification.setter 
    def MapClassification(self, classification):
        self.__MapClassification = classification

    #########################################################################################
    ##########################################################################  MAP FRAME TAB
    ######################################################################################### 
    @property 
    def MapFrameType(self):
        return self.__MapFrameType
    @MapFrameType.setter 
    def MapFrameType(self, frame):
        self.__MapFrameType = frame
    
    @property
    def MapFrameWidth(self):
        return self.__MapFrameWidth 
    @MapFrameWidth.setter
    def MapFrameWidth(self, width):
        self.__MapFrameWidth = width  
        
    @property 
    def MapFrameColor(self):
        return self.__MapFrameColor 
    @MapFrameColor.setter 
    def MapFrameColor(self, color):
        self.__MapFrameColor = color 
    
    #Frame Annotations        
    @property 
    def MapFrameFont(self): #This property holds the font face, font color, font size, and offset values
        return self.__MapFrameFont 
    @MapFrameFont.setter 
    def MapFrameFont(self, font):
        self.__MapFrameFont = font 
        
    #Gridlines    
    @property 
    def GridlineWidth(self):
        return self.__GridlineWidth 
    @GridlineWidth.setter 
    def GridlineWidth(self, width):
        self.__GridlineWidth = width 
        
    @property
    def GridlineColor(self):
        return self.__GridlineColor
    @GridlineColor.setter
    def GridlineColor(self, color):
        self.__GridlineColor = color
      
    @property 
    def GridlineIntervalX(self):
        return self.__GridlineIntervalX 
    @GridlineIntervalX.setter
    def GridlineIntervalX(self, interval):
        self.__GridlineIntervalX = interval 
   
    @property 
    def GridlineIntervalY(self):
        return self.__GridlineIntervalY 
    @GridlineIntervalY.setter
    def GridlineIntervalY(self, interval):
        self.__GridlineIntervalY = interval
        
    #Grid Ticks 
    @property 
    def GridTicks(self):
        return self.__GridTicks 
    @GridTicks.setter
    def GridTicks(self, ticks):
        self.__GridTicks = ticks 
        
    @property 
    def GridTickWidth(self):
        return self.__GridTickWidth 
    @GridTickWidth.setter 
    def GridTickWidth(self, width):
        self.__GridTickWidth = width
   
    @property 
    def GridTickColor(self):
        return self.__GridTickColor
    @GridTickColor.setter 
    def GridTickColor(self, color):
        self.__GridTickColor = color
 
    @property 
    def GridTickIntervalX(self):
        return self.__GridTickIntervalX 
    @GridTickIntervalX.setter
    def GridTickIntervalX(self, interval):
        self.__GridTickIntervalX = interval
        
    @property 
    def GridTickIntervalY(self):
        return self.__GridTickIntervalY 
    @GridTickIntervalY.setter
    def GridTickIntervalY(self, interval):
        self.__GridTickIntervalY= interval     
        
    @property 
    def GridTickLength(self):
        return self.__GridTickLength 
    @GridTickLength.setter
    def GridTickLength(self, length):
        self.__GridTickLength = length 
       
     
    #########################################################################################
    #########################################################################  SYMBOLOGY TAB
    #########################################################################################         
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
        
    #Coastline Data    
    @property 
    def CoastlineResolution(self): #COASTLINES
        return self.__CoastlineResolution 
    @CoastlineResolution.setter
    def CoastlineResolution(self, res):
        self.__CoastlineResolution = res 
        
    @property
    def CoastlineLandFillColor(self):
        return self.__CoastlineLandFillColor
    @CoastlineLandFillColor.setter 
    def CoastlineLandFillColor(self, fill):
        self.__CoastlineLandFillColor = fill

    @property
    def CoastlineWaterFillColor(self):
        return self.__CoastlineWaterFillColor
    @CoastlineWaterFillColor.setter 
    def CoastlineWaterFillColor(self, fill):
        self.__CoastlineWaterFillColor = fill
        
    @property
    def CoastlineBorderWeight(self):
        return self.__CoastlineBorderWeight
    @CoastlineBorderWeight.setter 
    def CoastlineBorderWeight(self, weight):
        self.__CoastlineBorderWeight = weight
        
    @property
    def CoastlineBorderColor(self):
        return self.__CoastlineBorderColor
    @CoastlineBorderColor.setter 
    def CoastlineBorderColor(self, borderColor):
        self.__CoastlineBorderColor = borderColor
           
    @property 
    def CoastlineNationalBoundaryType(self): #POLITICAL BOUNDARIES
        return self.__CoastlineNationalBoundaryType
    @CoastlineNationalBoundaryType.setter 
    def CoastlineNationalBoundaryType(self, tp):
        self.__CoastlineNationalBoundaryType = tp

    @property 
    def CoastlineNationalBoundaryWeight(self):
        return self.__CoastlineNationalBoundaryWeight
    @CoastlineNationalBoundaryWeight.setter 
    def CoastlineNationalBoundaryWeight(self, w):
        self.__CoastlineNationalBoundaryWeight = w
        
    @property 
    def CoastlineNationalBoundaryColor(self):
        return self.__CoastlineNationalBoundaryColor
    @CoastlineNationalBoundaryColor.setter 
    def CoastlineNationalBoundaryColor(self, color):
        self.__CoastlineNationalBoundaryColor = color

    @property 
    def CoastlineRiverType(self): #RIVER TYPES
        return self.__CoastlineRiverType
    @CoastlineRiverType.setter 
    def CoastlineRiverType(self, tp):
        self.__CoastlineRiverType = tp

    @property 
    def CoastlineRiverWeight(self):
        return self.__CoastlineRiverWeight 
    @CoastlineRiverWeight.setter 
    def CoastlineRiverWeight(self, w):
        self.__CoastlineRiverWeight = w
        
    @property 
    def CoastlineRiverColor(self):
        return self.__CoastlineRiverColor 
    @CoastlineRiverColor.setter 
    def CoastlineRiverColor(self, color):
        self.__CoastlineRiverColor = color 

    #########################################################################################
    ###########################################################################  SCALEBAR TAB
    #########################################################################################  
    @property 
    def Scalebar(self):
        return self.__Scalebar
    @Scalebar.setter
    def Scalebar(self, scalebar):
        self.__Scalebar = scalebar 
     
    @property 
    def ScalebarOrientation(self):
        return self.__ScalebarOrientation
    @ScalebarOrientation.setter 
    def ScalebarOrientation(self, orientation):
        self.__ScalebarOrientation = orientation
        
    @property 
    def ScalebarWidth(self):
        return self.__ScalebarWidth
    @ScalebarWidth.setter 
    def ScalebarWidth(self, width):
        self.__ScalebarWidth = width
        
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
    
    #Positioning
    @property
    def ScalebarPositioning(self):
        return self.__ScalebarPositioning 
    @ScalebarPositioning.setter 
    def ScalebarPositioning(self, position):
        self.__ScalebarPositioning = position
        
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
    def ScalebarOffsetUnit(self):
        return self.__ScalebarOffsetUnit
    @ScalebarOffsetUnit.setter 
    def ScalebarOffsetUnit(self, unit):
        self.__ScalebarOffsetUnit = unit

    #Labels & Ticks
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
    def ScalebarInterval(self):
        return self.__ScalebarInterval 
    @ScalebarInterval.setter 
    def ScalebarInterval(self, interval):
        self.__ScalebarInterval = interval 

    @property 
    def ScalebarTickLength(self): 
        return self.__ScalebarTickLength 
    @ScalebarTickLength.setter 
    def ScalebarTickLength(self, length):
        self.__ScalebarTickLength = length
        
    #Add Frame
    @property 
    def ScalebarFrame(self):
        return self.__ScalebarFrame 
    @ScalebarFrame.setter 
    def ScalebarFrame(self, frame):
        self.__ScalebarFrame = frame
        
    @property 
    def ScalebarFrameBorderWidth(self):
        return self.__ScalebarFrameBorderWidth 
    @ScalebarFrameBorderWidth.setter 
    def ScalebarFrameBorderWidth(self, width):
        self.__ScalebarFrameBorderWidth = width 
        
    @property 
    def ScalebarFrameBorderColor(self):
        return self.__ScalebarFrameBorderColor 
    @ScalebarFrameBorderColor.setter 
    def ScalebarFrameBorderColor(self, color):
        self.__ScalebarFrameBorderColor = color 

    @property 
    def ScalebarFilled(self):
        return self.__ScalebarFilled 
    @ScalebarFilled.setter
    def ScalebarFilled(self, filled):
        self.__ScalebarFilled = filled
        
    @property 
    def ScalebarFrameFill(self):
        return self.__ScalebarFrameFill 
    @ScalebarFrameFill.setter
    def ScalebarFrameFill(self, fill):
        self.__ScalebarFrameFill = fill        
        
    @property 
    def ScalebarPadding(self):
        return self.__ScalebarPadding 
    @ScalebarPadding.setter
    def ScalebarPadding(self, padding):
        self.__ScalebarPadding = padding
 
    @property 
    def ScalebarRounded(self):
        return self.__ScalebarRounded
    @ScalebarRounded.setter 
    def ScalebarRounded(self, rounded):
        self.__ScalebarRounded = rounded   

    @property 
    def ScalebarIlluminate(self):
        return self.__ScalebarIlluminate 
    @ScalebarIlluminate.setter 
    def ScalebarIlluminate(self, i):
        self.__ScalebarIlluminate = i

