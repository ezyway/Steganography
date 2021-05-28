"""

Py Program for the Steganography Implimentation (naive Approach)

"""
import os
from PIL import Image
import msvcrt as m


class Steganography:
    def __init__(self, fileName = "sample.jpeg"):
        
        os.system('cls')

        self.fileName = fileName
        
        # If No File name is given, then take sample.jpg
        if self.fileName == "sample.jpeg":
            print("Sample file is being used. File Name: \"sample.jpeg\"")
        
        # Makes absolute URL for the file
        self.fileLoc = os.path.dirname(__file__) + "\\" + self.fileName

        try:
            # Opens and displays stats for the img
            self.img = Image.open(self.fileLoc)
            print("Image was opened successfully...\n")
            print(":-: Image Stats :-:\n")

            print("Size: {:.2f}".format( os.stat(self.fileLoc).st_size / (1024*1024) ) + "MBs")
            print("Format: " + self.img.format)

            print("Resolution: " + str(self.img.size[0]) + " x " + str(self.img.size[1]))

            print("\n\nPress any key to continue:\n")
            # m.getch()

        except:
            print("The file cannot be opened\n")
            exit()

    # End of __init__() -----------------------------------------------------------------------------------

    def encode(self, msg = "Sample Message"):
        # Converts pixels in RGB VALS || use self.imgRGB.getpixel((x,y))
        # self.imgRGB = self.img.convert("RGB")


        msg = list(msg)
        # print(msg)

        # Converts the message to ASCII and stores in msgAscii list
        msgAscii = [ord(i) for i in msg]
        msgBi = list()


        # Converts the ASCII to Binary and appends to msgBi list
        for i in range(len(msgAscii)):
            binaryVal = bin(msgAscii[i]).replace("0b","")       # Gets Binary of the numbers
            if len(binaryVal) < 8:
                binaryVal = "0"*(8 - len(binaryVal)) + binaryVal
            msgBi.append(binaryVal)


        # Divides the binary into 2 parts and stores in msgBiDiv list
        msgBiDiv = list()
        for i in range(len(msgBi)):
            msgBiDiv.append(msgBi[i][:4])
            msgBiDiv.append(msgBi[i][4:])


        print(msgBi)
        print(msgBiDiv)


        # Put the vals in the img
        for i in range(len(msgBiDiv)):

            # 2 Lines: Replaces the Blue value in binary
            rgb = list(self.img.getpixel((i,0)))
            rgb = [ rgb[0], rgb[1], bin(rgb[2]).replace("0b","") ]

            # Merges the first 4 bits from the original and bits from the list msgBiDiv
            newVal = int(rgb[2][:4] + msgBiDiv[i], 2)

            # Goes into the Picture
            self.img.putpixel((i, 0), (rgb[0], rgb[1], newVal))
            
            # For Indication
            self.img.putpixel((i, 11), (0,0,0))

        self.img.show()
        self.img.save(os.path.dirname(__file__)+"\\"+"file.jpg")
        

        # self.img.putpixel((10,10),(0,0,0))
        # self.img.show()




s = Steganography("file.jpg")
s.encode("abcdefghijklmnopqrstuvwxyz")
s.decode()