from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import OffstudyFormValidator
from ..models import SubjectOffStudy


class SubjectOffStudyForm(FormValidatorMixin, forms.ModelForm):

    OffstudyFormValidator.visit_model = 'potlako_subject.subjectvisit'

    form_validator_cls = OffstudyFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),)

    class Meta:
        model = SubjectOffStudy
        fields = '__all__'
