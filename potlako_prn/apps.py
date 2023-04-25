from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = 'potlako_prn'
    verbose_name = 'Potlako Plus PRN'
    admin_site_name = 'potlako_prn_admin'

    def ready(self):
        from .models import death_report_on_post_save


if settings.APP_NAME == 'potlako_prn':
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_appointment.appointment_config import AppointmentConfig
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_visit_tracking.apps import (
        AppConfig as BaseEdcVisitTrackingAppConfig)
    from edc_sms.apps import AppConfig as BaseEdcSmsAppConfig

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        apply_community_filter = True
        send_sms_reminders = True
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='potlako_subject.subjectvisit')
        ]

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'potlako_subject': (
                'subject_visit', 'potlako_subject.subjectvisit')}

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}

    class EdcSmsAppConfig(BaseEdcSmsAppConfig):
        locator_model = 'potlako_subject.subjectlocator'
        consent_model = 'potlako_subject.subjectconsent'
        sms_model = 'potlako_subject.sms'
