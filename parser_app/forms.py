from django import forms
from .models import job


class DocumentForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ('jobid', 'jobrole', 'jobdate',
                  'joblocation', 'jobdescription','jobexp', 'p1', 'p2')
