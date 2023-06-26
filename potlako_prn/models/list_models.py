from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class ComponentsReceived(ListModelMixin, BaseUuidModel):
    pass

class TreatmentReceived(ListModelMixin,BaseUuidModel):
    pass
