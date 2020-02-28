from django import forms
from edc_form_validators import FormValidatorMixin

from ..models import SubjectOffStudy


class SubjectOffStudyForm(FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = SubjectOffStudy
        fields = '__all__'
