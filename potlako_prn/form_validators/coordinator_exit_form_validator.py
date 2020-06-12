from edc_constants.constants import YES
from edc_form_validators import FormValidator


class CoordinatorExitFormValidator(FormValidator):

    def clean(self):
        super().clean()

        self.validate_other_specify(
            field='components_rec'
        )

        self.required_if(
            YES,
            field='cancer_treatment_rec',
            field_required='cancer_treatment')

        self.validate_other_specify(
            field='cancer_treatment'
        )

        self.required_if(
            YES,
            field='date_therapy_started_estimated',
            field_required='date_therapy_started_estimation')
