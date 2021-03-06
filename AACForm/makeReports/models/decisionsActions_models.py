"""
This file contains models most directly related to decisions and actions
"""
from django.db import models
from makeReports.choices import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from gdstorage.storage import GoogleDriveStorage
from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe
import os
from .basic_models import gd_storage, NonArchivedManager

class DecisionsActions(models.Model):
    """
    Model of decisions/actions for a report
    """
    sloIR = models.OneToOneField('SLOInReport', on_delete=models.CASCADE)
    text = models.CharField(max_length=3000, blank=True, default="")

class ReportSupplement(models.Model):
    """
    Model to hold supplements to the report as a whole
    """
    supplement = models.FileField(
        upload_to='data/supplements', 
        storage=gd_storage,
        validators=[FileExtensionValidator(allowed_extensions=('pdf',))])
    report = models.ForeignKey('Report', on_delete=models.CASCADE)
    def __str__(self):
        return os.path.basename(self.supplement.name)