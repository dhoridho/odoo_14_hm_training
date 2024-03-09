# -*- coding: utf-8 -*-
# Brief descrition about the module
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software Desc""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends' : ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/seq_data.xml',
        'views/patient_view.xml',
        'views/patient_gender_view.xml',
        'views/kids_view.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
