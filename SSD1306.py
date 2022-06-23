SSD1306_LCDWIDTH                    = 128
SSD1306_LCDHEIGHT                   = 64
SSD1306_SETCONTRAST                 = 0x81
SSD1306_DISPLAYALLON_RESUME         = 0xA4
SSD1306_DISPLAYALLON                = 0xA5
SSD1306_NORMALDISPLAY               = 0xA6
SSD1306_INVERTDISPLAY               = 0xA7
SSD1306_DISPLAYOFF                  = 0xAE
SSD1306_DISPLAYON                   = 0xAF
SSD1306_SETDISPLAYOFFSET            = 0xD3
SSD1306_SETCOMPINS                  = 0xDA
SSD1306_SETVCOMDETECT               = 0xDB
SSD1306_SETDISPLAYCLOCKDIV          = 0xD5
SSD1306_SETPRECHARGE                = 0xD9
SSD1306_SETMULTIPLEX                = 0xA8
SSD1306_SETLOWCOLUMN                = 0x00
SSD1306_SETHIGHCOLUMN               = 0x10
SSD1306_SETSTARTLINE                = 0x40
SSD1306_MEMORYMODE                  = 0x20
SSD1306_COLUMNADDR                  = 0x21
SSD1306_PAGEADDR                    = 0x22
SSD1306_COMSCANINC                  = 0xC0
SSD1306_COMSCANDEC                  = 0xC8
SSD1306_SEGREMAP                    = 0xA0
SSD1306_CHARGEPUMP                  = 0x8D
SSD1306_EXTERNALVCC                 = 0x1
SSD1306_SWITCHCAPVCC                = 0x2

cont=0
spaziodisponibile=128

CHARACTERS={
    #-> LETTERS
    'A':[0X7E,0X09,0X09,0X7E,0X00],
    'B':[0X7F,0X49,0X49,0X36,0X00],
    'C':[0X3E,0X41,0X41,0X22,0X00],
    'D':[0X7F,0X41,0X41,0X3E,0X00],
    'E':[0X7F,0X49,0X49,0X41,0X00],
    'F':[0X7F,0X09,0X09,0X01,0X00],
    'G':[0X3E,0X41,0X51,0X32,0X00],
    'H':[0X7F,0X08,0X08,0X7F,0X00],
    'I':[0X41,0X7F,0X41,0X00],
    'J':[0X30,0X40,0X40,0X3F,0X00],
    'K':[0X7F,0X08,0X14,0X63,0X00],
    'L':[0X7F,0X40,0X40,0X40,0X00],
    'M':[0X7F,0X02,0X04,0X02,0X7F,0X00],
    'N':[0X7F,0X04,0X08,0X7F,0X00],
    'O':[0X3E,0X41,0X41,0X3E,0X00],
    'P':[0X7F,0X09,0X09,0X06,0X00],
    'Q':[0X3E,0X41,0X21,0X5E,0X00],
    'R':[0X7F,0X09,0X09,0X76,0X00],
    'S':[0X26,0X49,0X49,0X32,0X00],
    'T':[0X01,0X01,0X7F,0X01,0X01,0X00],
    'U':[0X3F,0X40,0X40,0X3F,0X00],
    'V':[0X1F,0X20,0X40,0X20,0X1F,0X00],
    'W':[0X7F,0X20,0X18,0X20,0X7F,0X00],
    'X':[0X77,0X08,0X08,0X77,0X00],
    'Y':[0X2F,0X48,0X48,0X3F,0X00],
    'Z':[0X71,0X49,0X49,0X47,0X00],
    #-> NUMBERS
    '1':[0x42,0x7F,0x40,0x00],
    '2':[0x62,0x51,0x49,0x46,0x00],
    '3':[0x22,0x49,0x49,0x36,0x00],
    '4':[0x0C,0x0A,0x09,0x7F,0x00],
    '5':[0x47,0x45,0x45,0x39,0x00],
    '6':[0x3C,0x4A,0x49,0x30,0x00],
    '7':[0x01,0x71,0x09,0x07,0x00],
    '8':[0x36,0x49,0x49,0x36,0x00],
    '9':[0x06,0x49,0x29,0x1E,0x00],
    '0':[0x3E,0x51,0x49,0x3E,0x00],
    #-> PUNCTUATION
    '.':[0x40,0x00],
    ',':[0x60,0x00],
    ';':[0x64,0x00],
    ':':[0x44,0x00],
    '*':[0x05,0x02,0x05,0x00],
    '+':[0x08,0x08,0x3E,0x08,0x08,0x00],
    '-':[0x08,0x08,0x08,0x08,0x08,0x00],
    '?':[0x02,0x51,0x09,0x06,0x00],
    '!':[0x5F,0x00],
    '&':[0x54,0x23,0x55,0x29,0x36,0x00],
    '(':[0X1C,0x22,0x41,0x00],
    ')':[0x41,0x22,0x1C,0X00],
    '[':[0X7F,0x41,0x41,0x00],
    ']':[0x41,0x41,0x7F,0X00],
    '{':[0X08,0x77,0x41,0x41,0x00],
    '}':[0x41,0x41,0x77,0x08,0X00],
    ' ':[0X00,0x00],
    '=':[0X14,0X14,0X14,0X00],
    '>':[0x41,0x22,0x14,0x08,0x00],
    '<':[0x08,0x14,0x22,0x41,0x00],
    '^':[0x04,0x02,0x09,0x25,0x95,0x25,0x09,0x02,0x04,0x00], #wifi acceso
    '@':[0x00,0x00,0x00,0x00,0xBF,0x00,0x00,0x00,0x00,0x00]  #wifi spento
}

import i2c

class SSD1306(i2c.I2c):
    def __init__(self, addr=0x3c, drvname = I2C0, clock = 1000000):
        print("SSD1306 init")
        i2c.I2c.__init__(self, addr, drvname, clock)
        self.init()
        self.clear()



    def init(self):
        init_sequence = [
            SSD1306_DISPLAYOFF,
            SSD1306_SETDISPLAYCLOCKDIV, 0x80,
            SSD1306_SETMULTIPLEX, 0x3F,
            SSD1306_SETDISPLAYOFFSET, 0x00,
            SSD1306_SETSTARTLINE,
            SSD1306_CHARGEPUMP, 0x14,
            SSD1306_MEMORYMODE, 0x00,
            SSD1306_SEGREMAP,
            SSD1306_COMSCANINC,
            SSD1306_SETCOMPINS, 0x12,
            SSD1306_SETCONTRAST, 0xCF,
            SSD1306_SETPRECHARGE, 0xF1,
            SSD1306_SETVCOMDETECT, 0x40,
            SSD1306_DISPLAYALLON_RESUME,
            SSD1306_INVERTDISPLAY,
            SSD1306_DISPLAYON,
            SSD1306_COLUMNADDR, 0x00, 0x7F,
            SSD1306_PAGEADDR, 0x00, 0x07
        ]
        self._commandStream(init_sequence)

    def clear(self):
        data = bytearray()
        for i in range(0, 1024):
            data.append(0x00)
        self._pixelStream(data)

    def printString(self, string):
        data = bytearray()
        string = string.upper()
        for char in string:
            print(char)
            self._printChar(char)


    def _printChar(self, char):
        c = CHARACTERS.get(char, None)
        data = bytearray(c)
        self._pixelStream(data)

    def _pixelStream(self, data):
        for d in data:
            self.write(bytearray([0x40, d]))

    def _commandStream(self, data):
        for d in data:
            self.write(bytearray([0x00, d]))
