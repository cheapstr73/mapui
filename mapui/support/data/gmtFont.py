from PyQt5.QtGui import QColor as qc 
###########################################################################################################################
#This class hold the font information for all of the text on the map (title, classification, grid numbers, etc.) 
#It holds the font face, color, and size. Also, to avoid alot of duplication, it also holds the ofset values, offset
#units and any text that it may display.
###########################################################################################################################

class gmtFont():
    #In the constructor all parameters are optional, but for certain text pieces, you may want to set them)
    def __init__(self, fFont='Helvetica-Bold', fSize=18, fColor=qc(0,0,0), fText='', offsetx=0, offsety =0, offsetunit='Points'):
        self.font = fFont
        self.size = fSize
        self.color = fColor 
        self.text = fText
        self.offsetX = offsetx
        self.offsetY = offsety
        self.offsetUnit = offsetunit
   
    ###########################################################################################################################
    #The font class properties. 
    ###########################################################################################################################     
    @property
    def font(self):
        return self.__font
    @font.setter 
    def font(self, f):
        self.__font = f 
    
    @property 
    def size(self):
        return self.__size 
    @size.setter
    def size(self, s):
        self.__size = s

    @property 
    def color(self):
        return self.__color
    @color.setter 
    def color(self, c):
        self.__color = c
    
    @property
    def text(self):
        return self.__text 
    @text.setter 
    def text(self, t):
        self.__text = t

    @property 
    def offsetX(self):
        return self.__offsetX 
    @offsetX.setter
    def offsetX(self, x):
        self.__offsetX = x
    
    @property 
    def offsetY(self):
        return self.__offsetY
    @offsetY.setter
    def offsetY(self, y):
        self.__offsetY = y
    
    @property 
    def offsetUnit(self):
        return self.__offsetUnit 
    @offsetUnit.setter
    def offsetUnit(self, unit):
        self.__offsetUnit = unit 
        