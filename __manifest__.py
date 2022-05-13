# -*- coding: utf-8 -*-
# General configs for each Odoo Module
{
    'name': 'School',
    'version': '1.0',
    'category': 'School',
    'summary': 'School Management System',
    'description': """
        A complete school management system
    """,
    'author': 'Rodrigo Lourenço',
    'depends': [],
    'data': [
        'views/student_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'sequence': -100,
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {},
}
