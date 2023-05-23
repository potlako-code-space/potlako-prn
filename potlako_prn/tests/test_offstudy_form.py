from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import DEAD, OTHER
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

from edc_action_item.site_action_items import site_action_items
from potlako_prn.models.coordinator_exit import CoordinatorExit

from ..action_items import COORDINATOR_EXIT_ACTION, DEATH_REPORT_ACTION
from ..form_validators import OffstudyFormValidator
from ..models import DeathReport


@tag('ofs')
class TestOffstudyForm(TestCase):

    def setUp(self):
        import_holidays()

        self.clinicial_call_enrolment = self.subject_screening = mommy.make_recipe(
            'potlako_subject.cliniciancallenrollment')

        self.subject_screening = mommy.make_recipe(
            'potlako_subject.subjectscreening',
            screening_identifier=self.clinicial_call_enrolment.screening_identifier)

        self.verbal_consent = mommy.make_recipe(
            'potlako_subject.verbalconsent',
            screening_identifier=self.clinicial_call_enrolment.screening_identifier)

        self.options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow,
            'identity': self.clinicial_call_enrolment.national_identity,
            'confirm_identity': self.clinicial_call_enrolment.national_identity,
            'version': '1'}

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

    def test_coordinator_exit_triggered(self):

        subject_consent = mommy.make_recipe('potlako_subject.subjectconsent',
                                            **self.options)

        mommy.make_recipe('potlako_prn.subjectoffstudy',
                          subject_identifier=subject_consent.subject_identifier)

        action_cls = site_action_items.get(CoordinatorExit.action_name)
        action_item_model_cls = action_cls.action_item_model_cls()

        self.assertEqual(action_item_model_cls.objects.filter(
            subject_identifier=subject_consent.subject_identifier,
            action_type__name=COORDINATOR_EXIT_ACTION).count(), 1)

    def test_death_report_exit_triggered(self):

        subject_consent = mommy.make_recipe('potlako_subject.subjectconsent',
                                            **self.options)

        mommy.make_recipe('potlako_prn.subjectoffstudy',
                          reason='death',
                          subject_identifier=subject_consent.subject_identifier)

        action_cls = site_action_items.get(DeathReport.action_name)
        action_item_model_cls = action_cls.action_item_model_cls()

        self.assertEqual(action_item_model_cls.objects.filter(
            subject_identifier=subject_consent.subject_identifier,
            action_type__name=DEATH_REPORT_ACTION).count(), 1)
