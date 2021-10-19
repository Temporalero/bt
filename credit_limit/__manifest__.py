#!/usr/bin/env python3
# -*- coding: utf-8 -*-

{
    'name': "Credit limit",
    'version': "14.0.1",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'summary': "Credit limit in Price List",
    'sequence': 10,
    'description': "Credit limit in Price List",
    'category': "Sales",
    'depends': [
        'base',
        'product',
        'sale'
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}

