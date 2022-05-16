from django.http import QueryDict
from xhtml2pdf import pisa
from django.template.loader import render_to_string
import io

# Simple Python API to generate PDF files from HTML
def render_pdf(filename, context):
    final = io.BytesIO()
    html = render_to_string(filename, context)
    pisa.CreatePDF(html, dest=final)
    val = final.getvalue()
    final.close()
    return val


def sanityData(data):
    if isinstance(data, QueryDict):
        data = data.dict()
    return data
