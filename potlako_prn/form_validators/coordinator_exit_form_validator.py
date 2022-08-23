from dataclasses import field
from edc_constants.constants import OTHER, YES, NO, UNKNOWN
from edc_form_validators import FormValidator


class CoordinatorExitFormValidator(FormValidator):

    def clean(self):
        super().clean()

        self.m2m_other_specify(
            OTHER, m2m_field='components_rec',
            field_other='components_rec_other')

        required_fields = ['cancer_treatment', 'date_therapy_started',
                           'date_therapy_started_estimated','treatment_intent']
        for required_field in required_fields:
            self.required_if(
                YES,
                field='cancer_treatment_rec',
                field_required=required_field)

        self.validate_other_specify(
            field='cancer_treatment'
        )

        self.required_if(
            YES,
            field='date_therapy_started_estimated',
            field_required='date_therapy_started_estimation')

