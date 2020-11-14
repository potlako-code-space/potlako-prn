from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import OTHER

from ..form_validators import OffstudyFormValidator


class TestOffstudyForm(TestCase):

    def test_cause_invalid(self):
        cleaned_data = {
            'reason': OTHER,
        }
        form_validator = OffstudyFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('reason_other', form_validator._errors)

    def test_cause_valid(self):
        cleaned_data = {
            'reason': OTHER,
            'reason_other': 'blah',
        }
        form_validator = OffstudyFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
