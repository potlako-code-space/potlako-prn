from edc_constants.constants import OTHER, NONE
from edc_list_data import PreloadData

list_data = {
    'potlako_prn.componentsreceived': [
        ('potlako+_iec_material', 'Potlako+ IEC material'),
        ('public_campaign',
         'Public campaign'),
        ('community_leader_info',
         'information from community leader'),
        ('group_teaching',
         'Group teaching'),
        (NONE, 'None'),
        (OTHER, 'Other (specify)'),
    ],
}

preload_data = PreloadData(
    list_data=list_data)
