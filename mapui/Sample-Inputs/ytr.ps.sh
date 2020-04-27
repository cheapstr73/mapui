#!/bin/bash
##########################################################################################
#SET UP PATH REFERENCES
##########################################################################################
gmt_path=/usr/share/gmt/
base_dir="/mnt/566A02716A024E65/MAPUI-BACKUP/GitHub/mapui/Sample-Inputs/"
base_name="ytr"
input_file="/mnt/566A02716A024E65/MAPUI-BACKUP/GitHub/mapui/Sample-Inputs/capitals.txt"
out_file=ytr.ps
##########################################################################################
#DECLARE CLASSIFICATION INFO
##########################################################################################
classification=UNCLASSIFIED
classification_font=Helvetica-Bold
classification_font_size=14
classification_color=85/170/0
classification_offset_x=0.0
classification_offset_y=-0.3
classification_offset_unit=i
##########################################################################################
#DECLARE MAP TITLE INFO
##########################################################################################
map_title="Map Title"
##########################################################################################
#DECLARE COLOR PALETTE INFO
##########################################################################################
output_cpt=file.cpt
input_cpt=cyclic.cpt
cpt_min_value=1.0
cpt_max_value=245.0
cpt_interval=10
cpt_opacity=44
##########################################################################################
#DECLARE PAGE AND REGION OF INTEREST SETTINGS
##########################################################################################
page_height=11.0
page_width=24.0
page_size_unit=i
cm=4.0
lt=10
ln=20
projection=Q${cm}/21.6i
RLL=-170/179/-55/78
##########################################################################################
#DECLARE SCALEBAR SETTINGS
##########################################################################################
scale_unit=mgals
scalebar_height=0.12
scalebar_width=5.0
scalebar_width_unit=i
scalebar_x_pos=3.5
scalebar_y_pos=0.6
scalebar_pos_unit=i
scalebar_label_x=""
scalebar_label_y=
scalebar_interval=25
scalebar_positioning=BL
scalebar_offset_x=3.0
scalebar_offset_y=0.8
scalebar_offset_unit=i
##########################################################################################
#DECLARE MAP SYMBOLOGY SETTINGS
##########################################################################################
symbol=c
symbol_size=4.0
symbol_size_unit=c
symbol_fill_color=255/0/0
symbol_border_color=0/0/0
##########################################################################################
#END VARIABLE DECLARATIONS  | DO NOT ALTER CODE BEYOND THIS POINT
##########################################################################################


##########################################################################################
#SET THE GMT DEFAULTS
##########################################################################################
gmt set PS_MEDIA ${page_height}${page_size_unit}x${page_width}${page_size_unit}
gmt set MAP_FRAME_TYPE fancy
gmt set FONT_TITLE 24p,Helvetica-Bold,0/0/0

##########################################################################################
#STRETCH THE CPT
##########################################################################################
gmt makecpt -C${gmt_path}/cpt/$input_cpt -A${cpt_opacity} -T${cpt_min_value}/${cpt_max_value}/${cpt_interval} -Z -V > ${output_cpt}

##########################################################################################
#CREATE A BASE LAYER FOR PROJECTED DATA
##########################################################################################
echo Creating Basemap...
gmt psbasemap -R${RLL} -J${projection} -B${ln}g${ln}/${lt}g${lt}:."${map_title}": -Xci -Yci -K > ${out_file}

##########################################################################################
#CREATE COASTLINE LAYER
##########################################################################################
echo Creating Coastlines...
gmt pscoast -R${RLL} -J${projection} -W0.5p,lightgrey -N1/0.5p,lightgrey -K -O -V >> ${out_file}

##########################################################################################
#PLOT THE XY DATA FROM THE INPUT FILE
##########################################################################################
echo Plotting input points...
gmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size_unit}  -O -K -V >> ${out_file}

##########################################################################################
#ADD THE MAP CLASSSIFICATION AT THE TOP
##########################################################################################

echo 10.8 9.615759312320918 ${classification} | gmt pstext -R0/${page_width}/0/${page_height} -Jx1i -F+f${classification_font_size}p,${classification_font},${classification_color}+jTC -Xa${classification_offset_x}${classification_offset_unit} -Ya${classification_offset_y}${classification_offset_unit} -O -K -N >> ${out_file}

##########################################################################################
#ADD THE MAP SCALEBAR AND COLOR SCHEME
##########################################################################################
echo Coloring the map with the color palette...
gmt psscale -C${output_cpt} -Xa${scalebar_offset_x}${scalebar_offset_unit} -Ya${scalebar_offset_y}${scalebar_offset_unit} -DJ${scalebar_positioning}+w${scalebar_width}${scalebar_width_unit}/${scalebar_height}${scalebar_width_unit}+jTC+h -Bx${scalebar_interval}${scale_units}  -R${RLL} -J${projection}  -O -V >> ${out_file}

##########################################################################################
#CONVERT THE POSTSCRIPT TO THE SELECTED OUTPUT FORMATS
##########################################################################################

gmt psconvert ${out_file} -S -Tf