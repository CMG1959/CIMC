# Create your views here.
import datetime
import numpy as np


from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from django.db.models import Avg, Max, Min, StdDev
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from models import passFailByPart, passFailTest, passFailInspection, \
    partWeightInspection, visualInspection, shotWeightInspection, outsideDiameterInspection, \
    volumeInspection, \
    neckDiameterInspection, assemblyInspection, cartonTemperature, visionInspection
from part.models import PartInspection, Part
from startupshot.models import startUpShot, MattecProd
from employee.models import Employees
from molds.models import Mold,PartIdentifier
from production_and_mold_history.models import ProductionHistory
from forms import passFailInspectionForm, partWeightForm, jobReportSearch, itemReportSearch, shotWeightForm, \



######################################
#
#  Section for generating indexes, etc
#
######################################

@login_required
def view_index(request):
    activeInMattec = MattecProd.objects.order_by('machNo').all()


    template = loader.get_template('inspection/index.html')
    context = RequestContext(request, {
        'active_parts': activeInMattec,
    })
    return HttpResponse(template.render(context))


@login_required
def view_detailJob(request, jobNumber):
    jobNumber = str(jobNumber).strip()
    active_job = startUpShot.objects.filter(jobNumber=jobNumber).select_related('item')
    if not active_job.exists():
        redir_url = '/startupshot/create/%s/' % jobNumber
        return HttpResponseRedirect(redir_url)

    # if  PartInspection object hasnt be created, make it now.
    checkPartInspection(active_job[0].item)
    # better go ahead and take care of the Mold now
    checkMoldCavs(item_Number=active_job[0].item)

    pf_inspectionType = passFailByPart.objects.filter(item_Number__item_Number=active_job[0].item)


    template = loader.get_template('inspection/detailJob.html')
    context = RequestContext(request, {
        'active_job': active_job,
        'inspectionTypes': inspectionTypes,
        'pf_inspectionType' : pf_inspectionType,
    })
    return HttpResponse(template.render(context))


######################################
#
#  Section for generating forms
#
######################################


@login_required
def view_pfInspection(request, jobNumber, inspectionName):
    active_job = startUpShot.objects.filter(jobNumber=jobNumber).select_related('item')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = passFailInspectionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # part_number = form.cleaned_data['jobID']
            redirect_url = '/inspection/%s/' % (jobNumber)
            # save the data
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = passFailInspectionForm(
            initial={'jobID': startUpShot.objects.get(jobNumber=jobNumber).id,
                     'passFailTestName':passFailTest.objects.get(testName=inspectionName).id}
        )
        form = presetStandardFields(form, jobID=jobNumber)

        form.fields["headCavID"].queryset = PartIdentifier.objects.filter(
            mold_number__mold_number=active_job[0].moldNumber)

        template = loader.get_template('inspection/forms/genInspection.html')
        context = RequestContext(request, {
            'form_title' : 'Visual Inspection Form',
            'form': form,
            'active_job': active_job,
            'use_checkbox' : True,
            'id_check':'#id_inspectionResult',
            'idSelect':'#id_defectType',
            'idSelect2':'#id_headCavID'
        })
        return HttpResponse(template.render(context))

@login_required
def view_partWeightInspection(request, jobNumber):
    active_job = startUpShot.objects.filter(jobNumber=jobNumber).select_related('item')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = partWeightForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # part_number = form.cleaned_data['jobID']
            redirect_url = '/inspection/%s/' % (jobNumber)
            # save the data
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = partWeightForm(
            initial={'jobID': startUpShot.objects.get(jobNumber=jobNumber).id},
        )
        form = presetStandardFields(form, jobID=jobNumber)

        ### Filter the cavity and molds
        form.fields["headCavID"].queryset = PartIdentifier.objects.filter(
            mold_number__mold_number=active_job[0].moldNumber)

        ### Get inspection parameters
        inspecParam = PartInspection.objects.get(item_Number__item_Number=active_job[0].item.item_Number)
        min_val = inspecParam.min_part_weight
        max_val = inspecParam.max_part_weight
        num_id = '#id_partWeight'

        template = loader.get_template('inspection/forms/genInspection.html')
        context = RequestContext(request, {
            'form_title' : 'Part Weight Inspection Form',
            'form': form,
            'active_job': active_job,
            'use_minmax': True,
            'min_val': min_val,
            'max_val': max_val,
            'num_id' : num_id,
        })
        return HttpResponse(template.render(context))



