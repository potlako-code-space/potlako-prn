from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import CoordinatorExitFormValidator
from ..models import CoordinatorExit


class CoordinatorExitForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = CoordinatorExitFormValidator

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),)

    class Meta:
        model = CoordinatorExit
        fields = '__all__'
