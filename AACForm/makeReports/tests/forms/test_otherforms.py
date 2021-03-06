"""
This tests the other forms work as expected
"""
from django.test import TestCase
from django.urls import reverse
from makeReports.models import *
from unittest import mock
from django.http import HttpResponse
import requests
from model_bakery import baker
from django import forms
from makeReports.forms import *
from datetime import datetime
class SubmitReportformTest(TestCase):
    """
    Tests forms relating to submitting reports
    """
    def test_submit_valid(self):
        """
        Tests SubmitReportForm properly takes valid
        """
        f = SubmitReportForm({
            'hidden':''
        },valid=True, eMsg="")
        self.assertTrue(f.is_valid())
    def test_submit_invalid(self):
        """
        Tests SubmitReportForm properly takes invalid argument
        """
        f = SubmitReportForm({
            'hidden':''
        },valid=False, eMsg="error is occuring")
        self.assertFalse(f.is_valid())