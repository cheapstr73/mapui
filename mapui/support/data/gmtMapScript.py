from support.data.gmtMap import gmtMap
from support.data.mapuiSettings import mapuiSettings
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
###########################################################################################################################
#This class will take a gmtMap object and output a shell script to feed into GMT
###########################################################################################################################
class gmtMapScript():
    def __init__(self, gmtMap, output_dir): 
        self.__gmtMap = gmtMap
        self.gmtPath = mapuiSettings.getGMTPath() 
        self.output = output_dir
        try:
            self.output_basename = output_dir[output_dir.rfind('/')+1:]
            self.output_directory = output_dir[:output_dir.rfind('/')+1:]
            self.output_ps = output_dir + '.ps'
            f = open("./test_output/myTest.sh", 'w')
            f.close()
        except Exception as e:
            q = qtw.QMessageBox()
            q.setText(str(e))
            q.exec()
        self.createScript()

    def getSymCode(self, sym):
        for item in mapuiSettings.getSymbols():
            if sym == item[0]:
                return item[1]
        return None

    def getScalebarPositioningCode(self, p):
        for item in mapuiSettings.getScalebarPositioning():
            if p == item[0]:
                return item[1]
        return None 
           
    def convertColor(self, color):
        #color = qtg.QColor(color)
        r = color.red()
        g = color.green()
        b = color.blue()
        return str(r) + '/' + str(g) + '/' + str(b)

    def createScript(self):
        try:
            with open(self.output + ".sh", 'a') as script:
                script.write("#!/bin/bash")
                script.write('\ngmt_path=%s' % self.gmtPath)
                script.write('\nbase_dir=%s' % self.output_directory)
                script.write('\nbase_name=%s' % self.output_basename)
                script.write('\nout_file=%s' % self.output_basename + '.ps')
                script.write('\noutput_cpt=file.cpt')
                #############THIS LINE (x7) WILL NEED EDITING LATER!!#################
                script.write('\n\nscl=0.750')
                script.write('\nrlen=22.5')
                script.write('\ncm=%s' % str(self.__gmtMap.getCM()))
                script.write('\norien=h')
                script.write('\nlt=%s' % str(self.__gmtMap.getLatitudeGS()))
                script.write('\nln=%s' % str(self.__gmtMap.getLongitudeGS()))
                #script.write('\nprojection=Q${cm}/${rlen}i') #Old version...
                #Get the page width
                w = float(self.__gmtMap.PageWidth) * .9
                script.write('\nprojection=Q${cm}/%si' % w)
                script.write('\nRLL=%s/%s/%s/%s' %(self.__gmtMap.ROIEast, self.__gmtMap.ROIWest, self.__gmtMap.ROISouth, self.__gmtMap.ROINorth))
                script.write('\nbasename=Working-Test')
                script.write('\ninput_file=\"%s\"' %self.__gmtMap.FileInput)
                script.write('\ncpt_file=%s' % self.__gmtMap.CPTFile)
                script.write('\n\ncpt_min_value=%s' % self.__gmtMap.CPTMinValue)
                script.write('\ncpt_max_value=%s' % self.__gmtMap.CPTMaxValue)
                script.write('\ncpt_interval=%s' % self.__gmtMap.CPTInterval)
                script.write('\ncpt_opacity=%s' % self.__gmtMap.Opacity)
                script.write('\nscale_unit=%s' % self.__gmtMap.ScaleUnit)    
                script.write('\npage_height=%s' % self.__gmtMap.PageHeight)
                script.write('\npage_width=%s' % self.__gmtMap.PageWidth)
                script.write('\npage_size_unit=%s' % self.__gmtMap.PageSizeUnit[:1].lower())
                script.write('\n\n#Scale Bar Settings')
                script.write('\nscalebar_height=%s' % self.__gmtMap.ScalebarHeight)
                script.write('\nscalebar_width=%s' % self.__gmtMap.ScalebarWidth)
                script.write('\nscalebar_unit=%s' % self.__gmtMap.ScalebarSizeUnit[:1].lower())
                script.write('\nscalebar_x_pos=%s' % self.__gmtMap.ScalebarXPos)
                script.write('\nscalebar_y_pos=%s' % self.__gmtMap.ScalebarYPos)
                script.write('\nscalebar_pos_unit=%s' % self.__gmtMap.ScalebarPosUnit[:1].lower())
                script.write('\nscalebar_label_x=%s' % self.__gmtMap.ScalebarLabelX)
                script.write('\nscalebar_label_y=%s' % self.__gmtMap.ScalebarLabelY)
                script.write('\nscalebar_interval=%s' % self.__gmtMap.ScalebarInterval)
                script.write('\nscalebar_positioning=%s' % self.getScalebarPositioningCode(self.__gmtMap.ScalebarPositioning))
                script.write('\nscalebar_offset_x=%s' % self.__gmtMap.ScalebarOffsetX)
                script.write('\nscalebar_offset_y=%s' % self.__gmtMap.ScalebarOffsetY)
                script.write('\nscalebar_offset_unit=%s' % self.__gmtMap.ScalebarOffsetUnit[:1].lower())
                script.write('\n#Symbology Settings')
                script.write('\nsymbol=%s' % self.getSymCode(self.__gmtMap.SymbologyShape))
                script.write('\nsymbol_size=%s' % self.__gmtMap.SymbologySize )
                script.write('\nsymbol_size_unit=%s' % self.__gmtMap.SymbologySizeUnit[:1].lower())
                script.write('\nsymbol_fill_color=%s' % self.convertColor(self.__gmtMap.SymbologyFillColor))
                script.write('\nsymbol_border_color=%s' % self.convertColor(self.__gmtMap.SymbologyBorderColor))

                #############THIS LINE WILL NEED EDITING LATER!!#################
                script.write('\n\n### SET THE MEDIA (PAPER) SIZE')
                script.write('\necho Setting Media Size...')
                script.write('\ngmt set PS_MEDIA ${page_height}${page_size_unit}x${page_width}${page_size_unit}')

                script.write('\n\n### CREATE A COLOR TABLE')
                script.write('\ngmt makecpt -C${gmt_path}/cpt/$cpt_file -A${cpt_opacity} -T${cpt_min_value}/${cpt_max_value}/${cpt_interval} -Z -V > ${output_cpt}')

                script.write('\n\n### CREATE A BASE LAYER FOR PROJECTED DATA')
                script.write('\necho Creating Basemap...')
                script.write('\ngmt psbasemap -R${RLL} -J${projection} -B${ln}g${ln}/${lt}g${lt}:.$basename: -Xci -Yci -K > ${out_file}')

                script.write('\n\n### CREATE A COASTLINE')
                script.write('\necho Creating Coastlines...')
                script.write('\ngmt pscoast -R${RLL} -J${projection} -W0.5p,lightgrey -N1/0.5p,lightgrey -K -O -V >> ${out_file}')

                script.write('\n\n### PLOT THE POINTS FROM THE INPUT FILE')
                script.write('\necho Plotting input points...')
                #script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size} -W.05,gray50 -O -K -V >> ${out_file}')
                #Decide the symbology level...
                if self.__gmtMap.SymbologyLevel == 0:
                    script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size_unit}  -O -K -V >> ${out_file}')
                elif self.__gmtMap.SymbologyLevel == 1:
                    script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size}${symbol_size_unit} -W.05,gray50 -O -K -V >> ${out_file}')
                else:
                    script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection}  -S${symbol}${symbol_size}${symbol_size_unit} -W.05,${symbol_border_color} -G${symbol_fill_color} -O -K -V >> ${out_file}')

                script.write('\n\n### COLORIZE THE MAP')
                script.write('\necho Coloring the map with the color palette...')
                #script.write('\ngmt psscale -C${output_cpt} -Dx13.0/6.0/10.0/.4 -B10${scale_units} -O -K -V >> out_file')
                script.write('\ngmt psscale -C${output_cpt} ')

                #For User Defined scale positioning, add the -Dx option
                if self.getScalebarPositioningCode(self.__gmtMap.ScalebarPositioning) == "UD":
                    script.write('-Dx${scalebar_x_pos}${scalebar_pos_unit}/${scalebar_y_pos}${scalebar_pos_unit}+w${scalebar_width}${scalebar_unit}/${scalebar_height}${scalebar_unit}+jTC')
                else: #For static positioning, add -DJ
                    script.write('-X${scalebar_offset_x}${scalebar_offset_unit} -Y${scalebar_offset_y}${scalebar_offset_unit} -DJ${scalebar_positioning}+w${scalebar_width}${scalebar_unit}/${scalebar_height}${scalebar_unit}+jTC')

                if self.__gmtMap.ScalebarOrientation == 'h':
                    script.write('+h')
                if self.__gmtMap.ScalebarLabelX:
                    script.write(' -Bx${scalebar_interval}${scale_units}+l\"' + self.__gmtMap.ScalebarLabelX + '\"')
                if self.__gmtMap.ScalebarLabelY:
                    script.write(' -By+l\"' + self.__gmtMap.ScalebarLabelY +'\" ')

                if not self.__gmtMap.ScalebarLabelX and not self.__gmtMap.ScalebarLabelY:
                    script.write(' -Bx${scalebar_interval}${scale_units} ')
                script.write(' -R${RLL} -J${projection} -O -K -V >> ${out_file}')
                

        except Exception as e:
            m = qtw.QMessageBox()
            m.setText("Script Error\n" + str(e))
            m.exec()