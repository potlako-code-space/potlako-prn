from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'potlako_prn'
    verbose_name = 'Potlako Plus PRN'
    admin_site_name = 'potlako_prn_admin'

    def ready(self):
        from .models import death_report_on_post_save
        from .models import subject_offstudy_on_post_save
