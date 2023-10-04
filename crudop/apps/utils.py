from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from random import randint
import os

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    #pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def render_to_file(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    file_name = "{0}.pdf".format(randint(1, 1000000))
    file_path = os.path.join(os.path.abspath(os.path.dirname("__file__")),"media/temp", file_name)
    with open(file_path, 'wb') as pdf:
        pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
    return file_name