@login_required
def view_shotWeightInspection(request, jobNumber):
    active_job = startUpShot.objects.filter(jobNumber=jobNumber).select_related('item')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = shotWeightForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            act_cav = MattecProd.objects.get(jobNumber=jobNumber)

            newForm = shotWeightInspection(
                jobID=startUpShot.objects.get(jobNumber=jobNumber),
                machineOperator=Employees.objects.get(pk=form.cleaned_data['machineOperator'].pk),
                inspectorName=Employees.objects.get(pk=form.cleaned_data['inspectorName'].pk),
                shotWeight=form.cleaned_data['shotWeight'],
                activeCavities=act_cav.activeCavities
            )
            # process the data in form.cleaned_data as required
            # part_number = form.cleaned_data['jobID']
            redirect_url = '/inspection/%s/' % (jobNumber)
            # save the data
            newForm.save()
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = shotWeightForm(
            initial={'jobID': startUpShot.objects.get(jobNumber=jobNumber).id},
        )
        form = presetStandardFields(form, jobID=jobNumber)

        act_cav = MattecProd.objects.get(jobNumber=jobNumber)

        inspecParam = PartInspection.objects.get(item_Number__item_Number=active_job[0].item.item_Number)
        min_val = inspecParam.min_part_weight * act_cav.activeCavities
        max_val = inspecParam.max_part_weight * act_cav.activeCavities
        num_id = '#id_shotWeight'

        template = loader.get_template('inspection/forms/genInspection.html')
        context = RequestContext(request, {
            'form_title' : 'Shot Weight Inspection Form',
            'form': form,
            'active_job': active_job,
            'use_minmax': True,
            'min_val': min_val,
            'max_val': max_val,
            'num_id' : num_id,
        })
        return HttpResponse(template.render(context))


######################################
#
#  Section for generating reports
#
######################################


