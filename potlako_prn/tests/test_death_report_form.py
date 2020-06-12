from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import OTHER, YES

from ..form_validators import DeathReportFormValidator


class TestDeathReportForm(TestCase):

    def test_cause_invalid(self):
        cleaned_data = {
            'cause': OTHER,
        }
        form_validator = DeathReportFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('cause_other', form_validator._errors)

    def test_cause_valid(self):
        cleaned_data = {
            'cause': OTHER,
            'cause_other': 'blah',
        }
        form_validator = DeathReportFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_category_invalid(self):
        cleaned_data = {
            'cause_category': OTHER,
        }
        form_validator = DeathReportFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('cause_category_other', form_validator._errors)

    def test_cause_category_valid(self):
        cleaned_data = {
            'cause_category': OTHER,
            'cause_category_other': 'blah',
        }
        form_validator = DeathReportFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_participant_hospitalized_invalid(self):
        cleaned_data = {
            'participant_hospitalized': YES,
        }
        form_validator = DeathReportFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('days_hospitalized', form_validator._errors)

    def test_participant_hospitalized_valid(self):
        cleaned_data = {
            'participant_hospitalized': YES,
            'days_hospitalized': 'blah',
        }
        form_validator = DeathReportFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
