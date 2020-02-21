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
                           'death_date',
                           'cause_of_death',
                           'place_of_death',
                           'facility_patient_died',
                           'death_info_source',
                           'info_source_other',
                           'ltfu_criteria_met',
                           'new_kgotla_res',
                           'new_village_res',
                           'new_district_res',
                           'new_facility_name',
                           'new_facility_type',
                           'exit_hiv_status',
                           'latest_hiv_test_known',
                           'hiv_test_date',
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
                    'place_of_death': admin.VERTICAL,
                    'facility_patient_died': admin.VERTICAL,
                    'death_info_source': admin.VERTICAL,
                    'ltfu_criteria_met': admin.VERTICAL,
                    'new_district_res': admin.VERTICAL,
                    'new_facility_type': admin.VERTICAL,
                    'exit_hiv_status': admin.VERTICAL,
                    'latest_hiv_test_known': admin.VERTICAL,
                    'review_flag': admin.VERTICAL,
                    'components_rec': admin.VERTICAL,
                    'cancer_treatment_rec': admin.VERTICAL,
                    'treatment_intent': admin.VERTICAL, }

    search_fields = ('subject_identifier',)

    list_display = ('subject_identifier', 'offstudy_date',)
