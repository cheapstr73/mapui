#!/usr/bin/python
####################### NEED TO DO ITEMS ####################
#Verify all settings before enabling the execute button
#Verify all max values are greater than min values...
#Do a better job of verifying .map file load!

from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 
from PyQt5 import uic
from os import walk, system, path
from support.data.mapuiSettings import mapuiSettings
from support.data.gmtFont import gmtFont
from support.data.gmtMap import gmtMap
from support.widgets.ColorPaletteViewer import PaletteViewer
from support.data.gmtMapScript import gmtMapScript
from support.data.gmtProjection import gmtProjection
from support.view.gmtMapOptionsWin import mapUIOptions
from support.view.gmtProjectionWin import gmtProjectionWin 
import sys
import pickle
import re

###########################################################################################################################
#This class loads the interface.ui file and creates the main interface
###########################################################################################################################
class mainWin(qtw.QDialog):
    def __init__(self):
        super(mainWin, self).__init__()
        uic.loadUi('./support/interfaces/interface.ui', self)
        #CHANGE BACK TO USER HOME DIR WHEN DONE TESTING...
        self.currentDir = "/mnt/566A02716A024E65/MAPUI-BACKUP/GitHub/mapui/"

        #Fix the window dimensions
        self.setFixedWidth(510)
        self.setFixedHeight(630)

        #Decare the icons to be used...
        self.windowIcon = qtg.QIcon('./support/icons/map7.png')
        self.populateIcon = qtg.QIcon('./support/icons/fill1')
        self.saveIcon = qtg.QIcon('./support/icons/save4.png')
        self.openIcon = qtg.QIcon('./support/icons/open-file.png')
        self.projectionIcon = qtg.QIcon('./support/icons/globe2.png')
        self.loadIcon = qtg.QIcon('./support/icons/open3.png')
        self.optionsIcon = qtg.QIcon('./support/icons/options10.png')
        self.helpIcon = qtg.QIcon('./support/icons/help1.png')
        self.aboutIcon = qtg.QIcon('./support/icons/help2.png')
        self.executeIcon = qtg.QIcon('./support/icons/run2.png')

        #Create a gmtMap object...
        self.gmtMap = gmtMap()
        
        #Create the options window
        self.options = mapUIOptions(self)
        self.projections = gmtProjectionWin(self) 
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
        self.btn_file_input.setIcon(self.openIcon)
        self.btn_fill_defaults.setIcon(self.populateIcon)
        self.btn_set_projection.setIcon(self.projectionIcon)        
        self.btn_save.setIcon(self.saveIcon)
        self.btn_load.setIcon(self.loadIcon)
        self.btn_options.setIcon(self.optionsIcon)
        self.btn_execute.setIcon(self.executeIcon)
        self.btn_file_output.setIcon(self.openIcon)
        
        #Set button cursors
        self.btn_file_input.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_fill_defaults.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.btn_set_projection.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))

        #Add signals to the slots 
        self.combo_cpt.currentIndexChanged.connect(self.viewPalette)   
        self.btn_file_input.clicked.connect(self.inputFile)  
        self.btn_file_output.clicked.connect(self.outputFile)
        self.btn_fill_defaults.clicked.connect(self.populateDefaults)      
        self.slider_opacity.valueChanged.connect(self.getSliderValue)
        self.btn_save.clicked.connect(self.saveParameters)
        self.btn_load.clicked.connect(self.loadParameters)
        self.btn_options.clicked.connect(self.openOptions)
        self.btn_execute.clicked.connect(self.executeScript)
        self.projections.submitted.connect(self.lbl_projection.setText)        
        self.btn_set_projection.clicked.connect(self.openProjections)


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
        
        #self.txt_file_open.setFocus()
        self.lbl_slider_value.setText(str(self.slider_opacity.value()) + "%")
        self.btn_fill_defaults.setEnabled(False)

        self.btn_execute.setEnabled(False)
        self.monitorControls()
        self.lockExecute()
                

    def centerInterface(self):
        pass

    def monitorControls(self):
        self.txt_file_input.textChanged.connect(self.lockExecute)
        self.txt_north.textChanged.connect(self.lockExecute)
        self.txt_south.textChanged.connect(self.lockExecute)
        self.txt_east.textChanged.connect(self.lockExecute)
        self.txt_west.textChanged.connect(self.lockExecute)
        self.txt_cpt_min.textChanged.connect(self.lockExecute)
        self.txt_cpt_max.textChanged.connect(self.lockExecute)
        self.txt_cpt_interval.textChanged.connect(self.lockExecute)
        self.combo_cpt_unit.currentIndexChanged.connect(self.lockExecute)
        self.txt_file_output.textChanged.connect(self.lockExecute)
        self.projections.submitted.connect(self.lockExecute)

    def lockExecute(self):
        if (not self.txt_file_input.text() or 
        not self.txt_north.text() or
        not self.txt_south.text() or
        not self.txt_east.text() or
        not self.txt_west.text() or  
        not self.txt_cpt_min.text() or
        not self.txt_cpt_max.text() or
        not self.txt_cpt_interval.text() or
        not self.combo_cpt_unit.currentText() or
        not self.txt_file_output.text() or
        not self.lbl_projection.text()
        ):
            self.btn_execute.setEnabled(False)
            return
        self.btn_execute.setEnabled(True)
        
    ###########################################################################################################################
    #This will create the file menu and sub-menu items
    ##########################################################################################################################
    def createFileMenu(self):
        self.convertFormat = 'f'

        menuBar = qtw.QMenuBar()
        fileMenu = menuBar.addMenu('&File')
        optionsMenu = menuBar.addMenu('&Options')
        self.convertMenu = menuBar.addMenu('&Output Formats')
        helpMenu = menuBar.addMenu('&Help')

        #Create the menu item actions
        saveAction = qtw.QAction(self.saveIcon, '&Save Parameters', self)
        loadAction = qtw.QAction(self.loadIcon, '&Load Parameters', self)
        optionsAction = qtw.QAction(self.optionsIcon, '&Options', self)

        #These are the checkable menu items for output conversion formats...
        self.bmpAction = qtw.QAction('BMP (Bitmap', self)
        self.epsAction = qtw.QAction('EPS (Encapsulated PostScript)', self)     
        self.jpgAction = qtw.QAction('JPG (JPEG)', self)
        self.pdfAction = qtw.QAction('PDF (Portable Document Format)', self)
        self.pngAction = qtw.QAction('PNG (Portable Network Graphic)', self)
        self.pngTAction = qtw.QAction('PNG (With Transparency)', self)
        self.ppmAction = qtw.QAction('PPM (Portable Pixmap Image)', self)
        #self.svgAction = qtw.QAction('SVG (Scalable Vector Graphic)', self)
        self.tiffAction = qtw.QAction('TIFF (Tagged Image File Format)', self)
        helpAction = qtw.QAction(self.helpIcon, '&Help', self)
        aboutAction = qtw.QAction(self.windowIcon, '&About MapUI', self)
        
        #Group the clickable menu items into a 
        group = qtw.QActionGroup(self.convertMenu)
        group.setExclusive(True)
        group.addAction(self.bmpAction)
        group.addAction(self.epsAction)
        group.addAction(self.jpgAction)
        group.addAction(self.pdfAction)
        group.addAction(self.pngAction)
        group.addAction(self.pngTAction)
        group.addAction(self.ppmAction)
        #group.addAction(self.svgAction)
        group.addAction(self.tiffAction)

        #Set the output formats to checkable items...
        self.bmpAction.setCheckable(True)
        self.epsAction.setCheckable(True)
        self.pdfAction.setCheckable(True)        
        self.jpgAction.setCheckable(True)
        self.pngAction.setCheckable(True)
        self.pngTAction.setCheckable(True)
        self.ppmAction.setCheckable(True)
        #self.svgAction.setCheckable(True)
        self.tiffAction.setCheckable(True)

        #Add the menu events...
        saveAction.triggered.connect(self.saveParameters)
        loadAction.triggered.connect(self.loadParameters)
        optionsAction.triggered.connect(self.openOptions)
        self.bmpAction.triggered.connect(lambda status : self.toggleFormat('b'))
        self.epsAction.triggered.connect(lambda status : self.toggleFormat('e'))
        self.jpgAction.triggered.connect(lambda status : self.toggleFormat('j'))
        self.pdfAction.triggered.connect(lambda status : self.toggleFormat('f'))
        self.pngAction.triggered.connect(lambda status : self.toggleFormat('g'))
        self.pngTAction.triggered.connect(lambda status : self.toggleFormat('G'))
        self.ppmAction.triggered.connect(lambda status : self.toggleFormat('m'))
        #self.svgAction.triggered.connect(lambda status : self.toggleFormat('s'))
        self.tiffAction.triggered.connect(lambda status : self.toggleFormat('t'))

        #Add menu items to the menus
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)
        optionsMenu.addAction(optionsAction)
        self.convertMenu.addAction(self.bmpAction)
        self.convertMenu.addAction(self.epsAction)       
        self.convertMenu.addAction(self.jpgAction)
        self.convertMenu.addAction(self.pdfAction)
        self.convertMenu.addAction(self.pngAction)
        self.convertMenu.addAction(self.pngTAction)
        self.convertMenu.addAction(self.ppmAction)
        #self.convertMenu.addAction(self.svgAction)
        self.convertMenu.addAction(self.tiffAction)
        helpMenu.addAction(aboutAction)
        helpMenu.addAction(helpAction)
        self.menu_layout.addWidget(menuBar)
        self.pdfAction.setChecked(True)

    ###########################################################################################################################
    #Add/Remove items from the convertFormats list; based on the state of each checkable menu item
    ###########################################################################################################################
    def toggleFormat(self, filetype):
        self.convertFormat = filetype

    ###########################################################################################################################
    #Show the main options window
    ###########################################################################################################################
    def openOptions(self):        
        self.options.show()

    def openProjections(self):       
        self.projections.show()
            
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
    #Read the input file. It should only be plain text with 4 columns (Longitude, Latitude, and 2 other columns containing
    #numerical data). While reading, split the file into 4 lists, sort them, and return the min and max values for each column.
    #These values will be displayed on the UI to give the user the numerical 'bounds' of the file.
    ###########################################################################################################################    
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
                       break                    
                col0.sort()
                col1.sort()
                col2.sort()
                col3.sort()
                #Set min/max longitude values
                self.FileMinLong = col0[0]
                self.FileMaxLong = col0[-1]
                #Set min/max latitude values
                self.FileMinLat = col1[0]
                self.FileMaxLat = col1[-1]
                #Set min/max cpt range values
                self.FileMinRange = col2[0]
                self.FileMaxRange = col2[-1] 
                #Set min/max size values (column 4 of the input file)
                self.FileMaxSize = col3[0]
                self.FileMaxSize = col3[-1]
                #Shouldn't be needed, but just to be on the safe side...
                col0 = None
                col1 = None
                col2 = None
                col3 = None

                #Set the hint labels with the appropriate text values...
                self.lbl_east.setText(str(self.FileMinLong))
                self.lbl_west.setText(str(self.FileMaxLong))
                self.lbl_south.setText(str(self.FileMinLat))
                self.lbl_north.setText(str(self.FileMaxLat))
                self.lbl_min.setText(str(self.FileMinRange))
                self.lbl_max.setText(str(self.FileMaxRange))
                self.btn_fill_defaults.setEnabled(True)
        except: 
            self.showMessage(3,'Unknown Format', 'There are problems with the format of this file.\nProcessing this file may produce unexpected results.')
    
    def populateDefaults(self):
        self.txt_east.setText(str(self.FileMinLong))
        self.txt_west.setText(str(self.FileMaxLong))
        self.txt_south.setText(str(self.FileMinLat))
        self.txt_north.setText(str(self.FileMaxLat))
        self.txt_cpt_min.setText(str(self.FileMinRange))
        self.txt_cpt_max.setText(str(self.FileMaxRange))
    
    ###########################################################################################################################
    #This will call a QFileDialog in order to select the input file
    ###########################################################################################################################       
    def inputFile(self):
        file = qtw.QFileDialog().getOpenFileName(self, 'Open File', self.currentDir )[0]
        if file:
            self.txt_file_input.setText(str(file))
            self.currentDir = path.split(file)[0]
            self.analyzeInput(str(file))
        else:
            return

    ###########################################################################################################################
    #This will call a QFileDialog in order to select the output file
    ###########################################################################################################################       
    def outputFile(self): 
        file = qtw.QFileDialog().getSaveFileName(self, 'Output File', self.currentDir, "Postscript Files (*.ps)" )[0] 
        if file:
            self.txt_file_output.setText(str(file))
            self.currentDir = path.split(file)[0]             
        else:
            return

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
    #This will call up a QFileDialog for saving the map parameters (.map file)
    ###########################################################################################################################
    def saveParameters(self):
        #Set up the file dialog with the appropriate options...
        savefile = qtw.QFileDialog.getSaveFileName(self, 'Save Map Parameters', self.currentDir, 'Map Parameters (.map)(*.map)')[0] 
        if savefile:
            self.createMapObject()
            self.currentDir = path.split(savefile)[0]
        else:
            return

        with open(savefile, 'wb') as f:            
            pickle.dump(self.gmtMap, f)         

    ###########################################################################################################################
    #This will call up a QFileDialog for saving the load in the map parameters (.map file)
    ###########################################################################################################################
    def loadParameters(self, loadfile = None):
        if not loadfile:
            loadfile = qtw.QFileDialog.getOpenFileName(self, 'Open Map Parameters', self.currentDir, 'Map Parameters (.map)(*.map)')[0] 
        if loadfile:
            self.currentDir = path.split(loadfile)[0]
        else:
            return            
        try:       
            with open(loadfile, 'rb') as f:    
                self.gmtMap = pickle.load(f)                
                self.populateForm() 
                self.analyzeInput(self.txt_file_input.text())   
        except Exception as e:
            self.showMessage(3, "Error", "The file you are attempting to load does not appear to be a valid .map file!\nError: " + str(e)) 
            
    ###########################################################################################################################
    #This will save the interface parameters and options to a gmtMap object. The values will come from each UI control.
    ########################################################################################################################### 
    def createMapObject(self):
        ################################################################################
        #Main Form UI - ...only a handful of items here.
        ################################################################################ 
        self.gmtMap.FileInput = self.txt_file_input.text().strip()
        
        #Region of Interest
        self.gmtMap.ROINorth = self.txt_north.text().strip()
        self.gmtMap.ROISouth = self.txt_south.text().strip()
        self.gmtMap.ROIEast = self.txt_east.text().strip()
        self.gmtMap.ROIWest = self.txt_west.text().strip()        
        
        #Color Palette Table
        self.gmtMap.CPTFile = self.combo_cpt.currentText()
        self.gmtMap.Opacity = self.slider_opacity.value()         
        self.gmtMap.CPTMinValue = self.txt_cpt_min.text().strip()
        self.gmtMap.CPTMaxValue = self.txt_cpt_max.text().strip()
        self.gmtMap.CPTInterval = self.txt_cpt_interval.text().strip()
        self.gmtMap.ScaleUnit = self.combo_cpt_unit.currentText()  
        
        #File Output
        self.gmtMap.FileOutput = self.txt_file_output.text().strip()

        ################################################################################
        #Advanced options window - Map tab
        ################################################################################
        self.gmtMap.PageHeight = self.options.spin_page_height.value()
        self.gmtMap.PageWidth = self.options.spin_page_width.value()
        self.gmtMap.PageSizeUnit = self.options.combo_page_size_unit.currentText()   
        
        #Map Title
        self.gmtMap.MapTitleAdd = self.options.chk_add_map_title.isChecked()    
        self.gmtMap.MapTitle = gmtFont(self.options.combo_map_title_font.currentText(), 
                                       self.options.spin_map_title_font_size.value(), 
                                       self.options.getMapTitleColor(), 
                                       self.options.txt_map_title.text().strip())       
        self.gmtMap.MapTitleOffsetX = self.options.spin_map_title_offset_x.value()
        self.gmtMap.MapTitleOffsetY = self.options.spin_map_title_offset_y.value()
        self.gmtMap.MapTitleOffsetUnit = self.options.combo_map_title_offset_unit.currentText()
        
        self.gmtMap.MapClassificationAdd = self.options.chk_add_map_classification.isChecked()    
        self.gmtMap.MapClassification = gmtFont(self.options.combo_map_classification_font.currentText(), 
                                                self.options.spin_map_classification_font_size.value(), 
                                                self.options.getMapClassificationColor(), 
                                                self.options.txt_map_classification.text().strip())
        self.gmtMap.MapClassificationOffsetX = self.options.spin_map_classsification_offset_x.value()
        self.gmtMap.MapClassificationOffsetY = self.options.spin_map_classsification_offset_y.value()
        self.gmtMap.MapClassificationOffsetUnit = self.options.combo_map_classification_offset_unit.currentText()
        #self.gmtMap.MapTitleFontSize = self.options.spin_map_title_font_size.value()
        
        ################################################################################
        #Advanced options window - Symbology tab
        ################################################################################           
        if self.options.radio_symlevel0.isChecked(): #The 3 symbology levels
            self.gmtMap.SymbologyLevel = 0
        elif self.options.radio_symlevel1.isChecked():
            self.gmtMap.SymbologyLevel = 1
        else:
            self.gmtMap.SymbologyLevel = 2 
        self.gmtMap.SymbologyShape = self.options.combo_symbols.currentText()
        self.gmtMap.SymbologyFillColor = self.options.cbtn_symbology_fill.getCurrentFillColor()
        self.gmtMap.SymbologyBorderColor = self.options.cbtn_symbology_fill.getCurrentBorderColor()
        self.gmtMap.SymbologySize = self.options.spin_symbology_size.value()
        self.gmtMap.SymbologySizeUnit = self.options.combo_symbology_size_unit.currentText()
        
        #Coastline Data
        self.gmtMap.CoastlineResolution = self.options.combo_resolution.currentText()
        self.gmtMap.CoastlineLandFillColor = self.options.cbtn_coastlines_fill.getCurrentFillColor()
        self.gmtMap.CoastlineWaterFillColor = self.options.cbtn_coastlines_water_fill.getCurrentFillColor()
        self.gmtMap.CoastlineBorderColor = self.options.lcbtn_coastline_border.getCurrentLineColor()
        self.gmtMap.CoastlineBorderWeight = self.options.lcbtn_coastline_border.getCurrentLineWeight()
        self.gmtMap.CoastlineNationalBoundaryType = self.options.combo_coastline_national_boundary_type.currentText()
        self.gmtMap.CoastlineNationalBoundaryColor = self.options.lcbtn_national_boundary.getCurrentLineColor()
        self.gmtMap.CoastlineNationalBoundaryWeight = self.options.lcbtn_national_boundary.getCurrentLineWeight()
        self.gmtMap.CoastlineRiverType = self.options.combo_coastline_river_type.currentText()
        self.gmtMap.CoastlineRiverColor = self.options.lcbtn_rivers.getCurrentLineColor()
        self.gmtMap.CoastlineRiverWeight = self.options.lcbtn_rivers.getCurrentLineWeight()
        
        ################################################################################
        #Advanced options window - Scalebar tab
        ################################################################################    
        self.gmtMap.ScalebarOrientation = 'h' if self.options.radio_horizontal.isChecked() else 'v'     
        self.gmtMap.ScalebarHeight = self.options.spin_scalebar_height.value()
        self.gmtMap.ScalebarWidth = self.options.spin_scalebar_width.value()
        self.gmtMap.ScalebarSizeUnit = self.options.combo_scalebar_size_unit.currentText()
        
        #Positioning
        self.gmtMap.ScalebarPositioning = self.options.combo_scalebar_position.currentText()  
        self.gmtMap.ScalebarXPos = self.options.spin_scalebar_x.value()
        self.gmtMap.ScalebarYPos = self.options.spin_scalebar_y.value()       
        self.gmtMap.ScalebarPosUnit = self.options.combo_scalebar_pos_unit.currentText()        
        self.gmtMap.ScalebarInterval = self.options.spin_scalebar_interval.value()  
        self.gmtMap.ScalebarOffsetX = self.options.spin_scalebar_offset_x.value()
        self.gmtMap.ScalebarOffsetY = self.options.spin_scalebar_offset_y.value()
        self.gmtMap.ScalebarOffsetUnit = self.options.combo_scalebar_offset_unit.currentText()

        #Labels
        self.gmtMap.ScalebarLabelX = self.options.txt_scalebar_label_x.text().strip()
        self.gmtMap.ScalebarLabelY = self.options.txt_scalebar_label_y.text().strip()
        self.gmtMap.ScalebarIlluminate = self.options.chk_illuminate.isChecked()       

        #Create the projection
        self.gmtMap.Projection = gmtProjection(self.projections.combo_projections.currentText(),
                                               self.gmtMap.getCM(),
                                               self.gmtMap.PageWidth)
        #Package the output types..
        self.gmtMap.ConvertTypes = self.convertFormat         

            
    ###########################################################################################################################
    #This will be called on form load. If gmtMap is populated with data, the data will be used to populate all of the items
    #on the main UI form, as well as the advanced options window.
    ###########################################################################################################################
    def populateForm(self):  
        ################################################################################
        #Main Form UI - ...only a handful of items here.
        ################################################################################           
        self.txt_file_input.setText(self.gmtMap.FileInput) 
        
        #Region of Interest
        self.txt_north.setText(self.gmtMap.ROINorth)
        self.txt_south.setText(self.gmtMap.ROISouth)
        self.txt_east.setText(self.gmtMap.ROIEast)
        self.txt_west.setText(self.gmtMap.ROIWest)
        
        #Color Palette Table
        self.combo_cpt.setCurrentText(self.gmtMap.CPTFile)
        self.slider_opacity.setValue(self.gmtMap.Opacity)
        self.txt_cpt_min.setText(self.gmtMap.CPTMinValue)
        self.txt_cpt_max.setText(self.gmtMap.CPTMaxValue)
        self.txt_cpt_interval.setText(self.gmtMap.CPTInterval)
        self.combo_cpt_unit.setCurrentText(self.gmtMap.ScaleUnit)
        
        #Output File
        self.txt_file_output.setText(self.gmtMap.FileOutput)

        ################################################################################
        #Advanced options window - Map tab
        ################################################################################
        self.options.spin_page_height.setValue(self.gmtMap.PageHeight)
        self.options.spin_page_width.setValue(self.gmtMap.PageWidth)
        self.options.combo_page_size_unit.setCurrentText(self.gmtMap.PageSizeUnit)

        #Map Title
        self.options.chk_add_map_title.setChecked(self.gmtMap.MapTitleAdd)
        self.options.txt_map_title.setText(self.gmtMap.MapTitle.text)
        self.options.spin_map_title_offset_x.setValue(self.gmtMap.MapTitleOffsetX)
        self.options.spin_map_title_offset_y.setValue(self.gmtMap.MapTitleOffsetY)
        self.options.combo_map_title_offset_unit.setCurrentText(self.gmtMap.MapTitleOffsetUnit)
        self.options.combo_map_title_font.setCurrentText(self.gmtMap.MapTitle.font)
        self.options.spin_map_title_font_size.setValue(self.gmtMap.MapTitle.size)
        self.options.setMapTitleColor(self.gmtMap.MapTitle.color)

        #Map Classification
        self.options.chk_add_map_classification.setChecked(self.gmtMap.MapClassificationAdd)
        self.options.txt_map_classification.setText(self.gmtMap.MapClassification.text)
        self.options.spin_map_classsification_offset_x.setValue(self.gmtMap.MapClassificationOffsetX)
        self.options.spin_map_classsification_offset_y.setValue(self.gmtMap.MapClassificationOffsetY)
        self.options.combo_map_classification_offset_unit.setCurrentText(self.gmtMap.MapClassificationOffsetUnit)        
        self.options.combo_map_classification_font.setCurrentText(self.gmtMap.MapClassification.font)
        self.options.spin_map_classification_font_size.setValue(self.gmtMap.MapClassification.size)
        self.options.setMapClassificationColor(self.gmtMap.MapClassification.color)

        ################################################################################
        #Advanced options window - Symbology Tab
        ################################################################################
        if self.gmtMap.SymbologyLevel == 0: #The 3 symbology options...
                self.options.radio_symlevel0.setChecked(True)
        elif self.gmtMap.SymbologyLevel == 1:
            self.options.radio_symlevel1.setChecked(True)
        else:
            self.options.radio_symlevel2.setChecked(True) 

        self.options.combo_symbols.setCurrentText(self.gmtMap.SymbologyShape)
        self.options.cbtn_symbology_fill.setCurrentFillColor(self.gmtMap.SymbologyFillColor)
        self.options.cbtn_symbology_fill.setCurrentBorderColor(self.gmtMap.SymbologyBorderColor)
        self.options.spin_symbology_size.setValue(self.gmtMap.SymbologySize)
        self.options.combo_symbology_size_unit.setCurrentText(self.gmtMap.SymbologySizeUnit)

        #Coastline Data Symbology 
        self.options.combo_resolution.setCurrentText(self.gmtMap.CoastlineResolution)
        self.options.cbtn_coastlines_fill.setCurrentFillColor(self.gmtMap.CoastlineLandFillColor)
        self.options.cbtn_coastlines_water_fill.setCurrentFillColor(self.gmtMap.CoastlineWaterFillColor)
        self.options.lcbtn_coastline_border.setCurrentLineColor(self.gmtMap.CoastlineBorderColor)
        self.options.lcbtn_coastline_border.setCurrentLineWeight(self.gmtMap.CoastlineBorderWeight)
        self.options.combo_coastline_national_boundary_type.setCurrentText(self.gmtMap.CoastlineNationalBoundaryType) 
        self.options.lcbtn_national_boundary.setCurrentLineColor(self.gmtMap.CoastlineNationalBoundaryColor)
        self.options.lcbtn_national_boundary.setCurrentLineWeight(self.gmtMap.CoastlineNationalBoundaryWeight)
        self.options.combo_coastline_river_type.setCurrentText(self.gmtMap.CoastlineRiverType)
        self.options.lcbtn_rivers.setCurrentLineColor(self.gmtMap.CoastlineRiverColor)
        self.options.lcbtn_rivers.setCurrentLineWeight(self.gmtMap.CoastlineRiverWeight)

        ################################################################################
        #Advanced options window - Scalebar Tab
        ################################################################################
        self.options.radio_horizontal.setChecked(True) if self.gmtMap.ScalebarOrientation == 'h' else self.options.radio_vertical.setChecked(True)
        self.options.spin_scalebar_height.setValue(self.gmtMap.ScalebarHeight)
        self.options.spin_scalebar_width.setValue(self.gmtMap.ScalebarWidth)
        self.options.combo_scalebar_size_unit.setCurrentText(self.gmtMap.ScalebarSizeUnit)

        #Positioning
        self.options.combo_scalebar_position.setCurrentText(self.gmtMap.ScalebarPositioning)
        self.options.spin_scalebar_x.setValue(self.gmtMap.ScalebarXPos)
        self.options.spin_scalebar_y.setValue(self.gmtMap.ScalebarYPos)
        self.options.combo_scalebar_pos_unit.setCurrentText(self.gmtMap.ScalebarPosUnit)        
        self.options.spin_scalebar_offset_x.setValue(self.gmtMap.ScalebarOffsetX)
        self.options.spin_scalebar_offset_y.setValue(self.gmtMap.ScalebarOffsetY)
        self.options.combo_scalebar_offset_unit.setCurrentText(self.gmtMap.ScalebarOffsetUnit)

        #Labels
        self.options.txt_scalebar_label_x.setText(self.gmtMap.ScalebarLabelX)
        self.options.txt_scalebar_label_y.setText(self.gmtMap.ScalebarLabelY)
        self.options.spin_scalebar_interval.setValue(self.gmtMap.ScalebarInterval)  
        self.options.chk_illuminate.setChecked(self.gmtMap.ScalebarIlluminate)             
            
        #Map Projection
        if self.gmtMap.Projection:
            self.lbl_projection.setText(self.gmtMap.Projection.Name)
        else:
            self.lbl_projection.setText("No map projection selected...")
   
    ###########################################################################################################################
    #This will execute the shell script. This is only for testing purposes. This is a placeholder until a more 'robust' 
    #procedure is written
    ###########################################################################################################################         
    def executeScript(self):
        self.createMapObject()  
        gmtMapScript(self.gmtMap)
        cmd = "cd \'" +  path.split(self.gmtMap.FileOutput)[0] + "\' && sh ." + path.split(self.gmtMap.FileOutput)[1][:-3] + '.sh'                  
        system(cmd)
        self.showMessage(1, "", "Process Completed!")

    ###########################################################################################################################
    #Testing function....this will go away in the end...
    ########################################################################################################################### 
    def showMessage(self, icon, title, str):
        m = qtw.QMessageBox(self)  
        m.setIcon(icon)
        m.setWindowTitle(title)
        m.setText(str) 
        m.exec()
    
    #Add a few properties for the UI.
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


