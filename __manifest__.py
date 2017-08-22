# -*- coding: utf-8 -*-
{
    'name': "Kwitansi",

    'summary': """
       Kwitansi Indoguna""",

    'description': """
        Kwitansi Indoguna
    """,

    'author': "Indoguna Utama. Andy Utomo",
    'website': "http://www.indoguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Report',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}