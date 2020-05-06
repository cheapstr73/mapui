from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 
from support.data.gmtColors import GMTColors
from os import path
import re

###########################################################################################################################
#The PaletteView class takes a (string) color palette table (.cpt) file as input, extracts the associated color values and 
#displays those colors as a visual color palette. The class also takes in an optional (integer) opacity value so the 
#palette can be drawn with transparency.
###########################################################################################################################
class PaletteViewer(qtw.QWidget):  
    @property 
    def CPTPath(self):
        return self.__CPTPath 
    @CPTPath.setter 
    def CPTPath(self, path):
        self.__CPTPath = path
    
    #Constructor takes a .cpt file and optional (int) opacity value
    def __init__(self):
        super(PaletteViewer, self).__init__()        
        #Set the GMT CPT Path
        try:
            with open("./.config/settings.txt", 'r') as f:
                path = f.readline().split('=')[1].strip() 
                self.CPTPath = path + 'cpt/'
        except:
            self.__showMessage(1,"L Cannot find the settings file \'./.config/settings.txt\'")
 
        #Set the size of this widget
        self.setFixedWidth(227)
        self.setFixedHeight(35)
         
        #Create and set up the layout
        self.layout = qtw.QHBoxLayout()  
        self.layout.addSpacing(-6)    
        self.layout.setAlignment(qtc.Qt.AlignLeft)
       
        #Add the layout to the widget     
        self.setLayout(self.layout)   

    ###########################################################################################################################
    #Since the painting is added to the layout, this will clear the layout; so as to not add mutiple painted objects.
    ###########################################################################################################################
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None: 
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    ###########################################################################################################################
    #This method does the initial read-in of a .cpt file. It takes a string parameter for the cptFile filename and an integer
    #parameter (0-255) to represent the alpha value (opacity).
    ###########################################################################################################################
    def DrawPalette(self, cptFile, normal=True, opacity=255):   
        self.clearLayout(self.layout)   
        self.normal = normal #For normally drawn CPT (colors not reversed)
        
        #If file if null or emtpy, just return...         
        if not cptFile: 
            return  
        #Check if the file actually exists... 
        if not path.exists(self.CPTPath + cptFile):
            self.__showMessage(3, 'Cannot find ' + self.CPTPath + cptFile)
            return

        #Make sure opacity is between 0-255
        if opacity >= 0 and opacity <= 255:
            self.opacity = opacity
        else:
            self.opacity = 255

        try:
            with open(self.CPTPath + cptFile, 'r') as file:
                lines = file.readlines() 

                #Clear up the file, remove all comments and un-needed lines...
                lines = self.__fixColumns(lines)

                #Set the totl number of colors to process...     
                self.TotalColors = len(lines) + 1 

                colors = self.__processColors(lines)   
                self.layout.addWidget(_PaintedPalette(colors, self.normal, self.opacity))

        except Exception as e:
            self.__showMessage(3, str(e))
            return         
         
    ###########################################################################################################################
    #This method will take the read file (a list of strings) and create / return a new list. The new list will have all of the
    #unnecessary lines removed as well as all of the awkward whitespaces, carriage returns, etc. The end result will be a list
    #of only the necessary lines with each column separated by one (1) whitespace to be used as a split key later.
    ###########################################################################################################################
    def __fixColumns(self, lines):        
        errors = []
        cleanList = []
        for line in lines:
            #We don't need the comments, Background color, Foreground color or the NaN color to display the palette...
            if not line.startswith("#") and not line.startswith('B') and not line.startswith('F') and not line.startswith('N'):
                try:
                    line.strip()
                    #Replace all (1 or more) newlines, tabs, and whitespaces with only 1 whitespace
                    line = re.sub(r"[\n\t\s]+", ' ', line)
                    cleanList.append(line)

                except Exception as e:
                    errors.append(str(e)) 
        return cleanList         

    ###########################################################################################################################
    #This function will split each line into columns and parse out the appropriate color values from the proper columns. Most
    #GMT supplied .cpt files will have 4 columns (elevation value (start) | color | elevation value (end) | color), while some 
    #have only 2 columns. Many third part supplied .cpt files contain 8 columns where each r-g-b value is put into it's own 
    #column next to associated elevation. This is a pretty long function, but a covers all of the above scenarios. This takes
    #a python list (.cpt file) and returns a new list, with propery formatted (String) color values to be processed.
    ###########################################################################################################################
    def __processColors(self, lines):
        count =1
        colorList = [] 
        #Loop through the lines of the colors file
        for line in lines:
            try:
                #Split the line into columsn based on emtpy space (' ')
                columns = line.split()

                #Most GMT supplied files have either 2 or 4 columms...
                if len(columns) == 2 or len(columns) == 4: 
                    #If this is the first one in the list, get the starting color from column 1
                    if count == 1:
                        tmpColor1 = columns[1].strip() 
                        if not self.__isNumber(tmpColor1[:1]):
                            if tmpColor1 in GMTColors.getGMTColors():
                                colorList.append(GMTColors.getGMTColors()[tmpColor1])
                            else:
                                self.__showMessage(1, "Cannot find RGB Code for \'" + tmpColor1 + "\'")

                    #Now get the stop color for each line from the last column
                    tmpColor2 = columns[-1].strip() 
                    
                    #If first character is not a digit, check the gmtColors for a 'name' match
                    if not self.__isNumber(tmpColor2[:1]):
                        if tmpColor2 in GMTColors.getGMTColors():
                            colorList.append(GMTColors.getGMTColors()[tmpColor2])
                        else:
                            self.__showMessage(1, "Cannot find RGB Code for \'" + tmpColor2 + "\'") 

                    #If here, first character was a digit, so look for a forward slash ('/') or a comma (',) - RGB's will be separated by one of these
                    elif  '/' in tmpColor2: #GMT RGB values like the '/', but we don't need that here...
                        tmpColor2 = tmpColor2.replace('/',',') 
                        
                    if ',' in tmpColor2: #RGB values should be comma separated                    
                        if len(tmpColor2.split(',')) == 3:                            
                            colorList.append(tmpColor2) #We have a 3 part number, so add to the list     
                            continue                   
                        else:
                            self.__showMessage(3, columns[-1] + " does not appear to be a valid color!")

                    #HSV values are dash ('-') separated, so if we are here, we are dealing with HSV
                    elif '-' in tmpColor2: 
                        tmp = tmpColor2.split('-')
                        h = int(tmp[0])
                        s = float(tmp[1])
                        v = float(tmp[2])

                        #I hope this is right...converting from -1:1 scale into 0-255 scale.
                        s = round((s) * 255) 
                        v = round((v) * 255)

                        tmpColor3 = str(h) + '-' + str(s) + '-' + str(v)                    
                        colorList.append(tmpColor3)
                    continue

                #For an 8 column file, we shouldn't be here...but just in case.
                elif len(columns) == 8: 
                    #If this is the first color of the file...get the starting color from column 1.
                    if count == 1:
                        r = columns[1].strip() 
                        g = columns[2].strip()
                        b = columns[3].strip()
                        tmpRGB = str(r) + ',' + str(g) + ',' + str(b)
                        #Check to make sure it's a numeric value (for RGB), and not a named color.
                        if not self.__isNumber(tmpRGB[:1]):
                            if tmpRGB in GMTColors.getGMTColors():
                                colorList.append(GMTColors.getGMTColors()[tmpRGB])
                            else:
                                self.__showMessage(1, "Cannot find RGB Code for \'" + tmpRGB + "\'")
                    #Now process the ending colors for the rest of the file (in column 7)
                    r = columns[5].strip()
                    g = columns[6].strip()
                    b = columns[7].strip()
                    tmpRGB = str(r) + ',' + str(g) + ',' + str(b)
                    #Make sure the ending color is a numeric value (not named color).
                    if not self.__isNumber(tmpRGB[:1]):
                        if tmpRGB in GMTColors.getGMTColors():
                            colorList.append(GMTColors.getGMTColors()[tmpRGB])
                            continue
                        else:
                            self.__showMessage(1, "Cannot find RGB Code for \'" + tmpRGB + "\'")
                    #Finally add this newly formatted color to the list to be returned
                    colorList.append(tmpRGB)

                count += 1
            except Exception as e:
                self.__showMessage(3, str(e))   

        #Return the list of colors...
        return colorList 


    def __writeFile(self, str):
        with open('test.txt', 'a') as f:
            f.write("Line: " + str + '\n')

    ###########################################################################################################################
    #This method will take a string and determine if it is a numeric digit or not...returning true or false
    ###########################################################################################################################
    def __isNumber(self, str):
        return str.isdigit()

    def __getRGBFromName(self, str):
        if str in GMTColors.getGMTColors():
            return GMTColors.getGMTColors()[str]
        else:
            self.__showMessage(1, "Cannot find RGB Code for \'" + str + "\'")
            return None
    
    def __showMessage(self,icon,str):
        if icon == 1:
            title = "Message"
        elif icon == 3:
            title = "Error"

        mes = qtw.QMessageBox(
            icon,
            title,
            str,
            qtw.QMessageBox.Ok,
            self.parent(),
            qtc.Qt.Dialog)
        mes.exec()

