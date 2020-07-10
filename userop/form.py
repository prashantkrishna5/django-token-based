from django import forms
from django.core.exceptions import ValidationError
from .models import TestQuery

class TestQueryForm(forms.ModelForm):
    class Meta:
        model = TestQuery()
        fields = ['State',
                  'ProblemID',
                  'ProblemTitle',
                  'MobileNubers']
