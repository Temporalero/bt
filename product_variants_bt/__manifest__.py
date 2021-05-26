#!/usr/bin/env python3
# -*- coding: utf-8 -*-

{
    'name': "Product Variants Bt",
    'version': "14.0.1",
    'author': "Kewitz Colina",
    'website': "https://github.com/colinak",
    'summary': "products variants",
    'sequence': 10,
    'description': "Variantes de Productos",
    'category': "mail",
    'depends': [
        'base',
        'product',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_brand_view.xml',
        'views/product_season_view.xml',
        'views/product_style_view.xml',
        'views/product_last_view.xml',
        'views/product_base_color_view.xml',
        'views/product_base_finish_view.xml',
        'views/product_soles_view.xml',
        'views/product_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}



