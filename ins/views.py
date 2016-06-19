import re

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.
from startupshot.models import MattecProd
from part.models import Part
from molds.models import Mold
from .models import *
from .forms import *
import datetime

@login_required
def view_index(request):
    activeInMattec = MattecProd.objects.order_by('machNo').all()

    template = loader.get_template('ins/index.html')
    context = RequestContext(request, {
        'active_parts': activeInMattec,
    })
    return HttpResponse(template.render(context))


def view_job(request):
    job_number = request.GET.get('job_number', '-1')

    context = {}

    job_in_mattec = MattecProd.objects.get(jobNumber=job_number)
    part_info = Part.objects.get(item_Number=job_in_mattec.itemNo)
    mold_info = Mold.objects.get(mold_number=job_in_mattec.moldNumber)

    mach_type = get_machine_type(job_in_mattec.machNo)

    inspection_set = ['A']
    if mach_type in ['IMM', 'ISBM']:
        if StaticInspectionPart.objects.filter(part_number=part_info.item_Number,
                                               inspection_group__product_type='M').exists() or \
                StaticInspectionGroup.objects.filter(product_type='M', apply_type='All').exists():
                inspection_set.append('M')
    elif mach_type not in ['Fail', 'M']:
        inspection_set.append(mach_type)
    else:
        pass

    existing_inspections = Inspection.objects.filter(job_number=job_number, inspection_result=-1)
    inspections = StaticInspectionGroup.objects.filter(product_type__in=inspection_set)

    template = loader.get_template('ins/view.html')
    context = RequestContext(request, {
        'job_number': job_number,
        'part_info': part_info,
        'mold_info': mold_info,
        'inspections': inspections,
        'existing_inspections': existing_inspections
        # 'pf_inspectionType': pf_inspectionType,
        # 'range_inspectionType': range_inspectionType,
        # 'text_inspectionType': text_inspectionType,
        # 'int_inspectionType': int_inspectionType,
        # 'float_inspectionType': float_inspectionType
    })
    return HttpResponse(template.render(context))

def view_record_inspection(request):
    job_number = request.GET.get('job_number', '-1')
    inspection_group_id = request.GET.get('inspection_group_id', '-1')
    new = request.GET.get('new','0')
    uut_id = request.GET.get('uut_id','-1')

    job_in_mattec = MattecProd.objects.get(jobNumber=job_number)
    part_info = Part.objects.get(item_Number=job_in_mattec.itemNo)
    mold_info = Mold.objects.get(mold_number=job_in_mattec.moldNumber)


    if request.method == 'POST':
        pass
    else:

        if new == '1':
            new_uut = Inspection(inspection_group_id=inspection_group_id,
                                 job_number=job_number,
                                 production_date=datetime.date.today(),
                                 start_date_time=datetime.datetime.now(),
                                 part_number=part_info.item_Number,
                                 mold_number=mold_info.mold_number,
                                 sta_reported=job_in_mattec.machNo,
                                 shift = '1',
                                 inspection_result=-1,
                                 location='Somerville')
            new_uut.save()
            uut_id = new_uut.uut_id


        inspection_regime = StaticInspectionGroup.objects.get(id=inspection_group_id)

        template = loader.get_template('ins/record_inspection.html')
        context = RequestContext(request, {
            'job_number': job_number,
            'part_info': part_info,
            'mold_info': mold_info,
            'uut_id': uut_id,
            'inspection_regime': inspection_regime
        })
        return HttpResponse(template.render(context))

def view_record_step(request):
    job_number = request.GET.get('job_number', '-1')
    inspection_id = request.GET.get('inspection_id', '-1')
    uut_id = request.GET.get('uut_id','-1')

    uut = Inspection.objects.get(uut_id=uut_id)
    job_in_mattec = MattecProd.objects.get(jobNumber=uut.job_number)
    part_info = Part.objects.get(item_Number=job_in_mattec.itemNo)
    mold_info = Mold.objects.get(mold_number=job_in_mattec.moldNumber)


    if request.method == 'POST':
        pass
    else:

        inspection_step = StaticInspection.objects.get(id=inspection_id)

        if inspection_step.inspection_type == 'Numeric Limit':
            form = FormPropNumericlimit()
        else:
            form = None


        template = loader.get_template('ins/record_step.html')
        context = RequestContext(request, {
            'job_number': job_number,
            'part_info': part_info,
            'mold_info': mold_info,
            'uut_id': uut_id,
            'form': form
            # 'inspection_regime': inspection_regime
        })
        return HttpResponse(template.render(context))


def get_machine_type(machine_alias):
    match = re.search('(?P<machine_type>\D+)(?P<machine_num>\d+)', machine_alias)
    try:
        return match.group('machine_type')
    except Exception as e:
        return 'Fail'