###########################################################################################################################
#The PaintedPalette class is responsible for taking in a list of colors and drawing/painting a gradient.
###########################################################################################################################
class _PaintedPalette(qtw.QWidget):
    color = None
    size = 0
    def __init__(self, colorList, normal, opacity):
        super(_PaintedPalette, self).__init__()

        self.setFixedHeight(19)
        self.setFixedWidth(220)         
        self.lines = colorList
        self.normal = normal
        self.opacity = opacity        
        self.update()

    def paintEvent(self, e):
        painter = qtg.QPainter()
        painter.begin(self)
        if not self.normal:
            self.__drawRectangleF(painter)
        else:
            self.__drawRectangleR(painter)
        painter.end()


    ###########################################################################################################################
    #Paint the gradient 'Forward', from start to end. Yes, we have to read the list from back to front for this!
    ###########################################################################################################################
    def __drawRectangleF(self, qp):
        pos = 1 / len(self.lines)
        start = 0

        #Set the gradient to about 10 pixels shorter and the width of the parent control...
        lg = qtg.QLinearGradient(215, 0, 0.0, 0.0)   

        #Start the list from the back and split the columms               
        for line in reversed(self.lines):
            cols = line.split()
            rough = cols[-1]        
            
            if ',' in rough: #Create color from RGB; RGB's should be comma separated here
                splitColor = rough.split(',')                    
                r = int(splitColor[0]) #red
                g = int(splitColor[1]) #green
                b = int(splitColor[2]) #blue
                a = self.opacity #and..the opacity
                color = qtg.QColor(r,g,b,a) #set the new color with the rgba

            elif '-'  in rough: #Create color from HSV; HSV's are dash separated
                splitColor = rough.split('-') 
                h = int(splitColor[0]) #hue
                s = int(splitColor[1]) #saturation
                v = int(splitColor[2]) #value
                a = self.opacity #and...opacity
                color = qtg.QColor() #set the new color with hsva
                color.setHsv(h,s,v,a)

            lg.setColorAt(start, color) #set the gradient color at the current position
            start += pos #increase the current position...

        qp.setPen(qtg.QColor(215,215,215))
        qp.setBrush(lg) 
        rect = qtc.QRectF(0, 0, 215, 18.0)
        qp.drawRect(rect)
  
    ###########################################################################################################################
    #Paint the gradient 'Reverse'
    ###########################################################################################################################
    def __drawRectangleR(self, qp):
        pos = 1 / len(self.lines)
        start = 0

        #Set the gradient to about 10 pixels shorter and the width of the parent control...
        lg = qtg.QLinearGradient(215, 0, 0.0, 0.0)   

        #Start the list from the front this time split the columms               
        for line in self.lines:
            cols = line.split()
            rough = cols[-1]        
            
            if ',' in rough: #Create color from RGB; RGB's should be comma separated here
                splitColor = rough.split(',')                    
                r = int(splitColor[0]) #red
                g = int(splitColor[1]) #green
                b = int(splitColor[2]) #blue
                a = self.opacity #and..the opacity
                color = qtg.QColor(r,g,b,a) #set the new color with the rgba

            elif '-'  in rough: #Create color from HSV; HSV's are dash separated
                splitColor = rough.split('-') 
                h = int(splitColor[0]) #hue
                s = int(splitColor[1]) #saturation
                v = int(splitColor[2]) #value
                a = self.opacity #and...opacity
                color = qtg.QColor() #set the new color with hsva
                color.setHsv(h,s,v,a)

            lg.setColorAt(start, color) #set the gradient color at the current position
            start += pos #increase the current position...

        qp.setPen(qtg.QColor(215,215,215))
        qp.setBrush(lg) 
        rect = qtc.QRectF(0, 0, 215, 18.0)
        qp.drawRect(rect)
