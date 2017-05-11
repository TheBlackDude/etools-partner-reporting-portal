from __future__ import unicode_literals

from model_utils import Choices


CSO_TYPES = Choices(
    ('International', 'International', 'International'),
    ('National', 'National', 'National'),
    ('CBO', 'CBO', 'Community Based Organization'),
    ('AI', 'AI', 'Academic Institution'),
)

PARTNER_TYPE = Choices(
    ('B/M', 'bilateral_multilateral', 'Bilateral / Multilateral'),
    ('CSO', 'civil_society_org', 'Civil Society Organization'),
    ('Gov', 'government', 'Government'),
    ('UNA', 'un_agency', 'UN Agency')
)

SHARED_PARTNER_TYPE = Choices(
    ('No', 'no', 'No'),
    ('UND', 'UNDP', 'with UNDP'),
    ('UNF', 'UNFPA', 'with UNFPA'),
    ('U&U', 'UNDP_UNFPA', 'with UNDP & UNFPA'),
)

INTERVENTION_TYPES = Choices(
    ('PD', 'PD', 'Programme Document'),
    ('SHP', 'SHPD', 'Simplified Humanitarian Programme Document'),
    ('SSF', 'SSFA', u'SSFA TOR'),
)

INTERVENTION_STATUS = Choices(
    ("Dra", "draft", "Draft"),
    ("Act", "active", "Active"),
    ("Imp", "implemented", "Implemented"),
    ("Sus", "suspended", "Suspended"),
    ("Ter", "terminated", "Terminated"),
    ("Can", "cancelled", "Cancelled"),
)

INDICATOR_REPORT_STATUS = Choices(
    ('OT', 'ontrack', 'On Track'),
    ('Con', 'constrained', 'Constrained'),
    ('NP', 'noprogress', 'No Progress'),
    ('TM', 'targetmet', 'Target Met')
)