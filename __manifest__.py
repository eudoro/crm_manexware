# -*- coding: utf-8 -*-
{
    'name': 'CRM Manexware',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 5,
    'summary': 'Leads, Opportunities, Activities',
    'description': """
The generic Odoo Customer Relationship Management
====================================================
Campos Adicionales
""",
    'author': 'Manexware S.A.',
    'website': 'http://www.manexware.com',
    'depends': ['crm',
    ],
    'data': [
        'data/crm_stage_data.xml',
        'views/crm_lead_manex_views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
