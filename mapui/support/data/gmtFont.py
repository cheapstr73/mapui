from PyQt5.QtGui import QColor as qc 
class gmtFont():
    def __init__(self, fFont = 'Helvetica-Bold', fSize = 18, fColor=qc(0,0,0), fText=''):
        self.font = fFont
        self.size = fSize
        self.color = fColor 
        self.text = fText
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

    