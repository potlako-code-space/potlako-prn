from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

from edc_sync.models import OutgoingTransaction


@tag('sync1')
class TestOutGoingTransactions(TestCase):

    def test_outgoing_transactions_none_valid(self):
        self.assertEqual(
            OutgoingTransaction.objects.all().count(), 0)

    def test_outgoing_transactions_valid(self):
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

        self.subject_consent = mommy.make_recipe(
            'potlako_subject.subjectconsent',
            **self.options)

        self.subject_consent = mommy.make_recipe(
            'potlako_prn.deathreport',)

        def test_outgoing_transactions_none_valid(self):
            self.assertNotEqual(
                OutgoingTransaction.objects.filter(
                    tx_name__startswith='potlako_prn').count(), 0)
