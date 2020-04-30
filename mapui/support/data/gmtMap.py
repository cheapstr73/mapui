from support.data.gmtMapOptions import gmtMapOptions
#from support.data.gmtProjection import gmtProjection

###########################################################################################################################
#This class will hold all of the properties associated to create a gmtMap. This will be the gmtMap object.
###########################################################################################################################
class gmtMap(gmtMapOptions):
    def __init__(self):
        super().__init__()  
        self.initializeDefaults()

    @property 
    def ConvertType(self):
        return self.__ConvertType
    @ConvertType.setter 
    def ConvertType(self, type):
        self.__ConvertType = type

    @property 
    def CPTFile(self):
        return self.__CPTFile         
    @CPTFile.setter 
    def CPTFile(self, cptFile = 'seis.cpt'):
        self.__CPTFile = cptFile 

    @property 
    def CPTInterval(self):
        return self.__CPTInterval
    @CPTInterval.setter 
    def CPTInterval(self, cptInterval = 10):
        self.__CPTInterval = cptInterval 
        
    @property 
    def CPTMaxValue(self):
        return self.__CPTMaxValue
    @CPTMaxValue.setter 
    def CPTMaxValue(self, cptMaxValue = 100):
        self.__CPTMaxValue = cptMaxValue 

    @property 
    def CPTMinValue(self):
        return self.__CPTMinValue 
    @CPTMinValue.setter 
    def CPTMinValue(self, cptMinValue = 0):
        self.__CPTMinValue = cptMinValue

    @property 
    def FileInput(self):
        return self.__FileInput 
    @FileInput.setter 
    def FileInput(self, fileInput):
        self.__FileInput = fileInput

    @property 
    def FileOutput(self):
        return self.__FileOutput 
    @FileOutput.setter 
    def FileOutput(self, fileOutput):
        self.__FileOutput = fileOutput

    @property 
    def InputFile(self):
        return self.__InputFile 
    @InputFile.setter 
    def InputFile(self, inputFile):
        self.__InputFile = inputFile

    @property 
    def Opacity(self):
        return self.__Opacity
    @Opacity.setter 
    def Opacity(self, opacity = 255):
        self.__Opacity = opacity

    @property
    def Projection(self):
        return self.__Projection
    @Projection.setter 
    def Projection(self, projection):
        self.__Projection = projection

    @property 
    def ROINorth(self):
        return self.__ROINorth
    @ROINorth.setter 
    def ROINorth(self, roiNorth = 60):
        self.__ROINorth = roiNorth

    @property 
    def ROISouth(self):
        return self.__ROISouth
    @ROISouth.setter 
    def ROISouth(self, roiSouth = 50):
        self.__ROISouth = roiSouth

    @property 
    def ROIEast(self):
        return self.__ROIEast
    @ROIEast.setter 
    def ROIEast(self, roiEast = 90):
        self.__ROIEast = roiEast

    @property 
    def ROIWest(self):
        return self.__ROIWest
    @ROIWest.setter 
    def ROIWest(self, roiWest = 130):
        self.__ROIWest = roiWest

    @property 
    def ScaleUnit(self):
        return self.__ScaleUnit 
    @ScaleUnit.setter 
    def ScaleUnit(self, scaleUnit):
        self.__ScaleUnit = scaleUnit 

    def initializeDefaults(self):
        self.ConvertType = 'f'
        self.FileInput = None
        self.ROINorth = '60'
        self.ROISouth = '50'
        self.ROIEast = '90'
        self.ROIWest = '130'
        self.CPTFile = 'seis.cpt'
        self.Opacity = 100
        self.CPTMinValue = '0'
        self.CPTMaxValue = '100'
        self.CPTInterval = '10'
        self.ScaleUnit = 'mgals'
        self.Projection = None
        self.FileOutput = None

    ###########################################################################################################################
    #This will return the central meridian of the East/West coordinates
    ###########################################################################################################################    
    def getCM(self):
        pe = float(self.ROIEast)
        pw = float(self.ROIWest)
        return float(round((pe+pw) / 2.0))

    ###########################################################################################################################
    #This will return the Latitude grid spacing in degres
    ###########################################################################################################################
    def getLatitudeGS(self): 
        ns = float(self.ROINorth) - float(self.ROISouth)
        if ns <= 15:
            return 1
        elif ns > 10 and ns <= 30:
            return 2
        elif ns > 30 and ns <= 75:
            return 3
        else:
            return 10

    ###########################################################################################################################
    #This will return the Longitude grid spacing in degres
    ###########################################################################################################################
    def getLongitudeGS(self): 
        ln = float(self.ROIWest) - float(self.ROIEast)
        if ln <= 15:
            return 1
        elif ln > 15 and ln <= 30:
            return 2
        elif ln > 30 and ln <= 70:
            return 5
        elif ln > 70 and ln <= 100:
            return 10
        else:
            return 20

    def __str__(self):
        with open('mapObject.txt', 'a') as f:
            f.write("CPT = " + self.CPTFile)