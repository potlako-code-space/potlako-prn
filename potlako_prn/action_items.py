from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, HIGH_PRIORITY, site_action_items


DEATH_REPORT_ACTION = 'submit-death-report'
SUBJECT_OFFSTUDY_ACTION = 'submit-subject-offstudy'


class DeathReportAction(Action):
    name = DEATH_REPORT_ACTION
    display_name = 'Submit Death Report'
    reference_model = 'potlako_prn.deathreport'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'potlako_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True

    def get_next_actions(self):
        actions = []
        potlako_deathreport_cls = django_apps.get_model(
            'potlako_prn.deathreport')

        action_item_cls = django_apps.get_model('edc_action_item.actionitem')

        subject_identifier = self.reference_model_obj.subject_identifier

        offstudy = action_item_cls.objects.filter(
            subject_identifier=subject_identifier,
            action_type__name='submit-subject-offstudy')

        try:
            potlako_deathreport_cls.objects.get(
                subject_identifier=subject_identifier)
            if not offstudy:
                actions = [SubjectOffStudyAction]
        except ObjectDoesNotExist:
            pass
        return actions


class SubjectOffStudyAction(Action):
    name = SUBJECT_OFFSTUDY_ACTION
    display_name = 'Submit Subject Offstudy'
    reference_model = 'potlako_prn.subjectoffstudy'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'potlako_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True


site_action_items.register(DeathReportAction)
site_action_items.register(SubjectOffStudyAction)
