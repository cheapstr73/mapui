
class mapuiSettings():
    
    @staticmethod 
    def getGMTPath():
        return "/usr/share/gmt/"

    @staticmethod 
    def getWidthScalingFactor():
        return .9
    
    @staticmethod
    def getVerbosity():
        levels = [
            "Debug Messages",
            "Detailed",
            "None",
            "Normal", 
            "Progress Messages", 
            "Warnings"            
        ]
        return levels

    @staticmethod 
    def getCPTUnits():
        units = [
            'mgals'
        ]
        return units 

    @staticmethod 
    def getUnitsOfMeasure():
        units = [
            'Centimeters',
            'Inches',
            'Points'
        ]   
        return units

    @staticmethod 
    def getBorderTypes():
        borders = [
            ['National Boundaries', '1'],
            ['State Boundaries (Americas)', '2'],
            ['Marine Boundaries', '3'],
            ['All Boundaries', 'a']
        ]
        return borders

    @staticmethod 
    def getRiverTypes():
        rivers = [
            ["None", '-1'],
            ["Double-Lined Rivers (River-Lakes)", "0"],
            ["Permanent Major Rivers", "1"],
            ["Additional Major Rivers", "2"],
            ["Additional Rivers", "3"],
            ["Minor Rivers", "4"],
            ["Intermittent Rivers - Major", "5"],
            ["Intermittent Rivers - Additional", "6"],
            ["Intermittent Rivers - Minor", "7"],
            ["Major Canals", "8"],
            ["Minor Canals", "9"],
            ["Irrigation Canals", "10"],
            ["All Rivers And Canals", "a "],
            ["All Rivers And Canals Except River-Lakes", "A "],
            ["All Permanent Rivers", "r "],
            ["All Permanent Rivers Except River-Lakes", "R "],
            ["All Intermittent Rivers", "i "],
            ["All Canals", "c "]
        ]
        return rivers

    @staticmethod 
    def getScalebarPositioning():
        pos = [
            ["Top Left", "TL"],
            ["Top Center", "TC"],
            ["Top Right", "TR"],
            ["Middle Left", "ML"],
            ["Middle Center", "MC"],
            ["Middle Right", "MR"],
            ["Bottom Left","BL"],
            ["Bottom Center", "BC"],
            ["Bottom Right", "BR"],
            ["User Defined", "UD"]
        ]
        return pos
    
    @staticmethod 
    def getResolutions():
        res = [
                "Full",
                "High",
                "Intermediate",
                "Low",
                "Crude"
            ]
        return res 
    
    @staticmethod 
    def getGMTFonts():
        fonts = [
            ["Helvetica", "0"],
            ["Helvetica-Bold", "1"],
            ["Helvetica-Oblique", "2"],
            ["Helvetica-BoldOblique", "3"],
            ["Times-Roman", "4"],
            ["Times-Bold", "5"],
            ["Times-Italic", "6"],
            ["Times-BoldItalic", "7"],
            ["Courier", "8"],
            ["Courier-Bold", "9"],
            ["Courier-Oblique", "10"],
            ["Courier-BoldOblique", "11"],
            ["Σψμβολ (Symbol)", "12"],
            ["AvantGarde-Book", "13"],
            ["AvantGarde-BookOblique", "14"],
            ["AvantGarde-Demi", "15"],
            ["AvantGarde-DemiOblique", "16"],
            ["Bookman-Demi", "17"],
            ["Bookman-DemiItalic", "18"],
            ["Bookman-Light", "19"],
            ["Bookman-LightItalic", "20"],
            ["Helvetica-Narrow", "21"],
            ["Helvetica-Narrow-Bold", "22"],
            ["Helvetica-Narrow-Oblique", "23"],
            ["Helvetica-Narrow-BoldOblique", "24"],
            ["NewCenturySchlbk-Roman", "25"],
            ["NewCenturySchlbk-Italic", "26"],
            ["NewCenturySchlbk-Bold", "27"],
            ["NewCenturySchlbk-BoldItalic", "28"],
            ["Palatino-Roman", "29"],
            ["Palatino-Italic", "30"],
            ["Palatino-Bold", "31"],
            ["Palatino-BoldItalic", "32"],
            ["ZapfChancery-MediumItalic", "33"],
            ["ZapfDingbats", "34"]
        ]
        return fonts
        
    @staticmethod
    def getSymbols():
        symbols = [
            ['Circle', 'c'],
            ['Cross (X)', 'x'],
            ['Diamond', 'd'],
            ['Hexagon', 'h'],
            ['Inverted Triangle', 'i'],
            ['Octagon', 'g'],
            ['Pentagon', 'n'],
            ['Point', 'p'],
            ['Square', 's'],
            ['Star', 'a'],
            ['Triangle', 't']
        ]   
        return symbols

    @staticmethod
    def getSymbols2():
        symbols = [
            'Circle', 
            'Cross (X)',
            'Diamond',
            'Hexagon',
            'Inverted Triangle',
            'Octagon',
            'Pentagon',
            'Point',
            'Square',
            'Star',
            'Triangle'
        ]   
        return symbols

    @staticmethod
    def getColorPalettes():
        cpt = [
            "abyss.cpt",
            "acton.cpt",
            "bamako.cpt",
            "bathy.cpt",
            "batlow.cpt",
            "berlin.cpt",
            "bilbao.cpt",
            "broc.cpt",
            "buda.cpt",
            "categorical.cpt",
            "cool.cpt",
            "copper.cpt",
            "cork.cpt",
            "cubhelix.cpt",
            "cyclic.cpt",
            "davos.cpt",
            "dem1.cpt",
            "dem2.cpt",
            "dem3.cpt",
            "dem4.cpt",
            "devon.cpt",
            "drywet.cpt",
            "earth.cpt",
            "elevation.cpt",
            "etopo1.cpt",
            "gebco.cpt",
            "geo.cpt",
            "globe.cpt",
            "grayC.cpt",
            "gray.cpt",
            "hawaii.cpt",
            "haxby.cpt",
            "hot.cpt",
            "ibcso.cpt",
            "imola.cpt",
            "inferno.cpt",
            "jet.cpt",
            "lajolla.cpt",
            "lapaz.cpt",
            "lisbon.cpt",
            "mag.cpt",
            "magma.cpt",
            "nighttime.cpt",
            "no_green.cpt",
            "nuuk.cpt",
            "ocean.cpt",
            "oleron.cpt",
            "oslo.cpt",
            "paired.cpt",
            "panoply.cpt",
            "plasma.cpt",
            "polar.cpt",
            "rainbow.cpt",
            "red2green.cpt",
            "relief.cpt",
            "roma.cpt",
            "seafloor.cpt",
            "sealand.cpt",
            "seis.cpt",
            "split.cpt",
            "srtm.cpt",
            "terra.cpt",
            "tofino.cpt",
            "tokyo.cpt",
            "topo.cpt",
            "turbo.cpt",
            "turku.cpt",
            "vik.cpt",
            "viridis.cpt",
            "world.cpt",
            "wysiwyg.cpt"

        ]        
        return cpt

    @staticmethod 
    def getProjections():
        prj = [
            "[GRP]Azimuthal Projections",
            "Azimuthal Equidistant",
            "Gnomonic",
            "Lambert Azimuthal Equal-Area",
            "Orthographic",
            "Stereographic Equal-Angle",
            "[GRP]Conic Projections",
            "Albers Conic Equal-Area",
            "Equidistant Conic",
            "Lambert Conic Conformal",
            "[GRP]Cylindrical Projections",
            "Cassini Cylindrical",
            "Cylindrical Equidistant",
            "General Cylindricals",
            "Mercator",
            "Miller Cylindricals",
            "Oblique Mercator",
            "Transverse Mercator",
            "Universal Transverse Mercator UTM",
            "[GRP]Miscellaneous Projections",
            "Eckert IV and VI",
            "Hammer",
            "Mollweide",
            "Robinson",
            "Sinusoidal",
            "Van der Grinten"
        ]
        return prj