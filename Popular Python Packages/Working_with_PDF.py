import PyPDF2

# with open(r"E:\ayush\my_resume3.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)  # gets the number of pages in pdf
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(180)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("rotated2.pdf", "wb") as file2:
#         writer.write(file2)

merge = PyPDF2.PdfFileMerger()
lst = ["rotated.pdf", "rotated2.pdf"]
for name in lst:
    merge.append(name)

merge.write("combined.pdf")
