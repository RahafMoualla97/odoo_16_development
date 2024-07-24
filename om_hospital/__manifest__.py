# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': 10,
    'description': """
Hospital Management Software""",
    'category': 'Productivity',
    'author' : 'Rahaf Moualla',
    'depends' : ['sale', 'mail', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/appointment_report_view.xml',
        'wizard/all_patient_report_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',
        'views/sale.xml',
        'views/partner.xml',
        'reports/report.xml',
        'reports/inherit_qweb_template.xml',
        'reports/patient_card_template.xml',
        'reports/custom_layout_template.xml',
        'reports/all_patient_list.xml',
        
        ],
    'assets': {
        'web.report_assets_common': [
            'om_hospital/static/src/scss/**/*',
            ],
        },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
