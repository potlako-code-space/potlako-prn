from edc_constants.constants import YES
from edc_form_validators import FormValidator


class DeathReportFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='cause',)

        self.validate_other_specify(
            field='cause_category',)

        self.required_if(
            YES,
            field='participant_hospitalized',
            field_required='days_hospitalized')
