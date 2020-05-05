
class mapuiSettings():
    
    @staticmethod 
    def getGMTPath():
        return "/usr/share/gmt/"

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
    def getMapFrameTypes():
        frames = [
                "Fancy",
                "Inside",
                "Plain"
                ]
        return frames 
    
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


