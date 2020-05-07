from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import OffstudyFormValidator
from ..models import SubjectOffStudy


class SubjectOffStudyForm(FormValidatorMixin, forms.ModelForm):

    OffstudyFormValidator.visit_model = 'potlako_subject.maternalvisit'

    form_validator_cls = OffstudyFormValidator

    class Meta:
        model = SubjectOffStudy
        fields = '__all__'
