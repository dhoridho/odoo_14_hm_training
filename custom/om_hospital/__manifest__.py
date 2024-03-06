# Brief descrition about the module

# -*- coding: utf-8 -*-
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
        'views/patient.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}