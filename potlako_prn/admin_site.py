from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Potlako PRN'
    site_header = 'Potlako PRN'
    index_title = 'Potlako PRN'
    site_url = '/administration/'


potlako_prn_admin = AdminSite(name='potlako_prn_admin')
