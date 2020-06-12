from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import CoordinatorExitFormValidator
from ..models import CoordinatorExit


class CoordinatorExitForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = CoordinatorExitFormValidator

    class Meta:
        model = CoordinatorExit
        fields = '__all__'
