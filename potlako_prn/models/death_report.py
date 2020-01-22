from edc_action_item.model_mixins import ActionModelMixin
from edc_base.sites.managers import CurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager

from ..action_items import DEATH_REPORT_ACTION


class DeathReport(SiteModelMixin, ActionModelMixin, BaseUuidModel):

    action_name = DEATH_REPORT_ACTION

    tracking_identifier = 'DR'

    on_site = CurrentSiteManager()

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,)

    natural_key.dependencies = ['sites.Site']

    class Meta:
        app_label = 'potlako_prn'
        verbose_name = 'Death Report'
