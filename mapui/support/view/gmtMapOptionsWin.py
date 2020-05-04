from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 
from PyQt5 import uic
from support.data.mapuiSettings import mapuiSettings
from support.widgets.ColorToolButton import ColorToolButton
from support.widgets.ColorButton import ColorButton
from support.widgets.LineColorButton import LineColorButton

###########################################################################################################################
#This class loads the options.ui file and creates the options window
###########################################################################################################################
class mapUIOptions(qtw.QDialog):
    def __init__(self, *args, **kwargs):
        super(mapUIOptions, self).__init__(*args, **kwargs) 
        uic.loadUi('./support/interfaces/options.ui', self)
        
        #Fix the window dimensions
        self.setFixedWidth(489)
        self.setFixedHeight(565)
        
        self.setupInterface()  
        
        #Setup the control initializations on each tab
        self.setupMapPageTab()
        self.setupMapFrameTab()
        self.setupSymbologyTab()
        self.setupScalebarTab()

    def setupInterface(self):
        self.fonts = mapuiSettings.getGMTFonts()   
        
        #Set the options window main icon
        self.setWindowIcon(qtg.QIcon('./support/icons/options10.png'))
        
        #Setup the close button and signal
        self.btn_options_close.setIcon(qtg.QIcon('./support/icons/close5.png'))
        self.btn_options_close.clicked.connect(self.close)

        #Set Tab Icons and icons for all controls (all tabs)
        self.options_tab.setTabIcon(0, qtg.QIcon('./support/icons/map9.png'))
        self.options_tab.setTabIcon(1, qtg.QIcon('./support/icons/frame4.png'))
        self.options_tab.setTabIcon(2, qtg.QIcon('./support/icons/points2.png'))
        self.options_tab.setTabIcon(3, qtg.QIcon('./support/icons/scale4.png'))
        #Map Page
        self.btn_map_title_font_color.setIcon(qtg.QIcon('./support/icons/color2.png'))
        self.btn_map_classification_font_color.setIcon(qtg.QIcon('./support/icons/color2.png'))
        self.iconH = qtg.QPixmap('./support/icons/orientationH2.png')
        self.iconP = qtg.QPixmap('./support/icons/orientationP2.png')
        self.colorPaletteIcon = qtg.QIcon('./support/icons/color2.png')
        #Map Frame
        self.btn_frame_font_color.setIcon(qtg.QIcon('./support/icons/color2.png'))
     
    ###########################################################################################################################
    #This will initialize the controls on the Map Page Tab
    ###########################################################################################################################
    def setupMapPageTab(self):
        self.combo_page_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        
        #Populate the map title and classification fonts combo box        
        for font in self.fonts:
            self.combo_map_title_font.addItem(font[0])
            self.combo_map_classification_font.addItem(font[0])
        
        #Add a mouse press event to the page orientaion icon label
        self.lbl_orientation.mousePressEvent = self.lblOrientationClick 
            
        #Setup the control signals
        self.btn_map_title_font_color.clicked.connect(self.chooseFontColor)
        self.btn_map_classification_font_color.clicked.connect(self.chooseFontColor)
        self.spin_page_height.valueChanged.connect(self.swapIcon)
        self.spin_page_width.valueChanged.connect(self.swapIcon)
        self.chk_add_map_title.stateChanged.connect(self.toggleMapTitle)
        self.chk_add_map_classification.stateChanged.connect(self.toggleClassification) 
        
        #Initialize the control view
        self.swapIcon()
        self.toggleMapTitle()
        self.toggleClassification()
       
    ###########################################################################################################################
    #This will initialize the controls on the Map Frame Tab
    ###########################################################################################################################
    def setupMapFrameTab(self):        
        #ColorButton for map frame
        self.lcbtn_map_frame = LineColorButton(qtg.QColor(0,0,0), 1.0, 1.0)
        self.map_frame_color_layout.addWidget(self.lcbtn_map_frame)
        
        #LineColorButton for gridlines
        self.lcbtn_gridlines = LineColorButton(qtg.QColor(255,0,0), .25, .25)
        self.map_frame_gridlines_layout.addWidget(self.lcbtn_gridlines) 
        
        #LineColorButton for Grid Ticks 
        self.lcbtn_grid_ticks = LineColorButton(qtg.QColor(0,0,0), .5, .25)
        self.grid_tick_layout.addWidget(self.lcbtn_grid_ticks)
        
        
        #Populate the combo boxes
        self.combo_frame_type.addItems(mapuiSettings.getMapFrameTypes())
        self.combo_frame_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure()) 
        for font in self.fonts:
            self.combo_frame_font.addItem(font[0])
            
        #Setup the control signals 
        self.btn_frame_font_color.clicked.connect(self.chooseFontColor)
        self.chk_grid_ticks.stateChanged.connect(self.toggleGridTicks)
        self.toggleGridTicks()
        
    ###########################################################################################################################
    #This will initialize the controls on the Symbology Tab
    ###########################################################################################################################
    def setupSymbologyTab(self):
        #Setup the cursors to change on label hover
        self.lbl_symlevel0.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel1.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel2.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_orientation.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor)) 
        
        #Add a click event for the 3 labels (for the symbology levels)
        self.lbl_symlevel0.mousePressEvent = self.lbl0Click
        self.lbl_symlevel1.mousePressEvent = self.lbl1Click
        self.lbl_symlevel2.mousePressEvent = self.lbl2Click
      
        #Populate the combo boxes... 
        self.combo_symbology_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_resolution.addItems(mapuiSettings.getResolutions()) 
        self.combo_resolution.setCurrentText("Low")   
        
        #The following three combo boxes populate based off a returned tuple. Item[0] holds the name.        
        for item in mapuiSettings.getSymbols(): #Add the symbol names to the combo box
            self.combo_symbols.addItem(item[0])            
        
        for item in mapuiSettings.getBorderTypes(): #Add the coastline border types combo box values
            self.combo_coastline_national_boundary_type.addItem(item[0])
        
        for item in mapuiSettings.getRiverTypes(): #Add the coastline river types combo box values
            self.combo_coastline_river_type.addItem(item[0])
    
        #ColorToolButton for Symbology
        self.cbtn_symbology_fill = ColorToolButton()
        self.color_button_layout.addWidget(self.cbtn_symbology_fill)
        
        #ColorButton for coastline data (land)
        self.cbtn_coastlines_fill = ColorButton()
        self.coastline_color_layout.addWidget(self.cbtn_coastlines_fill)
        
        #ColorButton for coastline data (water)
        self.cbtn_coastlines_water_fill = ColorButton()
        self.coastline_water_color_layout.addWidget(self.cbtn_coastlines_water_fill)
         
        #LineColorButton for coastline borders
        self.lcbtn_coastline_border = LineColorButton()
        self.coastline_border_layout.addWidget(self.lcbtn_coastline_border)
        
        #Coastline National Boundary data 
        self.lcbtn_national_boundary = LineColorButton(qtg.QColor(170,170,170), .5, .25)
        self.coastline_national_boundary_layout.addWidget(self.lcbtn_national_boundary)
        
        #Coastline River Data...
        self.lcbtn_rivers = LineColorButton(qtg.QColor(85,170,255), .5, .25) 
        self.coastline_river_color_layout.addWidget(self.lcbtn_rivers)
        
        #Setup the control signals
        self.radio_symlevel0.clicked.connect(self.checkLevels)
        self.radio_symlevel1.clicked.connect(self.checkLevels)
        self.radio_symlevel2.clicked.connect(self.checkLevels)
        
        #Initialize the control view
        self.checkLevels()
  
    ###########################################################################################################################
    #This will initialize the controls on the Scalebar Tab
    ###########################################################################################################################
    def setupScalebarTab(self):
        #LineColorButton for Scalebar Frame 
        self.lcbtn_scalebar_frame_border = LineColorButton()
        self.scalebar_frame_border.addWidget(self.lcbtn_scalebar_frame_border)
        
        #ColorButton for Scalebar Frame background fill
        self.cbtn_scalebar_frame_fill = ColorButton()
        self.scalebar_frame_fill_layout.addWidget(self.cbtn_scalebar_frame_fill)
        
        #Populate the combo boxes
        self.combo_scalebar_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_scalebar_pos_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_scalebar_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_map_title_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_map_classification_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure()) 
        #Add the scalebar postioning items to the combo box
        for item in mapuiSettings.getScalebarPositioning():
            self.combo_scalebar_position.addItem(item[0])            
            
        #Setup control signals
        self.chk_add_scalebar.stateChanged.connect(self.toggleScalebar)
        self.chk_scalebar_fill.stateChanged.connect(self.toggleScalebarFill)
        self.chk_scalebar_frame.stateChanged.connect(self.toggleScalebarFrame)
        self.combo_scalebar_position.currentIndexChanged.connect(self.comboPositionChanged)
      
    ###########################################################################################################################
    #This is the event handler to the page oriention icon label click event (map page tab)
    ###########################################################################################################################
    def lblOrientationClick(self, even):
        self.swapIcon()
        h = self.spin_page_height.value()
        self.spin_page_height.setValue(self.spin_page_width.value())
        self.spin_page_width.setValue(h)
        
    ###########################################################################################################################
    #These are the three event handlers for the symbology options mouse click
    ###########################################################################################################################
    def lbl0Click(self, event): 
        self.radio_symlevel0.setChecked(True)
        self.checkLevels()
    def lbl1Click(self, event): 
        self.radio_symlevel1.setChecked(True)
        self.checkLevels()
    def lbl2Click(self, event): 
        self.radio_symlevel2.setChecked(True)
        self.checkLevels()
  
    ###########################################################################################################################
    #Swaps the displayed icon when page orientation changes or when the icon label is pressed (map page tab)
    ########################################################################################################################### 
    def swapIcon(self):
        if self.spin_page_height.value() < self.spin_page_width.value():
            self.lbl_orientation.setPixmap(self.iconH)
        else:
            self.lbl_orientation.setPixmap(self.iconP)
            
    ###########################################################################################################################
    #This enables/disables certain controls based on whether map title is being added (map page tab)
    ###########################################################################################################################
    def toggleMapTitle(self):
        if self.chk_add_map_title.isChecked():
            self.txt_map_title.setEnabled(True)
            self.spin_map_title_offset_x.setEnabled(True)
            #self.spin_map_title_offset_y.setEnabled(True)
            self.combo_map_title_offset_unit.setEnabled(True)
            self.combo_map_title_font.setEnabled(True)
            self.spin_map_title_font_size.setEnabled(True)
            self.btn_map_title_font_color.setEnabled(True)
        else:
            self.txt_map_title.setEnabled(False)
            self.spin_map_title_offset_x.setEnabled(False)
            #self.spin_map_title_offset_y.setEnabled(False)
            self.combo_map_title_offset_unit.setEnabled(False)
            self.combo_map_title_font.setEnabled(False)
            self.spin_map_title_font_size.setEnabled(False)
            self.btn_map_title_font_color.setEnabled(False)
            
    ###########################################################################################################################
    #This enables/disables certain controls based on whether map classification is being added (map page tab)
    ###########################################################################################################################       
    def toggleClassification(self):
        if self.chk_add_map_classification.isChecked():
            self.txt_map_classification.setEnabled(True)
            self.spin_map_classsification_offset_x.setEnabled(True)
            self.spin_map_classsification_offset_y.setEnabled(True)
            self.combo_map_classification_offset_unit.setEnabled(True)
            self.combo_map_classification_font.setEnabled(True)
            self.spin_map_classification_font_size.setEnabled(True)
            self.btn_map_classification_font_color.setEnabled(True)
        else:
            self.txt_map_classification.setEnabled(False)
            self.spin_map_classsification_offset_x.setEnabled(False)
            self.spin_map_classsification_offset_y.setEnabled(False)
            self.combo_map_classification_offset_unit.setEnabled(False)
            self.combo_map_classification_font.setEnabled(False)
            self.spin_map_classification_font_size.setEnabled(False)
            self.btn_map_classification_font_color.setEnabled(False)            

    ###########################################################################################################################
    #This enables/disables certain controls based on whether grid ticks are being added (map frame tab)
    ###########################################################################################################################     
    def toggleGridTicks(self):
        if self.chk_grid_ticks.isChecked():
            self.spin_grid_tick_interval_x.setEnabled(True)
            self.spin_grid_tick_interval_y.setEnabled(True)
            self.spin_grid_tick_length.setEnabled(True)
            self.lcbtn_grid_ticks.setEnabled(True)
        else:
            self.spin_grid_tick_interval_x.setEnabled(False)
            self.spin_grid_tick_interval_y.setEnabled(False)
            self.spin_grid_tick_length.setEnabled(False)
            self.lcbtn_grid_ticks.setEnabled(False)
            
    def comboPositionChanged(self):
        if self.combo_scalebar_position.currentText() == 'User Defined':
            self.spin_scalebar_x.setEnabled(True)
            self.spin_scalebar_y.setEnabled(True)
            self.combo_scalebar_pos_unit.setEnabled(True)
            self.spin_scalebar_offset_x.setEnabled(False)
            self.spin_scalebar_offset_y.setEnabled(False)
            self.combo_scalebar_offset_unit.setEnabled(False)
        else:
            self.spin_scalebar_x.setEnabled(False)
            self.spin_scalebar_y.setEnabled(False)
            self.combo_scalebar_pos_unit.setEnabled(False)
            self.spin_scalebar_offset_x.setEnabled(True)
            self.spin_scalebar_offset_y.setEnabled(True)
            self.combo_scalebar_offset_unit.setEnabled(True)
            
    ###########################################################################################################################
    #This enables/disables certain controls based on which symbology level is chosen (symbology tab)
    ########################################################################################################################### 
    def checkLevels(self):
        if self.radio_symlevel0.isChecked():
            self.combo_symbols.setEnabled(True)
            self.combo_symbology_size_unit.setEnabled(True)
            self.cbtn_symbology_fill.setEnabled(False)
            self.spin_symbology_size.setEnabled(False) 

        elif self.radio_symlevel1.isChecked():
            self.combo_symbols.setEnabled(True)
            self.combo_symbology_size_unit.setEnabled(True)
            self.cbtn_symbology_fill.setEnabled(False)
            self.spin_symbology_size.setEnabled(True) 
        else:
            self.combo_symbols.setEnabled(True)
            self.combo_symbology_size_unit.setEnabled(True)
            self.cbtn_symbology_fill.setEnabled(True)
            self.spin_symbology_size.setEnabled(True) 

    ###########################################################################################################################
    #This will open a color chooser dialog and return the chosen color to the approprate sender 
    ########################################################################################################################### 
    def chooseFontColor(self):
        cChooser = qtw.QColorDialog(self)    
        cChooser.setCurrentColor(self.getMapTitleColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:  
            btn = self.sender()
            if str(btn.objectName()) == 'btn_map_title_font_color': 
                self.setMapTitleColor(cChooser.selectedColor())
            elif btn.objectName() == 'btn_map_classification_font_color':
                self.setMapClassificationColor(cChooser.selectedColor()) 
            elif btn.objectName() == "btn_frame_font_color":
                self.setMapFrameFontColor(cChooser.selectedColor())
                
    ###########################################################################################################################
    #This will open a color chooser dialog and return the chosen color to the approprate sender 
    ###########################################################################################################################   
    def chooseBoundaryColor(self):
        cChooser = qtw.QColorDialog(self)    
        cChooser.setCurrentColor(self.getMapTitleColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:  
            btn = self.sender()
            if str(btn.objectName()) == 'btn_coastline_boundary_color': 
                self.setCoastlineNationalBoundaryColor(cChooser.selectedColor()) 

    ###########################################################################################################################
    #This enables/disables certain controls based on whether a scalebar is being added (scalebar tab)
    ###########################################################################################################################
    def toggleScalebar(self):
        if self.chk_add_scalebar.isChecked():
            self.radio_horizontal.setEnabled(True)
            self.radio_vertical.setEnabled(True)
            self.spin_scalebar_height.setEnabled(True)
            self.spin_scalebar_width.setEnabled(True)
            self.combo_scalebar_size_unit.setEnabled(True)
        else:
            self.radio_horizontal.setEnabled(False)
            self.radio_vertical.setEnabled(False)
            self.spin_scalebar_height.setEnabled(False)
            self.spin_scalebar_width.setEnabled(False)
            self.combo_scalebar_size_unit.setEnabled(False)
            
    ###########################################################################################################################
    #This enables/disables certain controls based on whether a scalebar frame is being added (scalebar tab)
    ###########################################################################################################################    
    def toggleScalebarFrame(self):
        if self.chk_scalebar_frame.isChecked():
            self.lcbtn_scalebar_frame_border.setEnabled(True)
            self.cbtn_scalebar_frame_fill.setEnabled(True)
            self.chk_scalebar_fill.setEnabled(True)
            self.chk_rounded.setEnabled(True)
            self.spin_scalebar_padding.setEnabled(True)
            
        else:
            self.lcbtn_scalebar_frame_border.setEnabled(False)
            self.cbtn_scalebar_frame_fill.setEnabled(False)
            self.chk_scalebar_fill.setEnabled(False) 
            self.chk_rounded.setEnabled(False)
            self.spin_scalebar_padding.setEnabled(False)

    def toggleScalebarFill(self):
        if self.chk_scalebar_fill.isChecked():
             self.cbtn_scalebar_frame_fill.setEnabled(True)
        else:
            self.cbtn_scalebar_frame_fill.setEnabled(False)
                
    ###########################################################################################################################
    #A few helper functions for color controls. This will be re-written later.
    ########################################################################################################################### 
    #Color for the map title
    def setMapTitleColor(self, color):
        self.__MapTitleColor = color
        pal = self.btn_map_title_font_color.palette()
        pal.setColor(qtg.QPalette.Foreground, color)
        self.btn_map_title_font_color.setPalette(pal)

    def getMapTitleColor(self):
        return self.__MapTitleColor

    def setMapClassificationColor(self, color):
        self.__MapClassificationColor = color
        pal = self.btn_map_classification_font_color.palette()
        pal.setColor(qtg.QPalette.Foreground, color)
        self.btn_map_classification_font_color.setPalette(pal)

    def getMapClassificationColor(self):
        return self.__MapClassificationColor

    def setMapFrameFontColor(self, color):
        self.__MapFrameFontColor = color
        pal = self.btn_frame_font_color.palette()
        pal.setColor(qtg.QPalette.Foreground, color)
        self.btn_frame_font_color.setPalette(pal)
        
    def getMapFrameFontColor(self):
        return self.__MapFrameFontColor
    
    def setCoastlineNationalBoundaryColor(self, c):
        self.__CoastlineNationalBoundaryColor = c 
    def getCoastlineNationalBoundaryColor(self):
        return self.__CoastlineNationalBoundaryColor
    