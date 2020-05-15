from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_UNKNOWN

from ..choices import COMPONENTS_RECEIVED, FACILITY, FACILITY_TYPE, DATE_ESTIMATION
from ..choices import LTFU_CRITERIA, POS_NEG_UNKNOWN_MISSING, TREATMENT_INTENT


class OffStudyMixin(models.Model):

    general_comments = models.TextField(
        verbose_name='Any general comments about patient exit?',
        max_length=150,)

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

    components_rec = models.CharField(
        verbose_name='Potlako components received (or potentially received)',
        choices=COMPONENTS_RECEIVED,
        max_length=50,)

    components_rec_other = OtherCharField(
        verbose_name='Other Potlako component received:',
        max_length=50,)

    cancer_treatment_rec = models.CharField(
        verbose_name='Was any cancer specific treatment received?',
        choices=YES_NO_UNKNOWN,
        max_length=7,
        help_text='(Example: radiation, surgery (beyond biopsy), chemotherapy,'
                  ' ART for KS, esophageal stenting)',)

    treatment_intent = models.CharField(
        verbose_name='At time of exit, what was treatment intent? ',
        choices=TREATMENT_INTENT,
        max_length=10,)

    date_therapy_started = models.DateField(
        verbose_name='Date started cancer specific therapy',
        validators=[date_not_future, ],
        blank=True,
        null=True,)

    class Meta:
        abstract = True
