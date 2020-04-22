#!/bin/bash
gmt_path=/usr/share/gmt/
base_dir=./test_output/
base_name=myTest
out_file=myTest.ps
output_cpt=file.cpt

scl=0.750
rlen=22.5
cm=0.0
orien=h
lt=10
ln=20
projection=Q${cm}/21.6i
RLL=-179.99/179.9/-60.9/82.78
basename=Working-Test
input_file="/home/cheapstr/Development/python/mapui/Sample-Inputs/earthquakes-april20.txt"
cpt_file=seis.cpt

cpt_min_value=1.0
cpt_max_value=620.0
cpt_interval=10
cpt_opacity=100
scale_unit=mgals
page_height=12.5
page_width=24.0
page_size_unit=i

#Scale Bar Settings
scalebar_height=0.15
scalebar_width=6.0
scalebar_unit=i
scalebar_x_pos=3.5
scalebar_y_pos=0.6
scalebar_pos_unit=i
scalebar_label_x=
scalebar_label_y=
scalebar_interval=50
scalebar_positioning=BR
scalebar_offset_x=-3.5
scalebar_offset_y=0.6
scalebar_offset_unit=i
#Symbology Settings
symbol=c
symbol_size=4.0
symbol_size_unit=p
symbol_fill_color=0/0/0
symbol_border_color=0/0/0

### SET THE MEDIA (PAPER) SIZE
echo Setting Media Size...
gmt set PS_MEDIA ${page_height}${page_size_unit}x${page_width}${page_size_unit}

### CREATE A COLOR TABLE
gmt makecpt -C${gmt_path}/cpt/$cpt_file -A${cpt_opacity} -T${cpt_min_value}/${cpt_max_value}/${cpt_interval} -Z -V > ${output_cpt}

### CREATE A BASE LAYER FOR PROJECTED DATA
echo Creating Basemap...
gmt psbasemap -R${RLL} -J${projection} -B${ln}g${ln}/${lt}g${lt}:.$basename: -Xci -Yci -K > ${out_file}

### CREATE A COASTLINE
echo Creating Coastlines...
gmt pscoast -R${RLL} -J${projection} -W0.5p,lightgrey -N1/0.5p,lightgrey -K -O -V >> ${out_file}

### PLOT THE POINTS FROM THE INPUT FILE
echo Plotting input points...
gmt psxy ${input_file} -R${RLL} -J${projection} -C${output_cpt} -S${symbol}${symbol_size}${symbol_size_unit} -W.05,gray50 -O -K -V >> ${out_file}

### COLORIZE THE MAP
echo Coloring the map with the color palette...
gmt psscale -C${output_cpt} -X${scalebar_offset_x}${scalebar_offset_unit} -Y${scalebar_offset_y}${scalebar_offset_unit} -DJ${scalebar_positioning}+w${scalebar_width}${scalebar_unit}/${scalebar_height}${scalebar_unit}+jTC+h -Bx${scalebar_interval}${scale_units}  -R${RLL} -J${projection} -O -K -V >> ${out_file}