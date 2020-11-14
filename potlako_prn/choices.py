from edc_constants.constants import OTHER, POS, NEG, NONE, UNKNOWN

CANCER_STAGES = (
    ('not_yet_established', 'Not yet established'),
    ('stage_0', 'Stage 0'),
    ('stage_I', 'Stage I'),
    ('stage_II', 'Stage II'),
    ('stage_III', 'Stage III'),
    ('stage_IV', 'Stage IV'),
)

CANCER_TREATMENT = (
    ('radiation', 'Radiation'),
    ('surgery', 'Surgery - Beyond biopsy'),
    ('chemotherapy', 'Chemotherapy'),
    ('art_for_ks', 'ART for KS'),
    ('esophageam_stenting', 'Esophageam stenting'),
    (OTHER, 'Other, specify')
)

CAUSE_OF_DEATH_CAT = (
    ('hiv_related', 'HIV infection or HIV related diagnosis'),
    ('cancer', 'Cancer'),
    ('cancer_related_diseases', 'Cancer related diseases'),
    ('suicide', 'Suicide'),
    ('trauma', 'Trauma/Accident'),
    ('no_info', 'No information available'),
    (OTHER, 'Other, specify'),)

COMPONENTS_RECEIVED = (
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
)

DATE_ESTIMATION = (
    ('day', 'Estimated day only'),
    ('day_month', 'Estimated day and month'),
    ('month', 'Estimated month only'),
    ('year', 'Estimate year only'),
    ('day_month_year', 'Estimated day, month and year')
)

DEATH_INFO_SOURCE = (
    ('death_certificate_review', 'Death Certificate Review'),
    ('clinician', 'Clinician'),
    ('next_of_kin1', 'Next of kin 1'),
    ('inpatient_medical_file', 'Inpatient medical file'),
    ('fam_member', 'family member (specify relationship)'),
    (OTHER, 'Other (specify)'),
)

DEATH_PLACE = (
    ('home_or_community', 'Home or in the community'),
    ('facility', 'At facility'),
    ('unknown', 'Place of death unknown')
)

DISPOSITION = (
    ('exit', 'Exit'),
)

DISTRICT = (
    ('chobe', 'Chobe - Chobe'),
    ('bobonong', 'Central - Bobonong'),
    ('boteti', 'Central - Boteti'),
    ('mahalapye', 'Central - Mahalapye'),
    ('orapa', 'Central - Orapa'),
    ('serowe_palapye', 'Central - Serowe/Palapye'),
    ('tutume', 'Central - Tutume'),
    ('CKGR', 'ghanzi - CKGR'),
    ('ghanzi', 'ghanzi - Ghanzi'),
    ('kgalagdi_north', 'Kgalagadi North'),
    ('kgalagadi_south', 'Kgalagadi South'),
    ('kgatleng', 'Kgatleng'),
    ('kweneng_east', 'Kweneng - East'),
    ('kweneng_west', 'Kweneng - West'),
    ('delta', 'north West - Delta'),
    ('ngamiland_north', 'North West - Ngamiland Nort'),
    ('ngamiland_south', 'North East - Ngamiland South'),
    ('north_east', 'North East'),
    ('barolong', 'Southern - Barolong'),
    ('ngwaketse', 'Southern - Ngwaketse'),
    ('ngwaketse_west', 'Southern - Ngwaketse West'),
)

