from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import OTHER, YES

from ..form_validators import CoordinatorExitFormValidator


class TestCoordinatorExitForm(TestCase):

    def test_components_rec_invalid(self):
        cleaned_data = {
            'components_rec': OTHER,
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('components_rec_other', form_validator._errors)

    def test_components_rec_valid(self):
        cleaned_data = {
            'components_rec': OTHER,
            'components_rec_other': 'blah',
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cancer_treatment_rec_invalid(self):
        cleaned_data = {
            'cancer_treatment_rec': YES,
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('cancer_treatment', form_validator._errors)

    def test_cancer_treatment_rec_valid(self):
        cleaned_data = {
            'cancer_treatment_rec': YES,
            'cancer_treatment': 'blah',
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cancer_treatment_invalid(self):
        cleaned_data = {
            'cancer_treatment': OTHER,
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('cancer_treatment_other', form_validator._errors)

    def test_cancer_treatment_valid(self):
        cleaned_data = {
            'cancer_treatment': OTHER,
            'cancer_treatment_other': 'blah',
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_date_therapy_started_estimation_invalid(self):
        cleaned_data = {
            'date_therapy_started_estimated': YES,
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('date_therapy_started_estimation', form_validator._errors)

    def test_date_therapy_started_estimation_valid(self):
        cleaned_data = {
            'date_therapy_started_estimated': YES,
            'date_therapy_started_estimation': 'blah',
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
