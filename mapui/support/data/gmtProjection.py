from support.data.mapuiSettings import mapuiSettings
class gmtProjection():
    def __init__(self, name, cm, width):
        self.Type = 2
        self.Name = name
        self.CentralMeridian = cm
        self.Width = width
        
        #Set these to None, I will code this portion later; right now doing the basics (above)
        self.Scale = None
        self.Code = None
        self.ProjectionCenter = None
        self.StandardParallel = None
        self.UTMZone = None      
        
    def getProjectionCode(self):
        for item in self.projectionList():
           # if item[0].startswith('*'):
               # continue
            if self.Name == item[0]:
                if self.Type == 1:
                    return item[1].lower() + str(self.CentralMeridian) + '/**' + str(self.Scale)
                else:
                    return item[1].upper() + str(self.CentralMeridian) + '/' + str((float(self.Width) * mapuiSettings.getWidthScalingFactor()))
                
    @staticmethod
    def projectionList():
        proj = [
            ["*Cylindrical Projections", "-1", "-1"],
            #["Cassini Cylindrical Projection", "C", "Cylindrical"],
            ["Cylindrical Equal Area Projection", "Y", "Cylindrical"],
            ["Cylindrical Equidistant Projection", "Q", "Cylindrical"],
            ["Mercator Projection", "M", "Cylindrical"],
            ["Miller Cylindricals Projection", "J", "Cylindrical"],
            ["Transverse Mercator Projection", "T", "Cylindrical"],
            
            ["*Miscellaneous Projections", "-1", "-1"],
            ["Eckert IV and VI Projection", "K", "Miscellaneous"],
            ["Hammer Projection", "H", "Miscellaneous"],
            ["Mollweide Projection", "W", "Miscellaneous"],
            ["Robinson Projection", "N", "Miscellaneous"],
            ["Sinusoidal Projection", "I", "Miscellaneous"],
            ["Van der Grinten Projection", "V", "Miscellaneous"],
            ["Winkel Tripel Projection", "R", "Miscellaneous"]
            
        ]
        return proj
    
    @property 
    def Code(self):
        return self.__Code 
    @Code.setter 
    def Code(self, code):
        self.__Code = code 
        
    @property 
    def Type(self):
        return self.__Type 
    @Type.setter 
    def Type(self, t):
        self.__Type = t 

    @property 
    def Name(self):
        return self.__Name 
    @Name.setter 
    def Name(self, name):
        self.__Name = name 
            
    @property 
    def CentralMeridian(self):
        return self.__CentralMeridian
    @CentralMeridian.setter 
    def CentralMeridian(self, cm):
        self.__CentralMeridian = cm 

    @property 
    def ProjectionCenter(self):
        return self.__ProjectionCenter 
    @ProjectionCenter.setter 
    def ProjectionCenter(self, pc):
        self.__ProjectionCenter = pc 
    
    @property 
    def StandardParallel(self):
        return self.__StandardParallel 
    @StandardParallel.setter 
    def StandardParallel(self, sp):
        self.__StandardParallel = sp 
    
    @property 
    def Scale(self):
        return self.__Scale 
    @Scale.setter 
    def Scale(self, scale):
        self.__Scale = scale 

    @property 
    def UTMZone(self):
        return self.__UTMZone 
    @UTMZone.setter 
    def UTMZone(self, zone):
        self.__UTMZone = zone 

    @property 
    def Width(self):
        return self.__Width 
    @Width.setter 
    def Width(self, w):
        self.__Width = w
    







