"This program converts a Jupyter Notebook file (.ipynb) to a PDF format"

# libraries
import os
import sys
import nbformat
from nbconvert import PDFExporter

def convert_ipynb_to_pdf(ipynb_filename):
    # load the notebook file
    with open(ipynb_filename) as f:
        nb = nbformat.read(f, as_version=4) # version 4 is the jupyter notebook version. most widely used since 2015

    # Configure the PDFExporter
    pdf_exporter = PDFExporter()
    pdf_exporter.exclude_input = True
    pdf_exporter.exclude_output_prompt = True
    pdf_exporter.exclude_output_stderr = True

    # Export to PDF
    (output, resources) = PDFExporter.from_notebook_node(nb)

    # Determine the output filename
    basename = os.path.splitext(ipynb_filename)[0]
    pdf_filename = basename + ".pdf"

    # Write the PDF to disk
    with open(pdf_filename, "wb") as f:
        f.write(output)

    print("Converted {} to {}".format(ipynb_filename, pdf_filename))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ipynb_to_pdf.py [filename.ipynb]")
        sys.exit(1)

    ipynb_filename = sys.argv[1]
    convert_ipynb_to_pdf(ipynb_filename)