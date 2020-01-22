from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.managers import SubjectIdentifierManager
from edc_search.model_mixins import SearchSlugModelMixin

from edc_action_item.model_mixins.action_model_mixin import ActionModelMixin

from .death_report_model_mixin import DeathReportModelMixin


class DeathReport(DeathReportModelMixin, ActionModelMixin,
                          SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'PD'

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,)

    natural_key.dependencies = ['sites.Site']

    class Meta:
        app_label = 'potlako_prn'
        verbose_name = 'Death Report'
