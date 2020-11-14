from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import DeathReportFormValidator
from ..models import DeathReport


class DeathReportForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReport
        fields = '__all__'
