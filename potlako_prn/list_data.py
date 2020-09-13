from edc_constants.constants import OTHER, NONE
from edc_list_data import PreloadData

list_data = {
    'potlako_prn.componentsreceived': [
        ('provider_edication', 'Provider education'),
        ('diagnostic_facilitation', 'Diagnostic facilitation (pre-biopsy/test)'),
        ('access_to_diagnostic_results',
         'Access to diagnostic results (e.g. histology)'),
        ('cancer_treatment_facilitation_post_test_results',
         'Cancer treatment facilitation post-test results'),
        ('retention_or_completion_of_cancer_treatment',
         'Retention or completion of cancer treatment'),
        (NONE, 'None'),
        (OTHER, 'Other (specify)'),
    ],
}


preload_data = PreloadData(
    list_data=list_data)
