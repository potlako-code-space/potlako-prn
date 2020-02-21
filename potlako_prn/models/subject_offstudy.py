from django.apps import apps as django_apps
from django.db import models
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future, datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import (
    date_not_before_study_start, datetime_not_before_study_start)
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from ..action_items import SUBJECT_OFFSTUDY_ACTION
from ..choices import REASON_FOR_EXIT
from potlako_prn.models.offstudy_model_mixin import OffStudyMixin


class SubjectOffStudy(
        OffScheduleModelMixin, ActionModelMixin, OffStudyMixin, BaseUuidModel):

    action_name = SUBJECT_OFFSTUDY_ACTION

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

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def take_off_schedule(self):
        onschedule_model = django_apps.get_model(
            'potlako_subject.onschedule')
        try:
            onschedule_obj = onschedule_model.objects.get(
                subject_identifier=self.subject_identifier)
        except onschedule_model.DoesNotExist:
            pass
        else:
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                onschedule_model=onschedule_model._meta.label_lower)
            schedule.take_off_schedule(offschedule_model_obj=self)

    class Meta:
        app_label = 'potlako_prn'
        verbose_name = 'Subject off Study'
        verbose_name_plural = 'Subject Off Study'
