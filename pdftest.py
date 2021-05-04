import PyPDF2

with open('super.pdf', 'rb') as input_file, open('wtr.pdf', 'rb') as watermark_file:
	input_pdf = PyPDF2.PdfFileReader(input_file)
	watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
	watermark_page = watermark_pdf.getPage(0)

	output_pdf = PyPDF2.PdfFileWriter()

	for page in range(input_pdf.getNumPages()):
		pdf_page = input_pdf.getPage(page)
		pdf_page.mergePage(watermark_page)
		output_pdf.addPage(pdf_page)

	with open('watermarkedtest.pdf', 'wb') as output_file:
		output_pdf.write(output_file)

