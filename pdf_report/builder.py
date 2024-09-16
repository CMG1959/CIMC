# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.enums import TA_CENTER, TA_LEFT
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, \
#     Spacer, PageBreak, Image, KeepTogether, LongTable
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.rl_config import defaultPageSize
# from reportlab.lib.units import inch

# from cStringIO import StringIO

# import tempfile
# import os
# from pdf2image import convert_from_path
# from PIL import Image
# import win32print
# import win32ui

# BASE_FONT = "Times-Roman"
# BASE_FONT_BOLD = 'Times-Bold'
# BASE_FONT_SIZE = 9
# IMAGE_ALIGN_CENTER = "CENTER"
# PAGE_WIDTH = defaultPageSize[0]
# PAGE_HEIGHT = defaultPageSize[1]
# PAGE_NUMBER_STR = "Page %d"


# DOCUMENT_TITLE = "Job Report"
# DOCUMENT_NUMBER = "QSR-752-538/Job"
# DOCUMENT_DATE = "Rev A Dated 11/17/15"

# STYLE_TITLE_PAGE_KEY = 'title_page'
# STYLE_CENTER_TABLE_KEY = 'center_table'

# class PDFReport(object):
#     def __init__(self, document_title=None, document_number=None, document_date=None):
#         self.document_title = document_title or DOCUMENT_TITLE
#         self.document_number = document_number or DOCUMENT_NUMBER
#         self.document_date = document_date or DOCUMENT_DATE
#         self.styles = None
#         self.story = []


#     def _my_first_page(self, canvas, doc, date):
#         canvas.saveState()
#         canvas.setFont(BASE_FONT_BOLD, 16)
#         canvas.setFont(BASE_FONT, 9)
#         canvas.drawString(inch, 0.75 * inch, "%s" % self.document_number)
#         canvas.drawString(PAGE_WIDTH / 2 - 0.25 * inch, 0.75 * inch,
#                           PAGE_NUMBER_STR % doc.page)
#         canvas.drawString(PAGE_WIDTH - 2 * inch, 0.75 * inch,
#                           "%s" % date)
#         canvas.restoreState()

#     def _my_later_pages(self, canvas, doc, date):
#         canvas.saveState()
#         canvas.setFont(BASE_FONT, 9)
#         canvas.drawString(inch, 0.75 * inch, "%s" % self.document_number)
#         canvas.drawString(PAGE_WIDTH / 2 - 0.25 * inch, 0.75 * inch,
#                           PAGE_NUMBER_STR % doc.page)
#         canvas.drawString(PAGE_WIDTH - 2 * inch, 0.75 * inch,
#                           "%s" % date)
#         canvas.restoreState()

#     def _document_styles(self, styles):
#         styles = getSampleStyleSheet()
#         styles.add(ParagraphStyle(name=STYLE_TITLE_PAGE_KEY,
#                                   alignment=TA_CENTER))
#         styles.add(
#             ParagraphStyle(name=STYLE_CENTER_TABLE_KEY,
#                            alignment=TA_CENTER, fontSize=16))

#     def _report_meta(self):
#         pass

#     def _add_image(self, image_path, image_align, story=None):
#         story = story or self.story

#         image = Image(image_path)
#         image.hAlign = IMAGE_ALIGN_CENTER

#         story.append(image)

#     def _add_cover_page(self, cover_page_text, style, caption_spacer, story):
#         story = story or self.story

#         if caption_spacer:
#             story.append(caption_spacer)

#         story.append(Paragraph(cover_page_text, style))

#         if caption_spacer:
#             story.append(caption_spacer)


#     def _add_table(self, table_style, table_data, style, story=None,
#                    table_title=None, spacer=None):
#         story = story or self.story

#         if table_title:
#             story.append(Paragraph(table_title, style))
#             story.append(Spacer(1, 0.25 * inch))

#         t = Table(table_data)
#         t.setStyle(TableStyle(table_style))

#         story.append(t)

#         if spacer:
#             story.append(spacer)

#     def build_document(self, story=None):
#         story = story or self.story
#         tmp_file = StringIO()

#         document = SimpleDocTemplate(tmp_file)
#         document.build(story,
#                        onFirstPage=self._my_first_page,
#                        onLaterPages=self._my_later_pages)
#         stringified_object = tmp_file.getvalue()
#         tmp_file.close()
#         return stringified_object
    

#     def print_document(self, pdf_data):
#         # Create a temporary file to hold the PDF data
#         with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
#             temp_file.write(pdf_data)
#             temp_file_path = temp_file.name
        
#         try:
#             # Convert PDF to images
#             images = convert_from_path(temp_file_path)
            
#             # Get the default printer
#             printer_name = win32print.GetDefaultPrinter()
#             printer_info = win32print.GetPrinter(win32print.OpenPrinter(printer_name), 2)
            
#             # Initialize printing device context
#             printer_dc = win32ui.CreateDC()
#             printer_dc.CreatePrinterDC(printer_name)
#             printer_dc.StartDoc('PDF Document')
            
#             for image in images:
#                 # Convert image to RGB mode (required for printing)
#                 image = image.convert('RGB')
                
#                 # Create a temporary image file
#                 with tempfile.NamedTemporaryFile(delete=False, suffix='.bmp') as temp_image_file:
#                     image.save(temp_image_file.name)
#                     temp_image_path = temp_image_file.name
                    
