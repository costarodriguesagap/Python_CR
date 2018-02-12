# importing all the required modules
import PyPDF2

# creating an object 
pdf_r = 'teste.pdf'

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file(pdf_r,'rb'))
n_pages = fileReader.getNumPages()
print("Numero de Paginas - " +str(n_pages))

pg = 0
while pg < n_pages:
    pg_data = fileReader.getPage(pg)
    dados = pg_data.extractText()
    print(dados)
    pg += 1


##for pg in n_pages:
##    pg_data = fileReader.getPage(pg)
##    print(pg_data.extractText())
