from edc_action_item import Action, HIGH_PRIORITY

SUBJECT_OFFSTUDY_ACTION = 'submit-subject-offstudy'


class SubjectOffStudyAction(Action):
    name = SUBJECT_OFFSTUDY_ACTION
    display_name = 'Submit Subject Offstudy'
    reference_model = 'potlako_prn.subjectoffstudy'
    show_link_to_changelist = True
    show_link_to_add = True
    admin_site_name = 'potlako_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True