FACILITY = (
    ('athlone_hospital', 'Athlone Hospital'),
    ('bamalete_lutheran_hospital', 'Bamalete Lutheran Hospital'),
    ('bokaa_clinic', 'Bokaa clinic'),
    ('deborah_reteif_memorial_hospital', 'Deborah. Reteif. Memorial Hospital'),
    ('goodhope_hospital', 'Goodhope Hospital'),
    ('gweta_hospital', 'Gweta Hospital'),
    ('kanye_sda_hospital', 'Kanye SDA Hospital'),
    ('lentsweletau_clinic', 'Lentsweletau clinic'),
    ('lerala_clinic', 'Lerala clinic'),
    ('letlhakeng_clinic', 'Letlhakeng clinic'),
    ('mahalapye_hospital', 'Mahalapye Hospital'),
    ('mandunyane_clinic', 'Mandunyane clinic'),
    ('manga_clinic', 'Manga clinic'),
    ('masunga_primary_hospital', 'Masunga Primary Hospital'),
    ('masunga_clinic', 'Masunga clinic'),
    ('mathangwane_clinic', 'Mathangwane clinic'),
    ('maunatlala_clinic', 'Maunatlala clinic'),
    ('metsimotlhabe_clinic', 'Metsimotlhabe clinic'),
    ('mmadianare_primary_hospital', 'Mmadinare Primary Hospital'),
    ('mmankgodi_clinic', 'Mmankgodi clinic'),
    ('mmathethe_clinic', 'Mmathethe clinic'),
    ('molapowabojang_clinic', 'Molapowabojang clinic'),
    ('nata_clinic', 'Nata clinic'),
    ('nyangagwe_hospital', 'Nyangagwe Hospital'),
    ('oodi_clinic', 'Oodi clinic'),
    ('otse_clinic', 'Otse clinic'),
    ('palapye_hospital', 'Palapye Hospital'),
    ('princess_marina_hospital', 'Princess Marina Hospital'),
    ('ramokgonami_clinic', 'Ramokgonami clinic'),
    ('scottish_livingstone_hospital', 'Scottish Livingstone Hospital'),
    ('sefophe_clinic', 'Sefophe clinic'),
    ('selibe_phikwe_hospital', 'Selibe Phikwe Hospital'),
    ('sheleketla_clinic', 'Sheleketla clinic'),
    ('shoshong_clinic', 'Shoshong clinic'),
    ('tati_siding_clinic', 'Tati Siding clinic'),
    ('thamaga_hospital', 'Thamaga Hospital'),
    (OTHER, 'Other (specify)')
)

FACILITY_TYPE = (
    ('health_post', 'health post'),
    ('primary_clinic', 'primary clinic'),
    ('primary_hospital', 'primary hospital'),
    ('secondary_hospital', 'secondary hospital'),
    ('referral_hospital', 'referral hospital')
)

HOSPITILIZATION_REASONS = (
    ('respiratory illness(unspecified)', 'Respiratory Illness(unspecified)'),
    ('respiratory illness, cxr confirmed',
     'Respiratory Illness, CXR confirmed'),
    ('respiratory illness, cxr confirmed, bacterial pathogen, specify',
     'Respiratory Illness, CXR confirmed, bacterial pathogen, specify'),
    ('respiratory illness, cxr confirmed, tb or probable tb',
     'Respiratory Illness, CXR confirmed, TB or probable TB'),
    ('diarrhea illness(unspecified)', 'Diarrhea Illness(unspecified)'),
    ('diarrhea illness, viral or bacterial pathogen, specify',
     'Diarrhea Illness, viral or bacterial pathogen, specify'),
    ('sepsis(unspecified)', 'Sepsis(unspecified)'),
    ('sepsis, pathogen specified, specify',
     'Sepsis, pathogen specified, specify'),
    ('mengitis(unspecified)', 'Mengitis(unspecified)'),
    ('mengitis, pathogen specified, specify',
     'Mengitis, pathogen specified, specify'),
    ('non-infectious reason for hospitalization, specify',
     'Non-infectious reason for hospitalization, specify'),
    (OTHER, 'Other infection, specify'),
)

LTFU_CRITERIA = (
    ('missed_visits', 'Missed visits'),
    ('attempted_calls_to_patient',
     'attempted calls to patient x 3 or 3 different days'),
    ('attempted_calls_to_next_kin1',
     'attempted calls to next of kin 1 x 3 or 3 different days'),
    ('attempted_calls_to_next_kin2',
     'attempted calls to next of kin 2 x 3 or 3 different days'),
    ('home_visit_done_unable_to_trace', 'home visit done and unable to trace'),
)

MED_RESPONSIBILITY = (
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('traditional', 'Traditional Healer'),
    ('all', 'Both Doctor or Nurse and Traditional Healer'),
    ('none', 'No known medical care received (family/friends only)'),)

PLACE_OF_DEATH = (
    ('home', 'At home or in the community'),
    ('facility', 'At facility'),
    (UNKNOWN, 'Place of death unknown'),
)

POS_NEG_UNKNOWN_MISSING = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (UNKNOWN, 'Unknown'),
)

REASON_FOR_EXIT = (
    ('death', 'Patient death'),
    ('ltfu', 'Patient lost to follow-up'),
    ('eval_complete', 'Cancer evaluation complete'),
    ('declines_further_eval',
     'Patient or clinician declines further evaluation'),
    ('patient_requests_removal', 'Patient requests removal from Potlako'),
    ('clinician_requests_removal', 'Clinician requests removal from Potlako'),
    (OTHER, 'Other (specify)'),
)

TREATMENT_INTENT = (
    ('curative', 'Curative'),
    ('palliative', 'Palliative'),
    ('uncertain', 'Uncertain'),
)
