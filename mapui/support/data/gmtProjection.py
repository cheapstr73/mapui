class gmtProjection():
    def __init__(self):
        self.Type = 2
        self.Name = None
        self.CentralMeridian = None
        self.Width = None
        self.Azimuth = None
        #Set these to None, I will code this portion later; right now doing the basics (above)
        self.Scale = None
        self.Code = None
        self.ProjectionCenter = None
        self.StandardParallel = None
        self.StandardParallels = None
        self.UTMZone = None
        self.ScalingFactor = None
    
    def createAzimuthalProjection(self, name, projectionCenter, azimuth, width, scl):
        self.Name = name
        self.ProjectionCenter = projectionCenter
        self.Azimuth = azimuth
        self.Width = width
        self.ScalingFactor = scl
        
    def createConicProjection(self, name, projectionCenter, standardParallels, width, scl):
        self.Name = name
        self.ProjectionCenter = projectionCenter
        self.StandardParallels = standardParallels
        self.Width = width 
        self.ScalingFactor = scl
        
    def createCylindricProjection(self, name, centralMeridian, width, scl):
        self.Name = name
        self.CentralMeridian = centralMeridian        
        self.Width = width
        self.ScalingFactor = scl
        
    def getProjectionCode(self):
        for item in self.projectionList():
           # if item[0].startswith('*'):
               # continue
            if self.Name == item[0]:
                if item[2] == "Cylindrical" or item[2] == "Miscellaneous":
                    return item[1].upper() + str(self.CentralMeridian) + '/' + str((float(self.Width) * self.ScalingFactor))
                elif item[2] == "Azimuthal":
                    return item[1].upper() + str(self.ProjectionCenter) + '/' + str(self.Azimuth) + '/' + str((float(self.Width) * self.ScalingFactor))
                elif item[2] == "Conic":
                    return item[1].upper() + str(self.ProjectionCenter) + '/' + str(self.StandardParallels) + '/' + str((float(self.Width) * self.ScalingFactor))
                
    @staticmethod
    def projectionList():
        proj = [
                
            ["*Azimuthal Projections", "-1", "-1"],
            ["Azimuthal Equidistant Projection", "E", "Azimuthal"],
            ["Gnomonic Projection", "F", "Azimuthal"],
            ["Lambert Azimuthal Equal Area", "A", "Azimuthal"],
            ["Orthographic Projection", "G", "Azimuthal"],
            ["Stereographic Equal Angle Projection", "S", "Azimuthal"],
            
            ["*Conic Projections", "-1", "-1"],
            ["Albers Conic Equal Area Projection", "B", "Conic"],
            ["Equidistant Conic Projection", "L", "Conic"],
            ["Lambert Conic Conformal Projection", "D", "Conic"],
                
            ["*Cylindrical Projections", "-1", "-1"],
            #["Cassini Cylindrical Projection", "C", "Cylindrical"],
            ["Cylindrical Equal Area Projection", "Y", "Cylindrical"],
            ["Cylindrical Equidistant Projection", "Q", "Cylindrical"],
            ["Mercator Projection", "M", "Cylindrical"],
            ["Miller Cylindrical Projection", "J", "Cylindrical"],
            ["Transverse Mercator Projection", "T", "Cylindrical"],
            
            ["*Miscellaneous Projections", "-1", "-1"],
            ["Eckert VI Projection", "K", "Miscellaneous"],
            ["Hammer Projection", "H", "Miscellaneous"],
            ["Mollweide Projection", "W", "Miscellaneous"],
            ["Robinson Projection", "N", "Miscellaneous"],
            ["Sinusoidal Projection", "I", "Miscellaneous"],
            ["Van Der Grinten Projection", "V", "Miscellaneous"],
            ["Winkel Tripel Projection", "R", "Miscellaneous"]            
        ]
        return proj
    
    @property
    def Azimuth(self):
        return self.__Azimuth 
    @Azimuth.setter 
    def Azimuth(self, az):
        self.__Azimuth = az 
        
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
    def StandardParallels(self):
        return self.__StandardParallels
    @StandardParallels.setter 
    def StandardParallels(self, sp):
        self.__StandardParallels = sp 
        
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
    







