#from support.data.gmtMap import gmtMap
from support.data.mapuiSettings import mapuiSettings
#from support.data.gmtFont import gmtFont
from PyQt5 import QtWidgets as qtw
#from PyQt5 import QtGui as qtg
###########################################################################################################################
#This class will take a gmtMap object and output a shell script to feed into GMT
###########################################################################################################################
class gmtMapScript():
    def __init__(self, gmtMap): 
        self.__gmtMap = gmtMap
        self.sclFactor = mapuiSettings.getWidthScalingFactor()
        self.gmtPath = mapuiSettings.getGMTPath() 
        self.output = gmtMap.FileOutput
        
        try:
            self.output_basename = gmtMap.FileOutput[gmtMap.FileOutput.rfind('/')+1:][:-3]
            self.output_directory = gmtMap.FileOutput[:gmtMap.FileOutput.rfind('/')+1:]
            self.output_ps = self.output_directory + '/' + self.output_basename + ".ps"
            f = open(self.output_directory + '/.' + self.output_basename + '.sh' , 'w')
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
    def getNationaBoundaryCode(self, c):
        for item in mapuiSettings.getBorderTypes():
            if c == item[0]:
                return item[1]
        return None

    def getRiverTypeCode(self, c):
        for item in mapuiSettings.getRiverTypes():
            if c == item[0]:
                return item[1]
        return None 

    def getScalebarPositioningCode(self, p):
        for item in mapuiSettings.getScalebarPositioning():
            if p == item[0]:
                return item[1]
        return None 
 
    def getClassificationPosition(self):
        x = float(self.__gmtMap.ROIWest) - float(self.__gmtMap.ROIEast)
        y = float(self.__gmtMap.ROINorth) - float(self.__gmtMap.ROISouth)
        w = x / self.__gmtMap.PageWidth 
        h = (y / self.__gmtMap.PageHeight * self.sclFactor)
        YAxis = (self.__gmtMap.PageHeight * (h/w)) 
        XAxis = (self.__gmtMap.PageWidth * self.sclFactor) / 2
        YAxis2 = (self.__gmtMap.PageHeight - YAxis) / 2
        return [XAxis, YAxis+YAxis2]

    def convertColor(self, color):
        #color = qtg.QColor(color)
        r = color.red()
        g = color.green()
        b = color.blue()
        return str(r) + '/' + str(g) + '/' + str(b)

    ###########################################################################################################################
    #The script is written from top to bottom one line at a time...
    ###########################################################################################################################
    def createScript(self):        
        try:
            with open(self.output_directory + '/.' + self.output_basename + '.sh', 'a') as script:
                script.write("#!/bin/bash")
                script.write('\n##########################################################################################')
                script.write('\n#SET UP PATH REFERENCES')
                script.write('\n##########################################################################################')
                script.write('\ngmt_path=%s' % self.gmtPath)
                script.write('\nbase_dir=\"%s\"' % self.output_directory)
                script.write('\nbase_name=\"%s\"' % self.output_basename)
                script.write('\ninput_file=\"%s\"' %self.__gmtMap.FileInput)
                script.write('\nout_file=%s' % self.output_basename + '.ps')
                if self.__gmtMap.MapClassificationAdd:
                    script.write('\n##########################################################################################')
                    script.write('\n#DECLARE CLASSIFICATION INFO')
                    script.write('\n##########################################################################################')
                    script.write('\nclassification=%s' % self.__gmtMap.MapClassification.text)
                    script.write('\nclassification_font=%s' % self.__gmtMap.MapClassification.font)
                    script.write('\nclassification_font_size=%s' % self.__gmtMap.MapClassification.size)
                    script.write('\nclassification_color=%s' % self.convertColor(self.__gmtMap.MapClassification.color))
                    script.write('\nclassification_offset_x=%s' % self.__gmtMap.MapClassificationOffsetX)
                    script.write('\nclassification_offset_y=%s' % self.__gmtMap.MapClassificationOffsetY)
                    script.write('\nclassification_offset_unit=%s' % self.__gmtMap.MapClassificationOffsetUnit[:1].lower())
                if self.__gmtMap.MapTitleAdd:
                    script.write('\n##########################################################################################')
                    script.write('\n#DECLARE MAP TITLE INFO')
                    script.write('\n##########################################################################################')                  
                    script.write('\nmap_title=\"%s\"' % self.__gmtMap.MapTitle.text)
                else:
                    script.write('\nmap_title=\'\'')

                script.write('\n##########################################################################################')
                script.write('\n#DECLARE COLOR PALETTE INFO')
                script.write('\n##########################################################################################')
                script.write('\noutput_cpt=file.cpt')
                script.write('\ninput_cpt=%s' % self.__gmtMap.CPTFile)
                script.write('\ncpt_min_value=%s' % self.__gmtMap.CPTMinValue)
                script.write('\ncpt_max_value=%s' % self.__gmtMap.CPTMaxValue)
                script.write('\ncpt_interval=%s' % self.__gmtMap.CPTInterval)
                #In order to get the transparency correct in GMT, subtract the sliders opacity value from 100
                script.write('\ncpt_opacity=%s' % str(100 - int(self.__gmtMap.Opacity )))

                script.write('\n##########################################################################################')
                script.write('\n#DECLARE PAGE AND REGION OF INTEREST SETTINGS')
                script.write('\n##########################################################################################')
                script.write('\npage_height=%s' % self.__gmtMap.PageHeight)
                script.write('\npage_width=%s' % self.__gmtMap.PageWidth)
                script.write('\npage_size_unit=%s' % self.__gmtMap.PageSizeUnit[:1].lower())
                script.write('\ncm=%s' % str(self.__gmtMap.getCentralMeridian())) 
                script.write('\nlt=%s' % str(self.__gmtMap.getLatitudeGS()))
                script.write('\nln=%s' % str(self.__gmtMap.getLongitudeGS()))
                #Set the projection
                projWidth = float(self.__gmtMap.PageWidth) * self.sclFactor
                script.write('\nprojection2=Q${cm}/%si' % projWidth)
                script.write('\nprojection=%s%s' % (str(self.__gmtMap.Projection.getProjectionCode()), self.__gmtMap.PageSizeUnit[:1].lower()))
                script.write('\nRLL=%s/%s/%s/%s' %(self.__gmtMap.ROIEast, self.__gmtMap.ROIWest, self.__gmtMap.ROISouth, self.__gmtMap.ROINorth))

                script.write('\n##########################################################################################')
                script.write('\n#DECLARE SCALEBAR SETTINGS')
                script.write('\n##########################################################################################')
                script.write('\nscale_unit=%s' % self.__gmtMap.ScaleUnit)
                script.write('\nscalebar_height=%s' % self.__gmtMap.ScalebarHeight)
                script.write('\nscalebar_width=%s' % self.__gmtMap.ScalebarWidth)
                script.write('\nscalebar_width_unit=%s' % self.__gmtMap.ScalebarSizeUnit[:1].lower())
                script.write('\nscalebar_x_pos=%s' % self.__gmtMap.ScalebarXPos)
                script.write('\nscalebar_y_pos=%s' % self.__gmtMap.ScalebarYPos)
                script.write('\nscalebar_pos_unit=%s' % self.__gmtMap.ScalebarPosUnit[:1].lower())
                script.write('\nscalebar_label_x=\"%s\"' % self.__gmtMap.ScalebarLabelX)
                script.write('\nscalebar_label_y=%s' % self.__gmtMap.ScalebarLabelY)
                script.write('\nscalebar_interval=%s' % self.__gmtMap.ScalebarInterval)
                script.write('\nscalebar_positioning=%s' % self.getScalebarPositioningCode(self.__gmtMap.ScalebarPositioning))             
                script.write('\nscalebar_offset_x=%s' % self.__gmtMap.ScalebarOffsetX)
                script.write('\nscalebar_offset_y=%s' % self.__gmtMap.ScalebarOffsetY)
                script.write('\nscalebar_offset_unit=%s' % self.__gmtMap.ScalebarOffsetUnit[:1].lower())
                
                script.write('\n##########################################################################################')
                script.write('\n#DECLARE MAP SYMBOLOGY SETTINGS')
                script.write('\n##########################################################################################')
                script.write('\nsymbol=%s' % self.getSymCode(self.__gmtMap.SymbologyShape))
                script.write('\nsymbol_size=%s' % self.__gmtMap.SymbologySize )
                script.write('\nsymbol_size_unit=%s' % self.__gmtMap.SymbologySizeUnit[:1].lower())
                script.write('\nsymbol_fill_color=%s' % self.convertColor(self.__gmtMap.SymbologyFillColor))
                script.write('\nsymbol_border_color=%s' % self.convertColor(self.__gmtMap.SymbologyBorderColor))
                script.write('\ncoastline_resolution=%s' % self.__gmtMap.CoastlineResolution[:1].lower())
                script.write('\ncoast_fill_color=%s' % self.convertColor(self.__gmtMap.CoastlineLandFillColor))
                script.write('\ncoast_water_color=%s' % self.convertColor(self.__gmtMap.CoastlineWaterFillColor))
                script.write('\ncoast_border_color=%s' % self.convertColor(self.__gmtMap.CoastlineBorderColor))
                script.write('\ncoast_border_weight=%s' % self.__gmtMap.CoastlineBorderWeight)
                script.write('\nnational_boundaries_color=%s' % self.convertColor(self.__gmtMap.CoastlineNationalBoundaryColor))
                script.write('\nnational_boundaries_type=%s' % self.getNationaBoundaryCode(self.__gmtMap.CoastlineNationalBoundaryType))
                script.write('\nnational_boundaries_weight=%s' % self.__gmtMap.CoastlineNationalBoundaryWeight)
                rivers = self.getRiverTypeCode(self.__gmtMap.CoastlineRiverType)
                if rivers != '-1':
                    script.write('\nriver_type=%s' % rivers)
                    script.write('\nriver_color=%s' % self.convertColor(self.__gmtMap.CoastlineRiverColor))
                    script.write('\nriver_weight=%s' % self.__gmtMap.CoastlineRiverWeight)

                script.write('\n##########################################################################################')
                script.write('\n#END VARIABLE DECLARATIONS  | DO NOT ALTER CODE BEYOND THIS POINT')
                script.write('\n##########################################################################################')

                script.write('\n\n\n##########################################################################################')
                script.write('\n#SET THE GMT DEFAULTS')
                script.write('\n##########################################################################################')
                script.write('\ngmt set PS_MEDIA ${page_height}${page_size_unit}x${page_width}${page_size_unit}')
                script.write('\ngmt set MAP_FRAME_TYPE fancy')
                #if user selects to add a title...
                if self.__gmtMap.MapTitleAdd:
                    script.write('\ngmt set FONT_TITLE %sp,%s,%s' % (self.__gmtMap.MapTitle.size, self.__gmtMap.MapTitle.font, self.convertColor(self.__gmtMap.MapTitle.color)))                    

                script.write('\n\n##########################################################################################')
                script.write('\n#STRETCH THE CPT')
                script.write('\n##########################################################################################')
                script.write('\ngmt makecpt -C${gmt_path}/cpt/$input_cpt -A${cpt_opacity} -T${cpt_min_value}/${cpt_max_value}/${cpt_interval} -Z -V > ${output_cpt}')

                script.write('\n\n##########################################################################################')
                script.write('\n#CREATE COASTLINE LAYER')
                script.write('\n##########################################################################################')
                script.write('\necho Creating Coastlines...')
                #Add rivers
                if rivers  != '-1':
                    script.write('\ngmt pscoast -R${RLL} -J${projection} -D${coastline_resolution} -W${coast_border_weight}p,${coast_border_color} -G${coast_fill_color} -S${coast_water_color} -N${national_boundaries_type}/${national_boundaries_weight}p,${national_boundaries_color} -I${river_type}/${river_weight}p,${river_color} -Xc -Yc  -K  -V > ${out_file}')
                #Don't add rivers
                else:
                    script.write('\ngmt pscoast -R${RLL} -J${projection} -D${coastline_resolution} -W${coast_border_weight}p,${coast_border_color} -G${coast_fill_color} -S${coast_water_color} -N${national_boundaries_type}/${national_boundaries_weight}p,${national_boundaries_color} -Xc -Yc -K -V > ${out_file}')
                
                script.write('\n\n##########################################################################################')
                script.write('\n#PLOT THE XY DATA FROM THE INPUT FILE')
                script.write('\n##########################################################################################')
                script.write('\necho Plotting input points...')
                #script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size} -W.05,gray50 -O -K -V >> ${out_file}')
                #Decide the symbology level...
                if self.__gmtMap.SymbologyLevel == 0:
                    script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size_unit}  -O -K -V >> ${out_file}')
                elif self.__gmtMap.SymbologyLevel == 1:
                    script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size}${symbol_size_unit} -W.05,gray50 -O -K -V >> ${out_file}')
                else:
                    script.write('\ngmt psxy ${input_file} -R${RLL} -J${projection}  -S${symbol}${symbol_size}${symbol_size_unit} -W.05,${symbol_border_color} -G${symbol_fill_color} -O -K -V >> ${out_file}')
                    
                script.write('\n\n##########################################################################################')
                script.write('\n#CREATE A BASE LAYER FOR PROJECTED DATA')
                script.write('\n##########################################################################################')
                script.write('\necho Creating Basemap...')
                script.write('\ngmt psbasemap -R${RLL} -J${projection} -B${ln}g${ln}/${lt}g${lt}:.\"${map_title}\": -Xc -Yc -K -O -V >> ${out_file}')

                #Place the classification if needed....
                if self.__gmtMap.MapClassificationAdd:
                    script.write('\n\n##########################################################################################')
                    script.write('\n#ADD THE MAP CLASSSIFICATION AT THE TOP')
                    script.write('\n##########################################################################################')
                    pos = self.getClassificationPosition()
                    script.write('\necho '+ str(pos[0]) + ' ' + str(pos[1]) + ' ${classification} | gmt pstext -R0/${page_width}/0/${page_height} -Jx1i -F+f${classification_font_size}p,${classification_font},${classification_color}+jTC -Xa${classification_offset_x}${classification_offset_unit} -Ya${classification_offset_y}${classification_offset_unit} -O -K -N >> ${out_file}' )

                script.write('\n\n##########################################################################################')
                script.write('\n#ADD THE MAP SCALEBAR AND COLOR SCHEME')
                script.write('\n##########################################################################################')
                script.write('\necho Coloring the map with the color palette...')
                script.write('\ngmt psscale -C${output_cpt} ')   
                #For User Defined scale positioning, add the -Dx option
                if self.getScalebarPositioningCode(self.__gmtMap.ScalebarPositioning) == "UD":
                    script.write('-Dx${scalebar_x_pos}${scalebar_pos_unit}/${scalebar_y_pos}${scalebar_pos_unit}+w${scalebar_width}${scalebar_width_unit}/${scalebar_height}${scalebar_width_unit}+jTC')
                else: #For static positioning, add -DJ
                    script.write('-Xa${scalebar_offset_x}${scalebar_offset_unit} -Ya${scalebar_offset_y}${scalebar_offset_unit} -DJ${scalebar_positioning}+w${scalebar_width}${scalebar_width_unit}/${scalebar_height}${scalebar_width_unit}+jTC')

                if self.__gmtMap.ScalebarOrientation == 'h':
                    script.write('+h')
                if self.__gmtMap.ScalebarLabelX:
                    script.write(' -Bx${scalebar_interval}${scale_units}+l\"' + self.__gmtMap.ScalebarLabelX + '\"')
                if self.__gmtMap.ScalebarLabelY:
                    script.write(' -By+l\"' + self.__gmtMap.ScalebarLabelY +'\" ')

                if not self.__gmtMap.ScalebarLabelX and not self.__gmtMap.ScalebarLabelY:
                    script.write(' -Bx${scalebar_interval}${scale_units} ')
                if self.__gmtMap.ScalebarIlluminate:
                    script.write(' -I ')
                script.write(' -R${RLL} -J${projection}  -O -V >> ${out_file}')
                

                script.write('\n\n##########################################################################################')
                script.write('\n#CONVERT THE POSTSCRIPT TO THE SELECTED OUTPUT FORMATS')
                script.write('\n##########################################################################################')
                if self.__gmtMap.ConvertTypes:
                    script.write('\n\ngmt psconvert ${out_file} -T' + str(self.__gmtMap.ConvertTypes))
                     

        except Exception as e:
            m = qtw.QMessageBox()
            m.setText("Script Error\n" + str(e))
            m.exec()