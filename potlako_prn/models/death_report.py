from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.model_validators import datetime_not_future
from edc_base.sites.managers import CurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import datetime_not_before_study_start

from ..action_items import DEATH_REPORT_ACTION
from ..choices import DEATH_INFO_SOURCE, DEATH_PLACE, CAUSE_OF_DEATH_CAT
from ..choices import MED_RESPONSIBILITY, FACILITY


class DeathReport(SiteModelMixin, ActionModelMixin, BaseUuidModel):

    action_name = DEATH_REPORT_ACTION

    tracking_identifier = 'DR'

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    death_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of Death:')

    cause = models.CharField(
        max_length=50,
        choices=DEATH_INFO_SOURCE,
        verbose_name=('What was the source of information about participant'
                      'death?'
                      ))

    cause_other = OtherCharField(
        max_length=50)

    perform_autopsy = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Will an autopsy be performed later')

    death_cause = models.TextField(
        verbose_name=('Describe the major cause of death (including pertinent'
                      ' autopsy information if available), starting with the'
                      ' first noticeable illness thought to be  related to'
                      ' death, continuing to time of death.'),
        blank=True,
        null=True,
        help_text=('Note: Cardiac and pulmonary arrest are not major reasons'
                   ' and should not be used to describe major cause'))

    cause_category = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH_CAT,
        verbose_name=('Based on the description above, what category'
                      ' best defines the major cause of death?'))

    cause_category_other = OtherCharField()

    illness_duration = models.IntegerField(
        verbose_name='Duration of acute illness directly causing death',
        help_text='in days (If unknown enter -1)')

    medical_responsibility = models.CharField(
        choices=MED_RESPONSIBILITY,
        max_length=50,
        verbose_name=('Who was responsible for primary medical care of the '
                      'participant during the month prior to death?'))

    death_known = models.DateField(
        validators=[date_not_future],
        verbose_name=('When did the study team learn about the patient\'s '
                      'death?'))

    place_of_death = models.CharField(
        verbose_name=('Name the place where the patient died?'),
        choices=DEATH_PLACE,
        max_length=20,)

    facility_patient_died = models.CharField(
        verbose_name=('Name of the facility where the patient died?'),
        choices=FACILITY,
        max_length=50,
        blank=True,
        null=True,)

    facility_patient_died_other = OtherCharField()

    participant_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Was the participant hospitalised before death?')

    hospitalised_facility = models.CharField(
        verbose_name='What was the facility where the patient was hospitalised?',
        choices=FACILITY,
        max_length=40,
        blank=True,
        null=True,)

    hospitalised_facility_other = OtherCharField()

    days_hospitalized = models.IntegerField(
        verbose_name=('For how many days was the participant hospitalised'
                      ' during the illness immediately before death? '),
        help_text='in days',
        default=0)

    comment = models.TextField(
        max_length=250,
        verbose_name='Comments',
        blank=True,
        null=True)

    def get_consent_version(self):
        subject_consent_cls = django_apps.get_model(
            'potlako_subject.subjectconsent')
        try:
            subject_consent_obj = subject_consent_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except subject_consent_cls.DoesNotExist:
            raise ValidationError(
                'Missing Subject Consent form. Please complete '
                'it before proceeding.')
        else:
            return subject_consent_obj.version

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(DeathReport, self).save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier,)

    natural_key.dependencies = ['sites.Site']

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    class Meta:
        app_label = 'potlako_prn'
        verbose_name = 'Death Report'
