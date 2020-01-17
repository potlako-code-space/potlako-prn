from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'potlako_prn'
    verbose_name = 'Potlako Plus PRN'
    admin_site_name = 'potlako_prn_admin'
