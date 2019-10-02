from django import forms
from makeReports.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from makeReports.choices import *
class SectionRubricForm(forms.Form):
    #section_comment = forms.CharField(max_length=2000, required=False, widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        rubricItems = kwargs.pop('rubricItems')
        super(SectionRubricForm, self).__init__(*args, **kwargs)
        for rI in rubricItems:
            self.fields['rI'+str(rI.pk)] = forms.ChoiceField(choices=RUBRIC_GRADES_CHOICES, widget=forms.RadioSelect,label=rI.text,required=False)
            #required=False so allow partial completion of the 
        self.fields['section_comment']=forms.CharField(max_length=2000, required=False, widget=forms.Textarea)
class RubricItemForm(forms.ModelForm):
    class Meta:
        model = RubricItem
        fields = ['text','section','order','DMEtext','MEtext','EEtext']
        labels = {
            'text':'Category text',
            'section':'Section number',
            'order':'Order position of item (lower numbers will be displayed first) (optional)',
            'DMEtext':'Did not meet expectations text',
            'MEtext':"Met expectations with concerns text",
            'EEtext':'Met expectations text'
        }
class DuplicateRubric(forms.Form):
    rubToDup = forms.ModelChoiceField(queryset=Rubric.objects, widget=forms.HiddenInput())