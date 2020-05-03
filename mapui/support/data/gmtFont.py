from PyQt5.QtGui import QColor as qc 
class gmtFont():
    def __init__(self, fFont = 'Helvetica-Bold', fSize = 18, fColor=qc(0,0,0), fText='', offsetx=0, offsety =0, offsetunit='Points'):
        self.font = fFont
        self.size = fSize
        self.color = fColor 
        self.text = fText
        self.offsetX = offsetx
        self.offsetY = offsety
        self.offsetUnit = offsetunit
        
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
        