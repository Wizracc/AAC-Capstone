"""
Generates the to-do list for each section
"""
from makeReports.models import *
from makeReports.forms import *
from django.contrib.auth.models import User
from .text_processing import blooms_suggestion, is_complex
def section1ToDo(report):
    """
    Generates the ToDo list for section 1 and first page of report, includes things missing from the beginning of the report

    Args:
        report (:class:`~makeReports.models.Report`): in-progress report to generate to-do for
    Returns:
        dict, QuerySet : dictionary of to-dos, QuerySet of SLOs in report
    Notes:
        Extra return values prevent repeatedly querying the database for the same things
    """
    toDos = {
            'r':[],
            #"required"
            's':[]
            #"suggested"
        }
    slos = SLOInReport.objects.filter(report=report).order_by("number")
    if not report.author:
        toDos['r'].append(("Add author to report",0))
    if not report.date_range_of_reported_data:
        toDos['s'].append(("Add date range of reported data",0))
    if slos.count() is 0:
        toDos['r'].append(("Create an SLO",1))
    if SLOsToStakeholder.objects.filter(report=report).count() is 0:
        toDos['r'].append(("Add description of how SLOs are communicated to stakeholders",1))
    for slo in slos:
        b = blooms_suggestion(slo.goalText)
        if b and b != slo.slo.get_blooms_display and b!="none":
            toDos['s'].append(("Set the Bloom's level of SLO "+str(slo.number)+" to "+b,1))
        if is_complex(slo.goalText):
            toDos['s'].append(("Simplify or split SLO "+str(slo.number)+" into multiple, focused SLOs",1))
    return toDos, slos
def section2ToDo(report):
    """
    Generates the to-do list for section 2, inclusive of prior sections
    
    Args:
        report (:class:`~makeReports.models.Report`): in-progress report to generate to-do for
    Returns:
        dict, QuerySet, QuerySet : dictionary of to-dos, QuerySet of SLOs in report, QuerySet of assessments in report
    Notes:
        Extra return values prevent repeatedly querying the database for the same things

    """
    toDos, slos = section1ToDo(report)
    assess = AssessmentVersion.objects.filter(report=report).order_by("slo__number","number")
    for slo in slos:
        if assess.filter(slo=slo).count() is 0:
            toDos['r'].append(("Add an assessment for SLO "+str(slo.number),2))
        elif assess.filter(slo=slo, assessment__directMeasure=True).count() is 0:
            toDos['s'].append(("Add a direct measure for SLO "+str(slo.number),2))
    return toDos, slos, assess
def section3ToDo(report):
    """
    Generates the to-do list for section 3, including prior sections

    Args:
        report (:class:`~makeReports.models.Report`): in-progress report to generate to-do for
    Returns:
        dict, QuerySet, QuerySet, QuerySet : dictionary of to-dos, QuerySet of SLOs in report, QuerySet of assessments in report, QuerySet of data in report
    Notes:
        Extra return values prevent repeatedly querying the database for the same things

    """
    toDos, slos, assess = section2ToDo(report)
    data = AssessmentData.objects.filter(assessmentVersion__report=report)
    for a in assess:
        if data.filter(assessmentVersion=a).count() is 0:
            toDos['s'].append(("Add data for assessment SLO "+str(a.slo.number)+", measure "+str(a.number),3))
        elif AssessmentAggregate.objects.filter(assessmentVersion=a).count() is 0:
            toDos['s'].append(("Add an aggregation of data for SLO "+str(a.slo.number)+", measure "+str(a.number),3))
    if ResultCommunicate.objects.filter(report=report).count() is 0:
        toDos['r'].append(("Add description of how results are communicated within the program",3))
    return toDos, slos, assess, data
def section4ToDo(report):
    """
    Generates to-do list for section 4, including prior sections

    Args:
        report (:class:`~makeReports.models.Report`): in-progress report to generate to-do for
    Returns:
        dict : dictionary of to-dos
    Notes:
        Last section, so extra return values are unneeded
    """
    toDos, slos, assess, data = section3ToDo(report)
    dAs = DecisionsActions.objects.filter(sloIR__report=report)
    for slo in slos:
        if dAs.filter(sloIR=slo).count() is 0:
            toDos['r'].append(("Add a description of decisions and actions relating to SLO "+str(slo.number),4))
    return toDos
def todoGetter(section,report):
    """
    Gets the to-do list for given section of a report
    Normalizes the return value to just the to-do list

    Args:
        report (:class:`~makeReports.models.Report`): in-progress report to generate to-do for
        section (int): section number of section to generate list for
    Returns:
        dict : dictionary of to-do list, separated into required and suggestions
    """
    toDos = None
    if section is 1:
        toDos, x = section1ToDo(report)
    elif section is 2:
        toDos, x, y = section2ToDo(report)
    elif section is 3:
        toDos, x, y, z = section3ToDo(report)
    elif section is 4:
        toDos = section4ToDo(report)
    return toDos