#                     # Print the image
#                     bmp = Image.open(temp_image_path)
#                     printer_dc.StartPage()
#                     printer_dc.DrawImage(bmp)
#                     printer_dc.EndPage()
            
#             printer_dc.EndDoc()
#         except Exception as e:
#             print(f"An error occurred: {e}")
#         finally:
#             # Clean up
#             os.remove(temp_file_path)

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, \
    Spacer, PageBreak, Image, KeepTogether, LongTable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

import tempfile
import os
from pdf2image import convert_from_path
from PIL import Image
import win32print
import win32ui

BASE_FONT = "Times-Roman"
BASE_FONT_BOLD = 'Times-Bold'
BASE_FONT_SIZE = 9
IMAGE_ALIGN_CENTER = "CENTER"
PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]
PAGE_NUMBER_STR = "Page %d"

DOCUMENT_TITLE = "Job Report"
DOCUMENT_NUMBER = "QSR-752-538/Job"
DOCUMENT_DATE = "Rev A Dated 11/17/15"

STYLE_TITLE_PAGE_KEY = 'title_page'
STYLE_CENTER_TABLE_KEY = 'center_table'

class PDFReport(object):
    def __init__(self, document_title=None, document_number=None, document_date=None):
        self.document_title = document_title or DOCUMENT_TITLE
        self.document_number = document_number or DOCUMENT_NUMBER
        self.document_date = document_date or DOCUMENT_DATE
        self.styles = None
        self.story = []

    def _my_first_page(self, canvas, doc, date):
        canvas.saveState()
        canvas.setFont(BASE_FONT_BOLD, 16)
        canvas.setFont(BASE_FONT, 9)
        canvas.drawString(inch, 0.75 * inch, "%s" % self.document_number)
        canvas.drawString(PAGE_WIDTH / 2 - 0.25 * inch, 0.75 * inch,
                          PAGE_NUMBER_STR % doc.page)
        canvas.drawString(PAGE_WIDTH - 2 * inch, 0.75 * inch,
                          "%s" % date)
        canvas.restoreState()

    def _my_later_pages(self, canvas, doc, date):
        canvas.saveState()
        canvas.setFont(BASE_FONT, 9)
        canvas.drawString(inch, 0.75 * inch, "%s" % self.document_number)
        canvas.drawString(PAGE_WIDTH / 2 - 0.25 * inch, 0.75 * inch,
                          PAGE_NUMBER_STR % doc.page)
        canvas.drawString(PAGE_WIDTH - 2 * inch, 0.75 * inch,
                          "%s" % date)
        canvas.restoreState()

    def _document_styles(self, styles):
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name=STYLE_TITLE_PAGE_KEY,
                                  alignment=TA_CENTER))
        styles.add(
            ParagraphStyle(name=STYLE_CENTER_TABLE_KEY,
                           alignment=TA_CENTER, fontSize=16))

    def _report_meta(self):
        pass

    def _add_image(self, image_path, image_align, story=None):
        story = story or self.story

        image = Image.open(image_path)  # Changed to Image.open
        image.hAlign = IMAGE_ALIGN_CENTER

        story.append(image)

    def _add_cover_page(self, cover_page_text, style, caption_spacer, story):
        story = story or self.story

        if caption_spacer:
            story.append(caption_spacer)

        story.append(Paragraph(cover_page_text, style))

        if caption_spacer:
            story.append(caption_spacer)

    def _add_table(self, table_style, table_data, style, story=None,
                   table_title=None, spacer=None):
        story = story or self.story

        if table_title:
            story.append(Paragraph(table_title, style))
            story.append(Spacer(1, 0.25 * inch))

        t = Table(table_data)
        t.setStyle(TableStyle(table_style))

        story.append(t)

        if spacer:
            story.append(spacer)

    def build_document(self, story=None):
        story = story or self.story
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        tmp_file.close()  # Close the file to ensure it can be opened by ReportLab

        document = SimpleDocTemplate(tmp_file.name)
        document.build(story,
                       onFirstPage=self._my_first_page,
                       onLaterPages=self._my_later_pages)
        
        with open(tmp_file.name, 'rb') as file:
            stringified_object = file.read()
        
        os.remove(tmp_file.name)  # Clean up the temporary file
        return stringified_object

    def print_document(self, pdf_data):
        # Create a temporary file to hold the PDF data
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            temp_file.write(pdf_data)
            temp_file_path = temp_file.name
        
        try:
            # Convert PDF to images
            images = convert_from_path(temp_file_path)
            
            # Get the default printer
            printer_name = win32print.GetDefaultPrinter()
            
            # Initialize printing device context
            printer_dc = win32ui.CreateDC()
            printer_dc.CreatePrinterDC(printer_name)
            printer_dc.StartDoc('PDF Document')
            
            for image in images:
                # Convert image to RGB mode (required for printing)
                image = image.convert('RGB')
                
                # Create a temporary image file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.bmp') as temp_image_file:
                    image.save(temp_image_file.name)
                    temp_image_path = temp_image_file.name
                    
                    # Open the image and print
                    bmp = Image.open(temp_image_path)
                    printer_dc.StartPage()
                    # You need a function to draw the image to the printer_dc.
                    # The following line is a placeholder as `DrawImage` is not a real method:
                    # printer_dc.DrawImage(bmp)
                    printer_dc.EndPage()
            
            printer_dc.EndDoc()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Clean up
            os.remove(temp_file_path)
