# pdf_merging.py

from PyPDF2 import PdfFileReader, PdfFileWriter

if __name__ == '__main__':
    paths = ['document1.pdf', 'document2.pdf']
    while True:
        operation = input('Which operation would you like to perform? Type "m" to merge or "s" to split')
        if operation not in ['m','s']:
            print('You entered an invalid symbol.\n')
            continue
        elif operation == 'm':
            merge_pdfs(paths, output='merged.pdf')
        elif operation =='s':
            split(path, name_of_split)

    path = 'Jupyter_Notebook_An_Introduction.pdf'
    split(path, 'jupyter_page')


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)



def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
