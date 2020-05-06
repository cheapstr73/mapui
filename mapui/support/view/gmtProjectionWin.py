from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 
from PyQt5 import uic
from support.data.gmtProjection import gmtProjection 

###########################################################################################################################
#This is the interface for the projections. It contains a combo box populated with a list of projections, a projection
#icon and a projection description.
###########################################################################################################################
class gmtProjectionWin(qtw.QDialog):
    #Create a custom signal for the 'Submit' button
    submitted = qtc.pyqtSignal(str)   
    
    def __init__(self, *args, **kwargs):
        super(gmtProjectionWin, self).__init__(*args, **kwargs) 
        uic.loadUi('./support/interfaces/projection.ui', self)
        
        #Make sure the window is not resizable
        self.setFixedWidth(455)
        self.setFixedHeight(375)
        self.setWindowIcon(qtg.QIcon('./support/icons/globe2.png'))
        
        #Add a couple of unicode up/down arrows for the more info label
        self.downArrow = '\u2b9f'
        self.upArrow = '\u2b9d'
        
        #Is the window expanded?
        self.expanded = True
        self.toggleMoreInfo()
        
        #Set the icons to be used
        self.btn_submit.setIcon(qtg.QIcon('./support/icons/ok2.png'))
        self.lbl_icon.setScaledContents(True)
        self.lbl_icon.setAlignment(qtc.Qt.AlignVCenter)
        self.lbl_icon.setPixmap(qtg.QPixmap('./support/icons/projections/CylindricalEquidistantProjection.png'))
        
        #Create a dictionary of projecion names to function names
        self.createDictionary()  
        
        #Populate the projection names in the combo box
        self.populateProjectionComboBox()  
        
        #Set up the button click and combo box signals
        self.btn_submit.clicked.connect(self.onSubmit)
        self.combo_projections.currentIndexChanged.connect(self.currentIndexChanged)            
        self.currentIndexChanged()
        
        #Set the more information label as 'clickable'
        self.lbl_more_information.mousePressEvent = self.lblMoreInformationClicked
        self.lbl_more_information.setCursor(qtc.Qt.PointingHandCursor)       
        
    ###########################################################################################################################
    #This will populate the items in the projection combo box. The list is retrieved from the gmtProjection class and each
    #projection 'Category' is preceded by an asterick '*'. These items will be populated as a group header.
    ###########################################################################################################################
    def populateProjectionComboBox(self):
        row = 0
        for item in gmtProjection.projectionList(): #Loop through the list of projections
            if item[0].startswith('*'): #If the item begins with '*', it is a group header label
                self.addGroupHeader(row, item[0][1:]) #Add the item as a group header
                row += 1
                continue #Exit this iteration and continue with the next item in the loop
            self.combo_projections.addItem(item[0]) #If here, not a group header, but a regular item...
            row += 1
        self.combo_projections.setCurrentText("Cylindrical Equidistant Projection")
            
    ###########################################################################################################################
    #This will add a group header to the (projections)combo box. The effect will mimic the 'optgroup' that you see in an HTML 
    #select tag. This is not a default behavior in QT, so we have to improvise.
    ###########################################################################################################################
    def addGroupHeader(self, row, str):
        combo = self.combo_projections
        item = qtg.QStandardItem(str)
        item.setFlags(item.flags() ^ (qtc.Qt.ItemIsSelectable | qtc.Qt.ItemIsEnabled)) #Make the group header item non-selectable

        font = item.font()
        font.setBold(True)  #Also, make it bold to stand out
        item.setFont(font)
        
        itemModel = combo.model()
        itemModel.insertRow(row, item)   
    
    def onSubmit(self):    
        #self.__CurrentProjection = self.createProjection()            
        #Send the projection name back to parent to update the projection label...
        self.submitted.emit(str(self.combo_projections.currentText()))
        self.close()

    def currentIndexChanged(self):       
        t = self.combo_projections.currentText()  
        self.swapIcon()
        if t in self.projectionDictionary:
            self.projectionDictionary[t]()
        else:
            return     
         
   ###########################################################################################################################
   #Create a dictionary with each projection mapped to it's corresponding function. This will eliminate have 10 million
   #'if' statements to determine which function gets called when a new item is selected in the combo box.
   ########################################################################################################################### 
    def createDictionary(self):
        #Each projection has an equivalent function name...
        self.projectionDictionary = {
            "Cassini Cylindrical Projection" : self.CassiniCylindricalProjection,
            "Cylindrical Equidistant Projection" : self.CylindricalEquidistantProjection,
            "Cylindrical Equal Area Projection" : self.CylindricalEqualAreaProjection,
            "Mercator Projection" : self.MercatorProjection,
            "Miller Cylindrical Projection" : self.MillerCylindricalProjection,
            "Transverse Mercator Projection" : self.TransverseMercatorProjection
        }
      
    def swapIcon(self):
        path = './support/icons/projections/'
        name = self.combo_projections.currentText().replace(' ', '') + '.png'
        self.lbl_icon.setPixmap(qtg.QPixmap(path + name))     
    
    def lblMoreInformationClicked(self, event):
        self.toggleMoreInfo()
        
    def toggleMoreInfo(self):
        if self.expanded:
            self.setFixedHeight(170)
            self.lbl_more_information.setText('More ' + self.downArrow)
            self.expanded = False
        elif not self.expanded:            
            self.setFixedHeight(375)
            self.lbl_more_information.setText(self.upArrow + " Less")
            self.expanded = True
        else:
            return 
        self.update()            
        
   ###########################################################################################################################
   #There is a function for each projection in the list. This will control how the UI items get displayed.
   ########################################################################################################################### 
    def CassiniCylindricalProjection(self):
        pass    
    def CylindricalEqualAreaProjection(self):
        pass
    def CylindricalEquidistantProjection(self):
        pass
    def MercatorProjection(self):
        pass
    def MillerCylindricalProjection(self):
        pass
    def ObliqueMercatorProjection(self):
        pass
    def TransverseMercatorProjection(self):
        pass
    def UniversalTransverseMercatorProjection(self):
        pass
        