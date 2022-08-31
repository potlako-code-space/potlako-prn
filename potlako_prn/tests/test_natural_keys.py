from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

# from edc_appointment.models import Appointment
from edc_sync.models import OutgoingTransaction
from edc_sync.tests import SyncTestHelper

from ..sync_models import sync_models


@tag('sync')
class TestNaturalKey(TestCase):

    sync_test_helper = SyncTestHelper()

    def setUp(self):
        import_holidays()

        clinicial_call_enrolment = self.subject_screening = mommy.make_recipe(
            'potlako_subject.cliniciancallenrollment',
            facility='bokaa_clinic')

        self.subject_screening = mommy.make_recipe(
            'potlako_subject.subjectscreening',
            screening_identifier=clinicial_call_enrolment.screening_identifier)

        self.options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow() - relativedelta(days=5),
            'identity': clinicial_call_enrolment.national_identity,
            'confirm_identity': clinicial_call_enrolment.national_identity,
            'version': '1'}

        mommy.make_recipe(
            'potlako_subject.verbalconsent',
            screening_identifier=self.subject_screening.screening_identifier,
            )

        self.subject_consent = mommy.make_recipe(
            'potlako_subject.subjectconsent',
            **self.options)

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr('potlako_prn')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr('potlako_prn')
