from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_action_item.site_action_items import site_action_items

from ..action_items import SUBJECT_OFFSTUDY_ACTION
from .death_report import DeathReport
from .subject_offstudy import SubjectOffStudy


@receiver(post_save, weak=False, sender=DeathReport,
          dispatch_uid='death_report_on_post_save')
def death_report_on_post_save(sender, instance, raw, created, **kwargs):
    """Create Offstudy form action item after completing the
    death report model.
    """
    if not raw and created:
            trigger_action_item(SubjectOffStudy, SUBJECT_OFFSTUDY_ACTION,
                                instance.subject_identifier)


def trigger_action_item(model_cls, action_name, subject_identifier):
    action_cls = site_action_items.get(
        model_cls.action_name)
    action_item_model_cls = action_cls.action_item_model_cls()

    try:
        model_cls.objects.get(subject_identifier=subject_identifier)
    except model_cls.DoesNotExist:

        try:
            action_item_model_cls.objects.get(
                subject_identifier=subject_identifier,
                action_type__name=action_name)
        except action_item_model_cls.DoesNotExist:
            action_cls = site_action_items.get(action_name)
            action_cls(
                subject_identifier=subject_identifier)
