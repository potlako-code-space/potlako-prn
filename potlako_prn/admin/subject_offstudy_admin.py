from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import potlako_prn_admin
from ..forms import SubjectOffStudyForm
from ..models import SubjectOffStudy
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectOffStudy, site=potlako_prn_admin)
class SubjectOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectOffStudyForm

    fieldsets = (
        ('Fields to be completed by Potlako Research Assistant (Deaths/LTFU)',
            {
                'fields': ('subject_identifier',
                           'report_datetime',
                           'offstudy_date',
                           'reason',
                           'last_visit_date',
                           'last_visit_facility',
                           'last_visit_facility_other',
                           'ltfu_criteria_met',
                           'patient_relocated',
                           'new_facility_name',
                           'new_facility_type',
                           'exit_hiv_status',
                           'latest_hiv_test_known',
                           'hiv_test_date',
                           'hiv_test_date_estimated',
                           'hiv_test_date_estimation',
                           'review_flag',
                           'general_comments',),
            }),
        ('Fields to be completed by Physician (Final status)', {
            'fields': ('components_rec',
                       'components_rec_other',
                       'cancer_treatment_rec',
                       'treatment_intent',
                       'date_therapy_started'),
        }),
        audit_fieldset_tuple)

    radio_fields = {'reason': admin.VERTICAL,
                    'last_visit_facility': admin.VERTICAL,
                    'ltfu_criteria_met': admin.VERTICAL,
                    'patient_relocated': admin.VERTICAL,
                    'new_facility_type': admin.VERTICAL,
                    'exit_hiv_status': admin.VERTICAL,
                    'latest_hiv_test_known': admin.VERTICAL,
                    'hiv_test_date_estimated': admin.VERTICAL,
                    'hiv_test_date_estimation': admin.VERTICAL,
                    'review_flag': admin.VERTICAL,
                    'components_rec': admin.VERTICAL,
                    'cancer_treatment_rec': admin.VERTICAL,
                    'treatment_intent': admin.VERTICAL, }

    search_fields = ('subject_identifier',)

    list_display = ('subject_identifier', 'offstudy_date',)
