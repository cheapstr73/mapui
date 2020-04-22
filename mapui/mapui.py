#!/usr/bin/python
####################### NEED TO DO ITEMS ####################
#Verify all settings before enabling the execute button
#Verify all max values are greater than min values...
#Do a better job of verifying .map file load!

from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 
from PyQt5 import uic
from os import walk, system
from support.data.mapuiSettings import mapuiSettings
from support.data.gmtMap import gmtMap
from support.data.ColorPaletteViewer import PaletteViewer
from support.data.gmtMapScript import gmtMapScript
from support.data.mapuiOptionsWin import mapUIOptions
import sys
import pickle
import re

###########################################################################################################################
#This class loads the interface.ui file and creates the main interface
###########################################################################################################################
class mainWin(qtw.QDialog):
    def __init__(self):
        super(mainWin, self).__init__()
        uic.loadUi('./support/interfaces/interface2.ui', self)

        #Decare the icons to be used...
        self.windowIcon = qtg.QIcon('./support/icons/map7.png')
        self.populateIcon = qtg.QIcon('./support/icons/fill1')
        self.saveIcon = qtg.QIcon('./support/icons/save4.png')
        self.openIcon = qtg.QIcon('./support/icons/open-file.png')
        self.loadIcon = qtg.QIcon('./support/icons/open3.png')
        self.optionsIcon = qtg.QIcon('./support/icons/options10.png')
        self.helpIcon = qtg.QIcon('./support/icons/help1.png')
        self.aboutIcon = qtg.QIcon('./support/icons/help2.png')
        self.executeIcon = qtg.QIcon('./support/icons/run2.png')

        #Create a gmtMap object...
        self.gmtMap = gmtMap()
        
        #Create the options window
        self.options = mapUIOptions(self)
        self.setupInterface()

        #Poplate the form 
        self.populateForm()
        
        #Check to see if the interface is opening with a file (sys.argv parameter)    
        if len(sys.argv) > 1:
            if sys.argv[1]:
                self.loadParameters(sys.argv[1])
                self.analyzeInput(self.gmtMap.FileInput)
            else:
                self.showMessage(4, "title", "NO")           

        self.show()

    ###########################################################################################################################
    #This is responsible for setting up the interface controls (i.e. populating combo boxes, setting button-click signals, etc)
    ###########################################################################################################################
    def setupInterface(self):   
        #Set up the layout
        self.cpLayout.setAlignment(qtc.Qt.AlignLeft)
        self.createFileMenu()

        #Add the color palette viewer to the interface and load it.
        self.viewer = PaletteViewer()
        self.cpLayout.addWidget(self.viewer)

        #Add the icons for the window and button
        self.setWindowIcon(self.windowIcon)
        self.btn_open_file.setIcon(self.openIcon)
        self.btn_fill_defaults.setIcon(self.populateIcon)
        self.btn_save.setIcon(self.saveIcon)
        self.btn_load.setIcon(self.loadIcon)
        self.btn_options.setIcon(self.optionsIcon)
        self.btn_execute.setIcon(self.executeIcon)
        
        #Set button cursors
        self.btn_open_file.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_fill_defaults.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))

        #Add signals to the slots 
        self.combo_cpt.currentIndexChanged.connect(self.viewPalette)   
        self.btn_open_file.clicked.connect(self.openFile)  
        self.btn_fill_defaults.clicked.connect(self.populateDefaults)      
        self.slider_opacity.valueChanged.connect(self.getSliderValue)
        self.btn_save.clicked.connect(self.saveParameters)
        self.btn_load.clicked.connect(self.loadParameters)
        self.btn_options.clicked.connect(self.openOptions)
        self.btn_execute.clicked.connect(self.executeScript)

        #Populate the combo boxes with associated values
        self.combo_cpt.addItems(self.populateCPTComboBox())
        self.combo_verbosity.addItems(mapuiSettings.getVerbosity())
        self.combo_cpt_unit.addItems(mapuiSettings.getCPTUnits())
      

        self.txt_north.setValidator(qtg.QDoubleValidator(-90, 90, 2, self))
        self.txt_south.setValidator(qtg.QDoubleValidator(-90, 90, 2, self))
        self.txt_east.setValidator(qtg.QDoubleValidator(-180, 180, 2, self))
        self.txt_west.setValidator(qtg.QDoubleValidator(-180, 180, 2, self))
        self.txt_cpt_min.setValidator(qtg.QDoubleValidator())
        self.txt_cpt_max.setValidator(qtg.QDoubleValidator())
        self.txt_cpt_interval.setValidator(qtg.QIntValidator())

        #Fill the map projections combo box...
        projections = mapuiSettings.getProjections()
        for i in range(len(projections)):
            if projections[i].startswith('[GRP]'):               
                self.addGroupHeader(self.combo_projections, i, projections[i][5:])
                
            else:
                self.combo_projections.addItem(projections[i])
        self.combo_projections.setCurrentIndex(1)
        
        #self.txt_file_open.setFocus()
        self.lbl_slider_value.setText(str(self.slider_opacity.value()) + "%")
        self.btn_fill_defaults.setEnabled(False)

    ###########################################################################################################################
    #This will create the file menu and sub-menu items
    ##########################################################################################################################
    def createFileMenu(self):
        menuBar = qtw.QMenuBar()
        fileMenu = menuBar.addMenu('&File')
        optionsMenu = menuBar.addMenu('&Options')
        helpMenu = menuBar.addMenu('&Help')

        #Create the menu item actions
        saveAction = qtw.QAction(self.saveIcon, '&Save Parameters', self)
        loadAction = qtw.QAction(self.loadIcon, '&Load Parameters', self)
        optionsAction = qtw.QAction(self.optionsIcon, '&Options', self)
        helpAction = qtw.QAction(self.helpIcon, '&Help', self)
        aboutAction = qtw.QAction(self.windowIcon, '&About MapUI', self)
 
        #Add the menu events...
        saveAction.triggered.connect(self.saveParameters)
        loadAction.triggered.connect(self.loadParameters)
        optionsAction.triggered.connect(self.openOptions)

        #Add menu items to the menus
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)
        optionsMenu.addAction(optionsAction)
        helpMenu.addAction(aboutAction)
        helpMenu.addAction(helpAction)
        self.menu_layout.addWidget(menuBar)

    def openOptions(self):        
        self.options.show()

    ###########################################################################################################################
    #Most GMT installations seem to intstall different .cpt files depending on the distro being used; so I do not want to load
    #the combo box with 'static' .cpt filenames. Rather, pull the list of .cpt's from the GMT install directory.
    ###########################################################################################################################
    def populateCPTComboBox(self):
        #Get the GMT path... 
        cptList = []
        try:
            settings = ".config/settings.txt"
            with open(".config/settings.txt", 'r') as f:
                path = f.readline().split('=')[1].strip() 
                for r, d, f in walk(path + "cpt/"): #only need filenames here...
                    for file in f:
                        if file.endswith('.cpt'):
                            cptList.append(file)
        except:
            self.showMessage(3, "Error", "-Cannot find the settings file \'" + settings + "'")
        return sorted(cptList)
 
    ###########################################################################################################################
    #Get the value from the (Opacity) slider control. Call viewPalette on every value change.
    ###########################################################################################################################
    def getSliderValue(self):
        val = self.slider_opacity.value()         
        self.lbl_slider_value.setText(str(val) + "%") 
        self.viewPalette()

    ###########################################################################################################################
    #Read the first line of the input file and determine how many columns it contains.
    ###########################################################################################################################
    def readInputFile(self, input):
        try:
            with open(input, 'r') as f:
                line = f.readline()
                line = re.sub(r"[\n\t\s]+", ' ', line)
                cols = line.split(' ')
                count =0 
                for col in cols:
                    if col:
                        if col.isdigit:
                            count += 1
                        else:
                            return -1
                return count
        except Exception as e:
            self.showMessage(1, '', str(e))
            return -1
    
    def analyzeInput(self, input):
        try:
            with open(input, 'r') as f:
                lines = f.readlines()

                #Create 4 empty lists so we can fill each list with contents of each column...
                col0, col1, col2, col3 = ([] for i in range(4))  
                for line in lines:
                    line = re.sub(r"[\n\t\s]+", ' ', line)  
                    if line.startswith(u'\ufeff'):
                        line = line.replace(u'\ufeff','')            
                    line = line.strip()
                    cols = line.split()
                    #For the current line, put the value of each column in it's appropriate list...
                    #This is a messsy way of doing this, but...it works
                    if len(cols) == 4:
                        for i in range(len(cols)):  
                            if i == 0:
                                col0.append(float(cols[0]))
                            elif i == 1:
                                col1.append(float(cols[1]))
                            elif i == 2:
                                col2.append(float(cols[2]))
                            elif i == 3:
                                col3.append(float(cols[3]))
                    else:
                        return
                col0.sort()
                col1.sort()
                col2.sort()
                col3.sort()

                self.FileMinLong = col0[0]
                self.FileMaxLong = col0[-1]
                self.FileMinLat = col1[0]
                self.FileMaxLat = col1[-1]
                self.FileMinRange = col2[0]
                self.FileMaxRange = col2[-1] 
                self.FileMaxSize = col3[0]
                self.FileMaxSize = col3[-1]
                col0 = None
                col1 = None
                col2 = None
                col3 = None
                self.lbl_east.setText(str(self.FileMinLong))
                self.lbl_west.setText(str(self.FileMaxLong))
                self.lbl_south.setText(str(self.FileMinLat))
                self.lbl_north.setText(str(self.FileMaxLat))
                self.lbl_min.setText(str(self.FileMinRange))
                self.lbl_max.setText(str(self.FileMaxRange))
                self.btn_fill_defaults.setEnabled(True)
        except Exception as e:
            self.showMessage(1, '', str(e))
    
    def populateDefaults(self):
        self.txt_east.setText(str(self.FileMinLong))
        self.txt_west.setText(str(self.FileMaxLong))
        self.txt_south.setText(str(self.FileMinLat))
        self.txt_north.setText(str(self.FileMaxLat))
        self.txt_cpt_min.setText(str(self.FileMinRange))
        self.txt_cpt_max.setText(str(self.FileMaxRange))
    
    ###########################################################################################################################
    #This will add a group header to the (projections)combo box. The effect will mimic the 'optgroup' that you see in an HTML 
    #select tag. This is not a default behavior in QT, so we have to improvise.
    ###########################################################################################################################
    def addGroupHeader(self, combo, row, str):
        item = qtg.QStandardItem(str)
        item.setFlags(item.flags() ^ (qtc.Qt.ItemIsSelectable)) 

        font = item.font()
        font.setBold(True)  
        item.setFont(font)
        
        itemModel = combo.model()
        itemModel.insertRow(row, item)
    
    ###########################################################################################################################
    #This will call a QFileDialog in order to select the input file
    ###########################################################################################################################       
    def openFile(self):
        file = qtw.QFileDialog().getOpenFileName(self, 'Open File', ".\"" )
        self.txt_input_file.setText(str(file[0]))
        self.analyzeInput(str(file[0]))
      
    ###########################################################################################################################
    #This will cause the color palette control to redraw. This will fire whenever a new .cpt file is selected from the combo box
    #or when the value is changed on the transparency slider control.
    ########################################################################################################################### 
    def viewPalette(self, alpha=255):           
        val = self.slider_opacity.value()  
        cpt = self.combo_cpt.currentText() 

        #To paint the gradient, the alpha value needs to be in the range of 0-255...
        alpha = float(val/100) * 255
        self.viewer.DrawPalette(cpt, alpha)

    ###########################################################################################################################
    #This will save the interface parameters and options to a gmtMap object
    ########################################################################################################################### 
    def createMapObject(self):
        self.gmtMap.FileInput = self.txt_input_file.text().strip()
        self.gmtMap.ROINorth = self.txt_north.text().strip()
        self.gmtMap.ROISouth = self.txt_south.text().strip()
        self.gmtMap.ROIEast = self.txt_east.text().strip()
        self.gmtMap.ROIWest = self.txt_west.text().strip()
        self.gmtMap.CPTFile = self.combo_cpt.currentText()
        self.gmtMap.Opacity = self.slider_opacity.value() 
        self.gmtMap.CPTMinValue = self.txt_cpt_min.text().strip()
        self.gmtMap.CPTMaxValue = self.txt_cpt_max.text().strip()
        self.gmtMap.CPTInterval = self.txt_cpt_interval.text().strip()
        self.gmtMap.ScaleUnit = self.combo_cpt_unit.currentText() 
        self.gmtMap.Projection = self.combo_projections.currentText()

        #Get the properties from the options window...
        self.gmtMap.PageHeight = self.options.spin_page_height.value()
        self.gmtMap.PageWidth = self.options.spin_page_width.value()
        self.gmtMap.PageSizeUnit = self.options.combo_page_size_unit.currentText()
        
        if self.options.radio_symlevel0.isChecked():
            self.gmtMap.SymbologyLevel = 0
        elif self.options.radio_symlevel1.isChecked():
            self.gmtMap.SymbologyLevel = 1
        else:
            self.gmtMap.SymbologyLevel = 2 

        self.gmtMap.ScalebarInterval = self.options.spin_scalebar_interval.value()
        self.gmtMap.ScalebarOrientation = 'h' if self.options.radio_horizontal.isChecked() else 'v'  
        self.gmtMap.ScalebarPositioning = self.options.combo_scalebar_position.currentText()      
        self.gmtMap.ScalebarHeight = self.options.spin_scalebar_height.value()
        self.gmtMap.ScalebarWidth = self.options.spin_scalebar_width.value()
        self.gmtMap.ScalebarSizeUnit = self.options.combo_scalebar_size_unit.currentText()
        self.gmtMap.ScalebarXPos = self.options.spin_scalebar_x.value()
        self.gmtMap.ScalebarYPos = self.options.spin_scalebar_y.value()
        self.gmtMap.ScalebarOffsetX = self.options.spin_scalebar_offset_x.value()
        self.gmtMap.ScalebarOffsetY = self.options.spin_scalebar_offset_y.value()
        self.gmtMap.ScalebarOffsetUnit = self.options.combo_scalebar_offset_unit.currentText()
        self.gmtMap.ScalebarPosUnit = self.options.combo_scalebar_pos_unit.currentText()
        self.gmtMap.ScalebarLabelX = self.options.txt_scalebar_label_x.text().strip()
        self.gmtMap.ScalebarLabelY = self.options.txt_scalebar_label_y.text().strip()
        self.gmtMap.SymbologyShape = self.options.combo_symbols.currentText()
        self.gmtMap.SymbologySize = self.options.spin_symbology_size.value()
        self.gmtMap.SymbologySizeUnit = self.options.combo_symbology_size_unit.currentText()
        self.gmtMap.SymbologyFillColor = self.options.cbtn_symbology_fill.getCurrentFillColor()
        self.gmtMap.SymbologyBorderColor = self.options.cbtn_symbology_fill.getCurrentBorderColor()
       
    ###########################################################################################################################
    #This will call up a QFileDialog for saving the map parameters (.map file)
    ###########################################################################################################################
    def saveParameters(self):
        #Set up the file dialog with the appropriate options...
        savefile = qtw.QFileDialog.getSaveFileName(self, 'Save Map Parameters', '~/', 'Map Parameters (.map)(*.map)')[0] 
        if savefile:
            self.createMapObject()
        else:
            return

        with open(savefile, 'wb') as f:            
            pickle.dump(self.gmtMap, f)         

    ###########################################################################################################################
    #This will call up a QFileDialog for saving the load in the map parameters (.map file)
    ###########################################################################################################################
    def loadParameters(self, loadfile = None):
        if not loadfile:
            loadfile = qtw.QFileDialog.getOpenFileName(self, 'Open Map Parameters', '~/', 'Map Parameters (.map)(*.map)')[0] 
        #If user cancels the file selection, loadfile will still be null, so just return and do not throw the below exception
        if not loadfile:
            return             
        try:       
            with open(loadfile, 'rb') as f:    
                self.gmtMap = pickle.load(f)                
                self.populateForm() 
                self.analyzeInput(self.txt_input_file.text())  
        except Exception as e:
            self.showMessage(3, "Error", "The file you are attempting to load does not appear to be a valid .map file!\nError: " + str(e)) 
            #self.showMessage(3, "Error", str(e)) 

    def populateForm(self):        
        self.txt_input_file.setText(self.gmtMap.FileInput) 
        self.txt_north.setText(self.gmtMap.ROINorth)
        self.txt_south.setText(self.gmtMap.ROISouth)
        self.txt_east.setText(self.gmtMap.ROIEast)
        self.txt_west.setText(self.gmtMap.ROIWest)
        self.combo_cpt.setCurrentText(self.gmtMap.CPTFile)
        self.slider_opacity.setValue(self.gmtMap.Opacity)
        self.txt_cpt_min.setText(self.gmtMap.CPTMinValue)
        self.txt_cpt_max.setText(self.gmtMap.CPTMaxValue)
        self.txt_cpt_interval.setText(self.gmtMap.CPTInterval)
        self.combo_cpt_unit.setCurrentText(self.gmtMap.ScaleUnit)
        self.combo_projections.setCurrentText(self.gmtMap.Projection)
        #Set the options window's properties
        self.options.spin_page_height.setValue(self.gmtMap.PageHeight)
        self.options.spin_page_width.setValue(self.gmtMap.PageWidth)
        self.options.combo_page_size_unit.setCurrentText(self.gmtMap.PageSizeUnit)
        if self.gmtMap.SymbologyLevel == 0:
            self.options.radio_symlevel0.setChecked(True)
        elif self.gmtMap.SymbologyLevel == 1:
            self.options.radio_symlevel1.setChecked(True)
        else:
            self.options.radio_symlevel2.setChecked(True)       

        self.options.radio_horizontal.setChecked(True) if self.gmtMap.ScalebarOrientation == 'h' else self.options.radio_vertical.setChecked(True)
        self.options.combo_scalebar_position.setCurrentText(self.gmtMap.ScalebarPositioning)
        self.options.spin_scalebar_interval.setValue(self.gmtMap.ScalebarInterval)  
        self.options.spin_scalebar_offset_x.setValue(self.gmtMap.ScalebarOffsetX)
        self.options.spin_scalebar_offset_y.setValue(self.gmtMap.ScalebarOffsetY)
        self.options.combo_scalebar_offset_unit.setCurrentText(self.gmtMap.ScalebarOffsetUnit)
        self.options.spin_scalebar_height.setValue(self.gmtMap.ScalebarHeight)
        self.options.spin_scalebar_width.setValue(self.gmtMap.ScalebarWidth)
        self.options.combo_scalebar_size_unit.setCurrentText(self.gmtMap.ScalebarSizeUnit)
        self.options.spin_scalebar_x.setValue(self.gmtMap.ScalebarXPos)
        self.options.spin_scalebar_y.setValue(self.gmtMap.ScalebarYPos)
        self.options.combo_scalebar_pos_unit.setCurrentText(self.gmtMap.ScalebarPosUnit)
        self.options.txt_scalebar_label_x.setText(self.gmtMap.ScalebarLabelX)
        self.options.txt_scalebar_label_y.setText(self.gmtMap.ScalebarLabelY)
        self.options.combo_symbols.setCurrentText(self.gmtMap.SymbologyShape)
        self.options.spin_symbology_size.setValue(self.gmtMap.SymbologySize)
        self.options.combo_symbology_size_unit.setCurrentText(self.gmtMap.SymbologySizeUnit)
        self.options.cbtn_symbology_fill.setCurrentFillColor(self.gmtMap.SymbologyFillColor)
        self.options.cbtn_symbology_fill.setCurrentBorderColor(self.gmtMap.SymbologyBorderColor)
 
    def executeScript(self):
        self.createMapObject() 
        output = "./test_output/myTest"
        gmtMapScript(self.gmtMap, output)
        cmd = "cd " + "./test_output && sh " + 'myTest' + '.sh'        
        system(cmd)
        self.showMessage(1, "", "Process Completed!")

    def showMessage(self, icon, title, str):
        m = qtw.QMessageBox(self)  
        m.setIcon(icon)
        m.setWindowTitle(title)
        m.setText(str) 
        m.exec()

    @property
    def FileMinLong(self):
        return self.__FileMinLong
    @FileMinLong.setter 
    def FileMinLong(self, min):
        self.__FileMinLong = min

    @property
    def FileMaxLong(self):
        return self.__FileMaxLong
    @FileMaxLong.setter 
    def FileMaxLong(self, max):
        self.__FileMaxLong = max

    @property
    def FileMinLat(self):
        return self.__FileMinLat
    @FileMinLat.setter 
    def FileMinLat(self, min):
        self.__FileMinLat = min

    @property
    def FileMaxLat(self):
        return self.__FileMaxLat 
    @FileMaxLat.setter 
    def FileMaxLat(self, max):
        self.__FileMaxLat = max

    @property
    def FileMinRange(self):
        return self.__FileMinRange
    @FileMinRange.setter 
    def FileMinRange(self, min):
        self.__FileMinRange = min

    @property
    def FileMaxRange(self):
        return self.__FileMaxRange
    @FileMaxRange.setter 
    def FileMaxRange(self, max):
        self.__FileMaxRange = max

    @property
    def FileMinSize(self):
        return self.__FileMinSize
    @FileMinSize.setter 
    def FileMinSize(self, min):
        self.__FileMinSize = min

    @property
    def FileMaxSize(self):
        return self.__FileMaxSize
    @FileMaxSize.setter 
    def FileMaxSize(self, max):
        self.__FileMaxSize = max

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = mainWin()
    sys.exit(app.exec())


