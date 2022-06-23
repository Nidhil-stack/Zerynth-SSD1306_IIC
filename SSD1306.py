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

import i2c

class SSD1306(i2c.I2c):
    def __init__(self, addr=0x3c, drvname = I2C0, clock = 1000000):
        print("SSD1306 init")
        i2c.I2c.__init__(self, addr, drvname, clock)

        self.write(bytearray([0x00,SSD1306_DISPLAYOFF]))

        self.write(bytearray([0x00,SSD1306_SETDISPLAYCLOCKDIV]))
        self.write(bytearray([0x00,0x80]))

        self.write(bytearray([0x00,SSD1306_SETMULTIPLEX]))
        self.write(bytearray([0x00,0x3F]))

        self.write(bytearray([0x00,SSD1306_SETDISPLAYOFFSET]))
        self.write(bytearray([0x00,0x0]))

        self.write(bytearray([0x00,SSD1306_SETSTARTLINE]))

        self.write(bytearray([0x00,SSD1306_CHARGEPUMP]))
        self.write(bytearray([0x00,0x14]))

        self.write(bytearray([0x00,SSD1306_MEMORYMODE]))
        self.write(bytearray([0x00,0x00]))

        self.write(bytearray([0x00,SSD1306_SEGREMAP]))
        self.write(bytearray([0x00,SSD1306_COMSCANDEC]))

        self.write(bytearray([0x00,SSD1306_SETCOMPINS]))
        self.write(bytearray([0x00,0x12]))

        self.write(bytearray([0x00,SSD1306_SETCONTRAST]))
        self.write(bytearray([0x00,0xCF]))

        self.write(bytearray([0x00,SSD1306_SETPRECHARGE]))
        self.write(bytearray([0x00,0xF1]))

        self.write(bytearray([0x00,SSD1306_SETVCOMDETECT]))
        self.write(bytearray([0x00,0x40]))

        self.write(bytearray([0x00,SSD1306_DISPLAYALLON_RESUME]))

        self.write(bytearray([0x00,SSD1306_NORMALDISPLAY]))
        self.write(bytearray([0x00,0XC0]))  #REVERSE



        self.write(bytearray([0x00,SSD1306_DISPLAYON]))

        self.write(bytearray([0x00,SSD1306_COLUMNADDR]))
        self.write(bytearray([0x00,0]))
        self.write(bytearray([0x00,127]))

        self.write(bytearray([0x00,SSD1306_PAGEADDR]))
        self.write(bytearray([0x00,0]))
        self.write(bytearray([0x00,7]))


    def clear(self):
        string = bytearray(0x00 * 1024)
        self._pixelStream(string)

    def _pixelStream(self, data):
        for d in data:
            command = bytearray([0x40]) + bytearray(d)
            self._write(command)

    def _commandStream(self, data):
        #if data isn't a bytearray, make it one
        for d in data:
            command = bytearray([0x00]) + bytearray(d)
            self.write(command)

    # def printString(self, string):
    #     #if data isn't a bytearray, make it one
    #     string = bytearray(string)
    #     #set up the i2c transaction
    #     string_lenght = len(string)
    #     self.write(bytearray([0x80, string_lenght]))
    #     self.write(string)
