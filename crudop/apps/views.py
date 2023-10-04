
from django.shortcuts import render
from apps.models import * 
from django.http import  JsonResponse,HttpResponse,HttpResponsePermanentRedirect
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from random import randint
import os


@csrf_exempt

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    #pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, encoding="ISO-8859-1")
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# Create your views here.
def show(request):
    obj =passmodel.objects.all().values()
    context={'obj':obj}
    return render(request,'index.html',context)

def ajax_posting(request):
    if request.method=='GET':
        print('adfkhvbgakdj')
        aadhar=request.GET.get('aadhar')
        pname=request.GET.get('pname')
        email=request.GET.get('email')
        gender=request.GET.get('gender')
        contact=request.GET.get('contact')
        pin=request.GET.get('pin')
        dob=request.GET.get('dob')
        print(dob)
        print(gender)

        if passmodel.objects.filter(aadhar=aadhar).exists():
            passmodel.objects.filter(aadhar=aadhar).update(pname=pname,email=email,gender=gender,contact=contact,pin=pin,dob=dob)
        else :
            passmodel.objects.create( aadhar=aadhar,pname=pname,email=email,gender=gender,contact=contact,pin=pin,dob=dob)

        # Pass_model.objects.create(Passenger_name=pname,Email=email,Contact_No=contact,Flight=flight,Age=Age)
        return JsonResponse({'Success':'Form Updated successfully'},safe='False')
        
    else:
        # return JsonResponse({'error':'404 File not found '})
        return render(request,'index.html')
def get_data(request):
    obj =passmodel.objects.all().values()
    # print("obj",obj)
    # import json
    # data = json.dumps(list(obj))
    data = {'obj':list(obj)}
    print("data",data)
    return JsonResponse(data, safe=False)



def deleteview(request):
    if request.method == "GET":
        aadhar=request.GET.get('aadhar')
        print(aadhar)
        save = passmodel.objects.get(aadhar=aadhar)
        save.delete()
        return JsonResponse({'status': 200})  

def editview(request):
    if request.method == "GET":
        aadhar = request.GET.get('aadhar')
        obj = list(passmodel.objects.filter(aadhar=aadhar).values())
       
        return JsonResponse({'obj':obj}, safe=False)

def renderpdf(request):
    data=list(passmodel.objects.all().values())
    context={
           "data":data,
       }
    pdf = render_to_pdf('renderpdf.html',context)
    return HttpResponse(pdf,content_type='application/pdf')

import fiscalyear
import xlwt


def Karan_Excel_Report(request):
    # fiscalyear.START_MONTH = 4
    # fsy=str(fiscalyear.FiscalYear.current())
    # fsy=int(fsy[2:6])
    # fsy=str(fsy-1)+'-'+str(fsy)
    # date=datetime.now() 
    # date=date.strftime('%d-%m-%Y')
    # # records = list(block_division_Alco_16cyl_trx.objects.values().distinct())
    records = passmodel.objects.all().distinct()

    import xlwt
    #print(alldata)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Sample_Excel_Report.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Machines Capacity',cell_overwrite_ok=True)
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    font_style.font.name = "Arial"
    font_style.font.underline = True
    font_style.font.height = 220
    font_style.font.alignment ="Center"
    font_style.alignment = alignment
    font_style.alignment.wrap = True
    font_style1 = xlwt.XFStyle()
    font_style1.font.bold = True
    font_style1.font.name = "Calibri"
    font_style1.font.height = 220
    font_style1.alignment = alignment
    font_style1.alignment.wrap = False
    blue_style = xlwt.easyxf('pattern: pattern solid, fore_color blue;')
    styleg = xlwt.easyxf( 'font: colour green, bold True;')
    styley = xlwt.easyxf( 'font: colour blue, bold True;')
    styler = xlwt.easyxf( 'font: colour red, bold True;')
    
    ws.write_merge(0, 0, 0, 11, 'Excel Report ',font_style1)
    ws.write_merge(1, 1,0, 11, 'Flight Reservation System',font_style1)
    # ws.write_merge(2, 2, 0, 11, 'AS PER JPO YEAR - '+fsy, font_style1)
    # ws.write_merge(4, 4, 0, 11, 'AS ON DATE: '+date)
    row_num = 5
    # columns = ['ID','SNO','ENGINE_TYPE','ENGINE_NAME','ENGINE_URL']
    # for col_num in range(len(columns)):
    #     ws.write(row_num, col_num, columns[col_num],styleg)
    row_num = 5
    columns = [field.name for field in passmodel._meta.fields]
    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)
    
    for record in records:
        row_num += 1
        row = [getattr(record, field) for field in columns]
        for col_num, cell_value in enumerate(row):
             ws.write(row_num, col_num, cell_value)
    wb.save(response)
    return response 
         