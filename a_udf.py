# import libs
import os
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# create a function to convert .pdf -> .txt

def pdf_to_txt(file_path):
    # open pdf in read-binary mode
    with open(file_path, 'rb') as file: # opens the file in read mode rb 
        # create pdf resource manager object
        rsrcmgr = PDFResourceManager()

         # set the StringIO object as the file for the TextConverter
        # this allows the converter to write the text to a string buffer
        text_io = StringIO()
        converter = TextConverter(rsrcmgr, text_io, laparams=LAParams())

        # create a PDF interpreter object
        interpreter = PDFPageInterpreter(rsrcmgr, converter)

        # process each page in the PDF
        for page in PDFPage.get_pages(file):
            interpreter.process_page(page)

        # get the text from the StringIO object and close the file
        text = text_io.getvalue()
        file.close()

        # close the text buffer and the converter
        text_io.close()
        converter.close()

        # return the text
        return text