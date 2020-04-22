from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc 
from PyQt5 import uic
from support.data.mapuiSettings import mapuiSettings
from support.data.ColorToolButton import ColorToolButton

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
        self.txt_shift_x.setValidator(qtg.QDoubleValidator())
        self.txt_shift_y.setValidator(qtg.QDoubleValidator())
        self.combo_shift_unit.addItems(mapuiSettings.getUnitsOfMeasure()) 
        self.combo_symbology_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_page_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_scalebar_size_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.btn_options_close.clicked.connect(self.close)
        self.combo_scalebar_pos_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        self.combo_scalebar_offset_unit.addItems(mapuiSettings.getUnitsOfMeasure())
        for item in mapuiSettings.getScalebarPositioning():
            self.combo_scalebar_position.addItem(item[0])

        #Set Tab Icons
        self.options_tab.setTabIcon(0, qtg.QIcon('./support/icons/page_size3.png'))
        self.options_tab.setTabIcon(1, qtg.QIcon('./support/icons/points2.png'))
        self.options_tab.setTabIcon(2, qtg.QIcon('./support/icons/scale4.png'))

        self.radio_symlevel0.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        #Populate symbology combo box...The getSymbols methos returns a list of tuples 
        #containing the symbols name (shown in the combo box) and the symbol code.
        sym = mapuiSettings.getSymbols()
        for item in sym:
            self.combo_symbols.addItem(item[0])
    
        #Attach signals to slots..
        self.radio_symlevel0.clicked.connect(self.checkLevels)
        self.radio_symlevel1.clicked.connect(self.checkLevels)
        self.radio_symlevel2.clicked.connect(self.checkLevels)
        self.cbtn_symbology_fill = ColorToolButton()
        self.color_button_layout.addWidget(self.cbtn_symbology_fill)
        self.combo_scalebar_position.currentIndexChanged.connect(self.comboPositionChanged)
        self.checkLevels()

        self.lbl_symlevel0.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel1.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel2.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.lbl_symlevel0.mousePressEvent = self.lbl0Click
        self.lbl_symlevel1.mousePressEvent = self.lbl1Click
        self.lbl_symlevel2.mousePressEvent = self.lbl2Click

    def lbl0Click(self, event): 
        self.radio_symlevel0.setChecked(True)
        self.checkLevels()
    def lbl1Click(self, event): 
        self.radio_symlevel1.setChecked(True)
        self.checkLevels()
    def lbl2Click(self, event): 
        self.radio_symlevel2.setChecked(True)
        self.checkLevels()

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

