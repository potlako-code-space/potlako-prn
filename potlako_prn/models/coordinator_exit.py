from django.apps import apps as django_apps
from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future, date_is_future, datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO, YES_NO_UNKNOWN
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import datetime_not_before_study_start

from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from ..action_items import COORDINATOR_EXIT_ACTION
from ..choices import CANCER_STAGES, TREATMENT_INTENT
from ..choices import CANCER_TREATMENT, DATE_ESTIMATION, DISPOSITION
from .list_models import ComponentsReceived


class CoordinatorExit(OffScheduleModelMixin, ActionModelMixin, BaseUuidModel):

    action_name = COORDINATOR_EXIT_ACTION

    tracking_identifier_prefix = 'CE'

    report_datetime = models.DateTimeField(
        verbose_name='Report datetime',
        validators=[datetime_not_before_study_start, datetime_not_future],
        null=True,
        default=get_utcnow,)

    components_rec = models.ManyToManyField(
        ComponentsReceived,
        verbose_name='Potlako components received (or potentially received)',)

    components_rec_other = OtherCharField(
        verbose_name='Other Potlako component received:',
        max_length=50,)

    cancer_stage = models.CharField(
        verbose_name='If cancer, stage of cancer',
        choices=CANCER_STAGES,
        max_length=20,
        blank=True,
        null=True)

    cancer_treatment_rec = models.CharField(
        verbose_name='Was any cancer specific treatment received?',
        choices=YES_NO_UNKNOWN,
        max_length=7,
        help_text='(Example: radiation, surgery (beyond biopsy), chemotherapy,'
                  ' ART for KS, esophageal stenting)',)

    cancer_treatment = models.CharField(
        verbose_name='What specific cancer treatment was received?',
        choices=CANCER_TREATMENT,
        max_length=25,
        blank=True,
        null=True,)

    cancer_treatment_other = OtherCharField()

    date_therapy_started = models.DateField(
        verbose_name='Date started cancer specific therapy',
        validators=[date_not_future, ],
        blank=True,
        null=True,)

    date_therapy_started_estimated = models.CharField(
        verbose_name='Is the above therapy start date estimated?',
        choices=YES_NO,
        max_length=3,
        blank=True,
        null=True,)

    date_therapy_started_estimation = models.CharField(
        verbose_name='If yes, which part of the therapy start date was estimated?',
        choices=DATE_ESTIMATION,
        max_length=15,
        blank=True,
        null=True,)

    treatment_intent = models.CharField(
        verbose_name='At time of exit, what was treatment intent?',
        choices=TREATMENT_INTENT,
        max_length=10,)

    patient_disposition = models.CharField(
        verbose_name='What is the patient\'s final disposition?',
        choices=DISPOSITION,
        default='exit',
        max_length=15)

    patient_contact_date = models.DateField(
        verbose_name='If call/visit above, date for patient call/visit ',
        validators=[date_is_future, ],
        blank=True,
        null=True,)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier}'

    def take_off_schedule(self):
        on_schedule = django_apps.get_model(
            'potlako_subject.onschedule')

        _, schedule = site_visit_schedules.get_by_onschedule_model(
            onschedule_model=on_schedule._meta.label_lower)
        schedule.take_off_schedule(offschedule_model_obj=self)

    def save(self, *args, **kwargs):
        self.consent_version = None
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'potlako_prn'
        verbose_name = 'Coordinator Exit'
        verbose_name_plural = 'Coordinator Exit'
