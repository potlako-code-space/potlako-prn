from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future, datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import (
    date_not_before_study_start, datetime_not_before_study_start)

from ..action_items import SUBJECT_OFFSTUDY_ACTION
from ..choices import FACILITY, FACILITY_TYPE, DATE_ESTIMATION
from ..choices import LTFU_CRITERIA, POS_NEG_UNKNOWN_MISSING
from ..choices import REASON_FOR_EXIT


class SubjectOffStudy(ActionModelMixin, BaseUuidModel):

    action_name = SUBJECT_OFFSTUDY_ACTION

    tracking_identifier_prefix = 'SO'

    schedule = models.CharField(
        verbose_name='Are scheduled data being submitted on the exit date?',
        max_length=3,
        choices=YES_NO,)

    offstudy_date = models.DateField(
        verbose_name='Offstudy date',
        null=True,
        default=get_utcnow,
        validators=[date_not_before_study_start, date_not_future],)

    report_datetime = models.DateTimeField(
        verbose_name='Report datetime',
        validators=[datetime_not_before_study_start, datetime_not_future],
        null=True,
        default=get_utcnow,)

    reason = models.CharField(
        verbose_name='Reason for exit',
        max_length=50,
        choices=REASON_FOR_EXIT,
        null=True,)

    general_comments = models.TextField(
        verbose_name='Any general comments about patient exit?',
        max_length=150,
        blank=True,
        null=True)

    last_visit_date = models.DateField(
        verbose_name='What was the date of patient\'s last visit?',
        validators=[date_not_future, ],)

    last_visit_facility = models.CharField(
        verbose_name='What was the facility of the patient\'s last visit',
        choices=FACILITY,
        max_length=40,)

    last_visit_facility_other = OtherCharField()

    ltfu_criteria_met = models.CharField(
        verbose_name='Criteria met for loss to follow up',
        choices=LTFU_CRITERIA,
        max_length=50,
        blank=True,
        null=True)

    patient_relocated = models.CharField(
        verbose_name='Has the patient relocated?',
        max_length=3,
        choices=YES_NO,)

    new_facility_name = models.CharField(
        verbose_name='If relocated, patient\'s NEW facility name',
        max_length=30,
        blank=True,
        null=True,)

    new_facility_type = models.CharField(
        verbose_name='If relocated, patient\'s NEW facility type',
        choices=FACILITY_TYPE,
        max_length=30,
        blank=True,
        null=True,)

    exit_hiv_status = models.CharField(
        verbose_name='What was patient\'s HIV status at exit?',
        choices=POS_NEG_UNKNOWN_MISSING,
        max_length=10,)

    latest_hiv_test_known = models.CharField(
        verbose_name='Is the latest HIV test date known for the patient?',
        choices=YES_NO,
        max_length=3,)

    hiv_test_date = models.DateField(
        verbose_name='If yes, please enter date of HIV test',
        blank=True,
        null=True,)

    hiv_test_date_estimated = models.CharField(
        verbose_name='Is the HIV test date estimated?',
        choices=YES_NO,
        max_length=3,
        blank=True,
        null=True,)

    hiv_test_date_estimation = models.CharField(
        verbose_name='Which part of the date was estimated, if any?',
        choices=DATE_ESTIMATION,
        max_length=15,
        blank=True,
        null=True
    )

    review_flag = models.CharField(
        verbose_name='Flag for physician review',
        choices=YES_NO,
        max_length=3,)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.consent_version = None
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'potlako_prn'
        verbose_name = 'Subject off Study'
        verbose_name_plural = 'Subject Off Study'
