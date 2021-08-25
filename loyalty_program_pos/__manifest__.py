#!/usr/bin/env python3
# -*- coding: utf-8 -*-

{
    'name': "Loyalty Program Pos Bt",
    'version': "14.0.1",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'summary': "products variants",
    'sequence': 10,
    'description': "Loyalty Program Pos",
    'category': "Point of Sale",
    'depends': [
        'base',
        'point_of_sale',
        # 'loyalty_program_pos',
        # 'pos_loyalty',

    ],
    'data': [
        # 'security/base_finish/ir.model.access.csv',
        'views/res_partner_view.xml',
    ],
    'demo': [],
    'qweb': [
        'static/src/xml/Screens/ClientListScreen/ClientListScreen.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False

}

