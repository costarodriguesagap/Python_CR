from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import StringIO

page = 0
pagina = 1

fileName = "Colocar Path"
try:
        if fileName.lower()[-3:] == "pdf": 
            input1 = PdfFileReader(file(fileName, "rb"))

        while page < input1.getNumPages:
            content = input1.getPage(page).extractText()
            print(content + "\n")
            print(str(pagina))
            page += 1
            pagina += 1

except:
        print ",",