@login_required
def view_jobReportSearch(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = jobReportSearch(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            job_number = form.cleaned_data['job_Number']
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']

            context_dic = createJobReportDict(job_number, date_from=date_from, date_to=date_to)
            template = loader.get_template('inspection/reports/jobReport.html')

            context = RequestContext(request, context_dic)
            return HttpResponse(template.render(context))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = jobReportSearch()

    return render(request, 'inspection/searchForms/jobReportSearch.html', {'form': form})


@login_required
def view_itemReportSearch(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = itemReportSearch(request.POST)
        # check whether it's valid:
        if form.is_valid():
            item_number = form.cleaned_data['item_Number']
            date_from = form.cleaned_data['date_from']
            date_to = form.cleaned_data['date_to']
            context_dic = {}
            context_dic['partDict'] = createItemReportDict(item_number, date_from=date_from, date_to=date_to)
            template = loader.get_template('inspection/reports/partReport.html')
            context = RequestContext(request, context_dic)
            return HttpResponse(template.render(context))


    # if a GET (or any other method) we'll create a blank form
    else:
        form = itemReportSearch()

    return render(request, 'inspection/searchForms/itemReportSearch.html', {'form': form})


@login_required
def view_itemReport(request, itemNumber):
    context_dict = {}
    context_dict['partDict'] = createItemReportDict(itemNumber)
    print context_dict

    template = loader.get_template('inspection/reports/partReport.html')
    context = RequestContext(request, context_dict)
    return HttpResponse(template.render(context))


@login_required
def view_jobReport(request, jobNumber):
    context_dic = createJobReportDict(jobNumber)
    template = loader.get_template('inspection/reports/jobReport.html')
    context = RequestContext(request, context_dic)
    return HttpResponse(template.render(context))



####### Helper functions ###########

def createItemReportDict(itemNumber, date_from=None, date_to=None):
    date_from, date_to = createDateRange(date_from=date_from, date_to=date_to)

    try:
        inspectionTypes = PartInspection.objects.get(item_Number__item_Number=itemNumber)
    except ObjectDoesNotExist:
        raise Http404("No inspections types were set")

    jobList = startUpShot.objects.filter(item__item_Number=itemNumber, dateCreated__range=(date_from, date_to))
    jobList = jobList.values_list('jobNumber', flat=True)
    partDict = {}
    n = 0
    for eachJob in jobList:
        dictID = 'Job%i' % (n)
        n += 1
        partDict[dictID] = {}
        partDict[dictID]['startupInfo'] = startUpShot.objects.filter(jobNumber=eachJob, dateCreated__range=(
            date_from, date_to)).select_related('item')

        # Job number 6 and 9 should be QA and
        partDict[dictID]['phl'] = ProductionHistory.objects.filter(jobNumber__jobNumber=eachJob,
                                                                   dateCreated__range=(date_from, date_to),
                                                                   inspectorName__EmpJob__JobNum=6)  # |\


        if inspectionTypes.visual_inspection:
            temp_obj = visualInspection.objects.filter(jobID__jobNumber=eachJob,
                                                       dateCreated__range=(date_from, date_to))
            partDict[dictID]['InspectionDates'] = {}
            partDict[dictID]['InspectionDates'] = temp_obj.aggregate(Min('dateCreated'), Max('dateCreated'))

            partDict[dictID]['visualInspectionDict'] = {}
            ### Count number of passed inspections
            partDict[dictID]['visualInspectionDict']['numPass'] = temp_obj.filter(inspectionResult=1).count()

            ### Count number of failed inspections
            partDict[dictID]['visualInspectionDict']['numFail'] = temp_obj.filter(inspectionResult=0).count()

            ### Calculate number of total inspections
            partDict[dictID]['visualInspectionDict']['totalInspections'] = partDict[dictID]['visualInspectionDict'][
                                                                               'numPass'] + \
                                                                           partDict[dictID]['visualInspectionDict'][
                                                                               'numFail']
            ### Calculate percentage passed
            if partDict[dictID]['visualInspectionDict']['totalInspections'] > 0:
                partDict[dictID]['visualInspectionDict']['passPerc'] = 100 * partDict[dictID]['visualInspectionDict'][
                    'numPass'] / partDict[dictID]['visualInspectionDict']['totalInspections']
            else:
                partDict[dictID]['visualInspectionDict']['passPerc'] = 0

        if inspectionTypes.part_weight_inspection:
            temp_obj = partWeightInspection.objects.filter(jobID__jobNumber=eachJob,
                                                           dateCreated__range=(date_from, date_to))
            partDict[dictID]['partWeightInspection'] = temp_obj
            partDict[dictID]['partWeightInspectionDict'] = {}
            partDict[dictID]['partWeightInspectionDict'] = temp_obj.aggregate(Avg('partWeight'),
                                                                              Max('partWeight'),
                                                                              Min('partWeight'),
                                                                              StdDev('partWeight'))
        if inspectionTypes.shot_weight_inspection:
            partDict[dictID]['shotWeightInspection'] = shotWeightInspection.objects.filter(jobID__jobNumber=eachJob,
                                                                                           dateCreated__range=(
                                                                                               date_from, date_to))

            partWeightList = []
            for eachShot in partDict[dictID]['shotWeightInspection']:
                partWeightList.append(eachShot.shotWeight / eachShot.activeCavities)

            partDict[dictID]['partWeightInspectionDict'] = {}
            partDict[dictID]['partWeightInspectionDict'] = \
                {
                    'partWeight__min':    '%1.3f' % (np.amin(partWeightList)),
                    'partWeight__max':    '%1.3f' % (np.amax(partWeightList)),
                    'partWeight__avg':    '%1.3f' % (np.mean(partWeightList)),
                    'partWeight__stddev': '%1.3f' % (np.std(partWeightList))
                }


        if inspectionTypes.od_inspection:
            partDict[dictID]['od_inspection'] = outsideDiameterInspection.objects.filter(jobID__jobNumber=eachJob,
                                                                                         dateCreated__range=(
                                                                                             date_from, date_to))
            partDict[dictID]['od_inspectionDict'] = {}
            partDict[dictID]['od_inspectionDict'] = partDict[dictID]['od_inspection'].aggregate(
                Avg('outsideDiameter'),
                Max('outsideDiameter'),
                Min('outsideDiameter'),
                StdDev('outsideDiameter'))

        if inspectionTypes.vol_inspection:
            partDict[dictID]['vol_inspection'] = volumeInspection.objects.filter(jobID__jobNumber=eachJob,
                                                                                 dateCreated__range=(
                                                                                     date_from, date_to))
            partDict[dictID]['vol_inspectionDict'] = {}
            partDict[dictID]['vol_inspectionDict'] = partDict[dictID]['od_inspection'].aggregate(
                Avg('liquidWeight'),
                Max('liquidWeight'),
                Min('liquidWeight'),
                StdDev('liquidWeight'))

        if inspectionTypes.neck_diameter_inspection:
            partDict[dictID]['neckDiam_inspection'] = neckDiameterInspection.objects.filter(jobID__jobNumber=eachJob,
                                                                                            dateCreated__range=(
                                                                                                date_from, date_to))
            partDict[dictID]['neckDiam_inspectionDict'] = {}
            partDict[dictID]['neckDiam_inspectionDict']['numPass'] = partDict[dictID]['neckDiam_inspection'].filter(
                testResult=1).count()
            partDict[dictID]['neckDiam_inspectionDict']['numFail'] = partDict[dictID]['neckDiam_inspection'].filter(
                testResult=0).count()
            partDict[dictID]['neckDiam_inspectionDict']['totalInspections'] = \
            partDict[dictID]['neckDiam_inspectionDict']['numPass'] + \
            partDict[dictID]['neckDiam_inspectionDict']['numFail']

            ### Calculate percentage passed
            if partDict[dictID]['neckDiam_inspectionDict']['totalInspections'] > 0:
                partDict[dictID]['neckDiam_inspectionDict']['passPerc'] = 100 * \
                                                                          partDict[dictID]['neckDiam_inspectionDict'][
                                                                              'numPass'] / \
                                                                          partDict[dictID]['neckDiam_inspectionDict'][
                                                                              'totalInspections']
            else:
                partDict[dictID]['neckDiam_inspectionDict']['passPerc'] = 0

        if inspectionTypes.assembly_test_inspection:
            partDict[dictID]['assembly_inspection'] = assemblyInspection.objects.filter(jobID__jobNumber=eachJob,
                                                                                        dateCreated__range=(
                                                                                            date_from, date_to))
        if inspectionTypes.carton_temp_inspection:
            partDict[dictID]['cartonTemp_inspection'] = cartonTemperature.objects.filter(jobID__jobNumber=eachJob,
                                                                                         dateCreated__range=(
                                                                                             date_from, date_to))
            partDict[dictID]['cartonTemp_inspectionDict'] = {}
            partDict[dictID]['cartonTemp_inspectionDict'] = partDict[dictID]['cartonTemp_inspection'].aggregate(
                Avg('cartonTemp'),
                Max('cartonTemp'),
                Min('cartonTemp'),
                StdDev('cartonTemp'))

        if inspectionTypes.vision_system_inspection:
            partDict[dictID]['visionSys_inspection'] = visionInspection.objects.filter(jobID__jobNumber=eachJob,
                                                                                       dateCreated__range=(
                                                                                           date_from, date_to))


    return partDict

def createJobReportDict(jobNumber, date_from=None, date_to=None):
    date_from, date_to = createDateRange(date_from=date_from, date_to=date_to)

    context_dic = {}

    active_job = startUpShot.objects.filter(jobNumber=jobNumber).select_related('item')

    context_dic['active_job'] = active_job

    # Job number 6 and 9 should be QA and
    context_dic['phl'] = ProductionHistory.objects.filter(jobNumber__jobNumber=jobNumber,
                                                          dateCreated__range=(date_from, date_to),
                                                          inspectorName__EmpJob__JobNum=6)

    pf_inspectionType = passFailByPart.objects.filter(item_Number__item_Number=active_job[0].item)

    context_dic['pf'] = {}
    for each_pf_inspection in pf_inspectionType:
        context_dic['pf'][each_pf_inspection.testName] = passFailInspection.objects.filter(passFailTestName__testName=each_pf_inspection.testName,
                                                                                     jobID__jobNumber=jobNumber)

        context_dic['pf'][each_pf_inspection.testName]['numPass'] = context_dic['pf'][each_pf_inspection.testName].filter(
            inspectionResult=1).count()

        ### Count number of failed inspections
        context_dic['pf'][each_pf_inspection.testName]['numFail'] = context_dic['pf'][each_pf_inspection.testName].filter(
            inspectionResult=0).count()

        ### Calculate number of total inspections
        context_dic['pf'][each_pf_inspection.testName]['totalInspections'] = context_dic['pf'][each_pf_inspection.testName]['numPass'] + \
                                                                  context_dic['pf'][each_pf_inspection.testName]['numFail']
        ### Calculate percentage passed
        if context_dic['pf'][each_pf_inspection.testName]['totalInspections'] > 0:
            context_dic['pf'][each_pf_inspection.testName]['passPerc'] = 100 * context_dic['pf'][each_pf_inspection.testName]['numPass'] / + \
                context_dic['pf'][each_pf_inspection.testName]['totalInspections']
        else:
            context_dic['pf'][each_pf_inspection.testName]['passPerc'] = 0
    #
    # if inspectionTypes.visual_inspection:
    #     context_dic['visualInspection'] = visualInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                       dateCreated__range=(date_from, date_to))
    #
    #     context_dic['InspectionDates'] = {}
    #     context_dic['InspectionDates'] = context_dic['visualInspection'].aggregate(Min('dateCreated'),
    #                                                                                Max('dateCreated'))
    #
    #     ### Initialize dictionary for summary stats
    #     context_dic['visualInspectionDict'] = {}
    #     ### Count number of passed inspections
    #     context_dic['visualInspectionDict']['numPass'] = context_dic['visualInspection'].filter(
    #         inspectionResult=1).count()
    #
    #     ### Count number of failed inspections
    #     context_dic['visualInspectionDict']['numFail'] = context_dic['visualInspection'].filter(
    #         inspectionResult=0).count()
    #
    #     ### Calculate number of total inspections
    #     context_dic['visualInspectionDict']['totalInspections'] = context_dic['visualInspectionDict']['numPass'] + \
    #                                                               context_dic['visualInspectionDict']['numFail']
    #     ### Calculate percentage passed
    #     if context_dic['visualInspectionDict']['totalInspections'] > 0:
    #         context_dic['visualInspectionDict']['passPerc'] = 100 * context_dic['visualInspectionDict']['numPass'] / + \
    #             context_dic['visualInspectionDict']['totalInspections']
    #     else:
    #         context_dic['visualInspectionDict']['passPerc'] = 0
    #
    # if inspectionTypes.part_weight_inspection:
    #     context_dic['partWeightInspection'] = partWeightInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                               dateCreated__range=(
    #                                                                                   date_from, date_to))
    #     context_dic['partWeightInspectionDict'] = {}
    #     context_dic['partWeightInspectionDict'] = context_dic['partWeightInspection'].aggregate(Avg('partWeight'),
    #                                                                                             Max('partWeight'),
    #                                                                                             Min('partWeight'),
    #                                                                                             StdDev('partWeight'))
    #
    # if inspectionTypes.shot_weight_inspection:
    #     context_dic['shotWeightInspection'] = shotWeightInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                               dateCreated__range=(
    #                                                                                   date_from, date_to))
    #
    #     partWeightList = []
    #     for eachShot in context_dic['shotWeightInspection']:
    #         partWeightList.append(eachShot.shotWeight / eachShot.activeCavities)
    #
    #     context_dic['partWeightInspectionDict'] = {}
    #     context_dic['partWeightInspectionDict'] = \
    #             {
    #                 'partWeight__min':    '%1.3f' % (np.amin(partWeightList)),
    #                 'partWeight__max':    '%1.3f' % (np.amax(partWeightList)),
    #                 'partWeight__avg':    '%1.3f' % (np.mean(partWeightList)),
    #                 'partWeight__stddev': '%1.3f' % (np.std(partWeightList))
    #             }
    #
    #
    #
    # if inspectionTypes.od_inspection:
    #     context_dic['od_inspection'] = outsideDiameterInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                             dateCreated__range=(
    #                                                                                 date_from, date_to))
    #     context_dic['od_inspectionDict'] = {}
    #     context_dic['od_inspectionDict'] = context_dic['od_inspection'].aggregate(
    #         Avg('outsideDiameter'),
    #         Max('outsideDiameter'),
    #         Min('outsideDiameter'),
    #         StdDev('outsideDiameter'))
    #
    # if inspectionTypes.vol_inspection:
    #     context_dic['vol_inspection'] = volumeInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                     dateCreated__range=(
    #                                                                         date_from, date_to))
    #     context_dic['vol_inspectionDict'] = {}
    #     context_dic['vol_inspectionDict'] = context_dic['od_inspection'].aggregate(
    #         Avg('liquidWeight'),
    #         Max('liquidWeight'),
    #         Min('liquidWeight'),
    #         StdDev('liquidWeight'))
    #
    # if inspectionTypes.neck_diameter_inspection:
    #     context_dic['neckDiam_inspection'] = neckDiameterInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                                dateCreated__range=(
    #                                                                                    date_from, date_to))
    #     context_dic['neckDiam_inspectionDict'] = {}
    #     context_dic['neckDiam_inspectionDict']['numPass'] = context_dic['neckDiam_inspection'].filter(
    #         testResult=1).count()
    #     context_dic['neckDiam_inspectionDict']['numFail'] = context_dic['neckDiam_inspection'].filter(
    #         testResult=0).count()
    #     context_dic['neckDiam_inspectionDict']['totalInspections'] = context_dic['neckDiam_inspectionDict']['numPass'] + \
    #                                                                  context_dic['neckDiam_inspectionDict']['numFail']
    #
    #     ### Calculate percentage passed
    #     if context_dic['neckDiam_inspectionDict']['totalInspections'] > 0:
    #         context_dic['neckDiam_inspectionDict']['passPerc'] = 100 * context_dic['neckDiam_inspectionDict'][
    #             'numPass'] / context_dic['neckDiam_inspectionDict']['totalInspections']
    #     else:
    #         context_dic['neckDiam_inspectionDict']['passPerc'] = 0
    #
    # if inspectionTypes.assembly_test_inspection:
    #     context_dic['assembly_inspection'] = assemblyInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                            dateCreated__range=(
    #                                                                                date_from, date_to))
    # if inspectionTypes.carton_temp_inspection:
    #     context_dic['cartonTemp_inspection'] = cartonTemperature.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                             dateCreated__range=(
    #                                                                                 date_from, date_to))
    #     context_dic['cartonTemp_inspectionDict'] = {}
    #     context_dic['cartonTemp_inspectionDict'] = context_dic['cartonTemp_inspection'].aggregate(
    #         Avg('cartonTemp'),
    #         Max('cartonTemp'),
    #         Min('cartonTemp'),
    #         StdDev('cartonTemp'))
    #
    # if inspectionTypes.vision_system_inspection:
    #     context_dic['visionSys_inspection'] = visionInspection.objects.filter(jobID__jobNumber=jobNumber,
    #                                                                           dateCreated__range=(
    #                                                                               date_from, date_to))
    #

    return context_dic


######################
#
# Helper functions
#
######################

def createDateRange(date_from=None, date_to=None):
    if date_from is None:
        date_from = datetime.datetime.strptime('1900-01-01', '%Y-%m-%d')
        date_from = timezone.make_aware(date_from, timezone.get_current_timezone())

    if date_to is None:
        date_to = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        date_to = timezone.make_aware(date_to, timezone.get_current_timezone())

    return (date_from, date_to)


def presetStandardFields(my_form, jobID):
    # this will preset machine and qa fields
    ### Filter the machine operators
    my_form.fields["machineOperator"].queryset = Employees.objects.filter(EmpJob__JobNum=9).order_by('EmpShift')
                                                                         # EmpShift=getShift())
    ### Filter the QA ladies
    my_form.fields["inspectorName"].queryset = Employees.objects.filter(EmpJob__JobNum=6).order_by('EmpShift')
                                                                       # EmpShift=getShift())
    my_form.fields["jobID"].queryset = startUpShot.objects.filter(jobNumber=jobID)


    return my_form


def getShift():
    currentHour = datetime.datetime.time(datetime.datetime.now()).hour

    if (currentHour >= 7) and (currentHour < 15):
        shift = 1
    elif (currentHour >= 15) and (currentHour < 23):
        shift = 2
    else:
        shift = 3

    return shift

def checkPartInspection(item_Number):
    if not passFailByPart.objects.filter(item_Number__item_Number=item_Number,testName__testName='Visual Inspection').exists():
        newPartInspection = passFailByPart(item_Number = Part.objects.get(item_Number=item_Number),
                                           testName = passFailTest.objects.get(testName='Visual Inspection'))
        newPartInspection.save()

    # Will probably need to create something for shot weights...


def checkMoldCavs(item_Number=None,mold_Number=None):
    if item_Number:
        mattec_info = MattecProd.objects.get(itemNo=item_Number)
        mold_Number = mattec_info.moldNumber

    if not PartIdentifier.objects.filter(mold_number__mold_number=mold_Number).exists():
        ### grab the mold information
        mold_info = Mold.objects.get(mold_number = mold_Number)
        ### add all the cavities
        for n in range(mold_info.num_cavities):
            newCavID = PartIdentifier(mold_number=mold_info,head_code='A',cavity_id = '%i' % (n))
            newCavID.save()