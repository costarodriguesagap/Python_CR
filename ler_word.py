import docx ## para usar o modulo docx, instalar python-docx 

if __name__ == "__main__":
    x = docx.Document('C:\Users\i051284\Documentação\UNION vs UNION ALL.docx')
    for para in x.paragraphs:
        print(para.text)
