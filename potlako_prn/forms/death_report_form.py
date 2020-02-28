from django import forms
from edc_form_validators import FormValidatorMixin
from ..models import DeathReport


class DeathReportForm(FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = DeathReport
        fields = '__all__'
