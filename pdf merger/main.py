from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n=int(input("Enter the number of pdfs to merge: "))
for i in range(0, n):
    name = input("Enter the name of the pdf file {i+1}: ")
    pdfs.append(name)
    

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()