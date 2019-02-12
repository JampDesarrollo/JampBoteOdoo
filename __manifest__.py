# -*- coding: utf-8 -*-
{
    'name': "bote",

    'summary': """Manejar el bote de un txoko""",

    'description': """Este modulo se va a utilizar para manjear 
    las entradas y salidas de dinero de un txoko""",

    'author': "Jamp",
    'website': "http://www.jamp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/gastos.xml',
        'views/users.xml',
        'reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}