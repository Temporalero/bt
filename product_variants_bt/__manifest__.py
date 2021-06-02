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
        'security/base_finish/ir.model.access.csv',
        'security/brand/ir.model.access.csv',
        'security/classification/ir.model.access.csv',
        'security/color/ir.model.access.csv',
        'security/family/ir.model.access.csv',
        'security/last/ir.model.access.csv',
        'security/lining/ir.model.access.csv',
        'security/season/ir.model.access.csv',
        'security/sole/ir.model.access.csv',
        'security/stencil/ir.model.access.csv',
        'security/style/ir.model.access.csv',
        'security/upper/ir.model.access.csv',
        'views/product_base_finish_view.xml',
        'views/product_brand_view.xml',
        'views/product_classification_view.xml',
        'views/product_colors_view.xml',
        'views/product_family_view.xml',
        'views/product_last_view.xml',
        'views/product_lining_view.xml',
        'views/product_season_view.xml',
        'views/product_soles_view.xml',
        'views/product_stencil_view.xml',
        'views/product_style_view.xml',
        'views/product_upper_view.xml',
        'views/product_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
