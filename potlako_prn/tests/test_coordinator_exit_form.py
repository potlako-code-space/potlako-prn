from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import OTHER, YES, NO

from ..form_validators import CoordinatorExitFormValidator
from .models import ListModel

@tag('ce')
class TestCoordinatorExitForm(TestCase):

    def setUp(self):
        ListModel.objects.create(name=OTHER)

    def test_components_rec_invalid(self):
        cleaned_data = {
            'components_rec': ListModel.objects.all(),
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('components_rec_other', form_validator._errors)

    def test_components_rec_valid(self):
        cleaned_data = {
            'components_rec': ListModel.objects.all(),
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
            'date_therapy_started': get_utcnow().date(),
            'date_therapy_started_estimated': NO,
            'treatment_intent': 'blah',
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

    def test_treatment_intent_valid(self): 
        cleaned_data = {
            'cancer_treatment_rec': YES,
            'cancer_treatment': 'blah',
            'treatment_intent': 'blah',
            'date_therapy_started': get_utcnow().date(),
            'date_therapy_started_estimated': NO
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
            
            
    def test_treatment_intent_invalid(self): 
        cleaned_data = {
            'cancer_treatment_rec': YES,
            'cancer_treatment': 'blah',
            'date_therapy_started': get_utcnow().date(),
            'date_therapy_started_estimated': NO
        }
        form_validator = CoordinatorExitFormValidator(
            cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('treatment_intent', form_validator._errors)           