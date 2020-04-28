from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 
from PyQt5 import uic
from support.data.mapuiSettings import mapuiSettings
from support.widgets.ColorToolButton import ColorToolButton
from support.widgets.LineColorButton import LineColorButton

###########################################################################################################################
#This class loads the options.ui file and creates the options window
###########################################################################################################################
class mapUIOptions(qtw.QDialog):
    def __init__(self, *args, **kwargs):
        super(mapUIOptions, self).__init__(*args, **kwargs) 
        uic.loadUi('./support/interfaces/options.ui', self)
        self.setupInterface()  

    def setupInterface(self):
        self.setWindowIcon(qtg.QIcon('./support/icons/options10.png'))
        self.btn_options_close.setIcon(qtg.QIcon('./support/icons/close5.png'))

        self.btn_options_close.clicked.connect(self.close)

        #Set Tab Icons
        self.options_tab.setTabIcon(0, qtg.QIcon('./support/icons/map9.png'))
        self.options_tab.setTabIcon(1, qtg.QIcon('./support/icons/points2.png'))
        self.options_tab.setTabIcon(2, qtg.QIcon('./support/icons/scale4.png'))
        self.btn_map_title_font_color.setIcon(qtg.QIcon('./support/icons/color2.png'))
        self.btn_map_classification_font_color.setIcon(qtg.QIcon('./support/icons/color2.png'))
        self.iconH = qtg.QPixmap('./support/icons/orientationH2.png')
        self.iconP = qtg.QPixmap('./support/icons/orientationP2.png')
        self.colorPaletteIcon = qtg.QIcon('./support/icons/color2.png')
        
        #Populate the combo boxes... 
        self.combo_symbology_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_page_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_scalebar_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_scalebar_pos_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_scalebar_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_map_title_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_map_classification_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure()) 

        #Add the coastline border types 
        for item in mapuiSettings.getBorderTypes():
            self.combo_coastline_national_boundary_type.addItem(item[0])

        for item in mapuiSettings.getRiverTypes():
            self.combo_coastline_river_type.addItem(item[0])

        #Add the scalebar postioning items...
        for item in mapuiSettings.getScalebarPositioning():
            self.combo_scalebar_position.addItem(item[0])   

        #Populate symbology combo box...The getSymbols methos returns a list of tuples 
        #containing the symbols name (shown in the combo box) and the symbol code.
        sym = mapuiSettings.getSymbols()
        for item in sym:
            self.combo_symbols.addItem(item[0])

        #Populate the map title fonts combo box
        fonts = mapuiSettings.getGMTFonts()
        for font in fonts:
            self.combo_map_title_font.addItem(font[0])
            self.combo_map_classification_font.addItem(font[0])

        self.radio_symlevel0.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))

        #Attach signals to slots..
        self.radio_symlevel0.clicked.connect(self.checkLevels)
        self.radio_symlevel1.clicked.connect(self.checkLevels)
        self.radio_symlevel2.clicked.connect(self.checkLevels)
        self.spin_page_height.valueChanged.connect(self.swapIcon)
        self.spin_page_width.valueChanged.connect(self.swapIcon)
        self.chk_add_map_title.stateChanged.connect(self.toggleMapTitle)
        self.chk_add_map_classification.stateChanged.connect(self.toggleClassification) 
        self.swapIcon()

        self.cbtn_symbology_fill = ColorToolButton()
        self.color_button_layout.addWidget(self.cbtn_symbology_fill)
        self.cbtn_coastlines_fill = ColorToolButton()
        self.coastline_color_layout.addWidget(self.cbtn_coastlines_fill)
        self.btn_map_title_font_color.clicked.connect(self.chooseFontColor)
        self.btn_map_classification_font_color.clicked.connect(self.chooseFontColor)

        #Coastline National Boundary data 
        self.lcbtn_national_boundary = LineColorButton()
        self.coastline_national_boundary_layout.addWidget(self.lcbtn_national_boundary)
        
        #Coastline River Data...
        self.lcbtn_rivers = LineColorButton() 
        self.coastline_river_color_layout.addWidget(self.lcbtn_rivers)

        self.combo_scalebar_position.currentIndexChanged.connect(self.comboPositionChanged)
        self.checkLevels()
        self.toggleMapTitle()
        self.toggleClassification()

        self.lbl_symlevel0.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel1.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel2.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_orientation.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel0.mousePressEvent = self.lbl0Click
        self.lbl_symlevel1.mousePressEvent = self.lbl1Click
        self.lbl_symlevel2.mousePressEvent = self.lbl2Click
        self.lbl_orientation.mousePressEvent = self.lblOrientationClick

    def lbl0Click(self, event): 
        self.radio_symlevel0.setChecked(True)
        self.checkLevels()
    def lbl1Click(self, event): 
        self.radio_symlevel1.setChecked(True)
        self.checkLevels()
    def lbl2Click(self, event): 
        self.radio_symlevel2.setChecked(True)
        self.checkLevels()
    def lblOrientationClick(self, even):
        self.swapIcon()
        h = self.spin_page_height.value()
        self.spin_page_height.setValue(self.spin_page_width.value())
        self.spin_page_width.setValue(h)

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

    def swapIcon(self):
        if self.spin_page_height.value() < self.spin_page_width.value():
            self.lbl_orientation.setPixmap(self.iconH)
        else:
            self.lbl_orientation.setPixmap(self.iconP)

    def chooseFontColor(self):
        cChooser = qtw.QColorDialog(self)    
        cChooser.setCurrentColor(self.getMapTitleColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:  
            btn = self.sender()
            if str(btn.objectName()) == 'btn_map_title_font_color': 
                self.setMapTitleColor(cChooser.selectedColor())
            elif btn.objectName() == 'btn_map_classification_font_color':
                self.setMapClassificationColor(cChooser.selectedColor()) 
    
    def chooseBoundaryColor(self):
        cChooser = qtw.QColorDialog(self)    
        cChooser.setCurrentColor(self.getMapTitleColor())
        if cChooser.exec() == qtw.QColorDialog.Accepted:  
            btn = self.sender()
            if str(btn.objectName()) == 'btn_coastline_boundary_color': 
                self.setCoastlineNationalBoundaryColor(cChooser.selectedColor()) 

    def toggleMapTitle(self):
        if self.chk_add_map_title.isChecked():
            self.txt_map_title.setEnabled(True)
            self.spin_map_title_offset_x.setEnabled(True)
            self.spin_map_title_offset_y.setEnabled(True)
            self.combo_map_title_offset_unit.setEnabled(True)
            self.combo_map_title_font.setEnabled(True)
            self.spin_map_title_font_size.setEnabled(True)
            self.btn_map_title_font_color.setEnabled(True)
        else:
            self.txt_map_title.setEnabled(False)
            self.spin_map_title_offset_x.setEnabled(False)
            self.spin_map_title_offset_y.setEnabled(False)
            self.combo_map_title_offset_unit.setEnabled(False)
            self.combo_map_title_font.setEnabled(False)
            self.spin_map_title_font_size.setEnabled(False)
            self.btn_map_title_font_color.setEnabled(False)

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

    def setCoastlineNationalBoundaryColor(self, c):
        self.__CoastlineNationalBoundaryColor = c 
    def getCoastlineNationalBoundaryColor(self):
        return self.__CoastlineNationalBoundaryColor
    