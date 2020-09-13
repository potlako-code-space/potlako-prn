from edc_constants.constants import YES
from edc_form_validators import FormValidator


class DeathReportFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            'fam_member',
            field='cause',
            field_required='specify_relationship')

        self.validate_other_specify(
            field='cause',)

        self.validate_other_specify(
            field='cause_category',)

        self.required_if(
            'facility',
            field='place_of_death',
            field_required='facility_patient_died')

        required_fields = ['hospitalised_facility', 'days_hospitalized']
        for required in required_fields:
            self.required_if(
                YES,
                field='participant_hospitalized',
                field_required=required)

        self.validate_other_specify(field='hospitalised_facility')

        self.validate_other_specify(field='facility_patient_died')
