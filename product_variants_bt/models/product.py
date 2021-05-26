#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product'


    # type = fields.Selection(
        # [
            # ('consu', 'Consumable'),
            # ('service', 'Service'),
            # ('product', 'Storable')
        # ],
        # string='Product Type',
        # default='product',
        # required=True,
        # help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
             # 'A consumable product is a product for which stock is not managed.\n'
             # 'A service is a non-material product you provide.')
    product_line = fields.Selection(
        [
            ('accessories','Accessories'),
            ('purse','Purse'),
            ('footwear','Footwear'),
            ('perfumes','Perfumes'),
            ('clothing','Clothing'),
        ],
        string="Product Line",
        required=True,
        help="Product Line"
    )
    classification = fields.Char(
        string="Classification"
    )
    brand_id = fields.Many2one(
        'product.brand',
        string="Make",
        help="Manufacturers"
    )
    season_id = fields.Many2one(
        'product.season',
        string="Season",
        help="Season in which the product was launched"
    )
    last_id = fields.Many2one(
        'product.last',
        string="Last"
    )
    style_id = fields.Many2one(
        'product.style',
        string="Style"
    )
    sole_id = fields.Many2one(
        'product.sole',
        string="Sole"
    )
    base_color_id = fields.Many2one(
        'product.base.color',
        string="Base Color"
    )
    base_finish_id = fields.Many2one(
        'product.base.finish',
        string="Base finish"
    )

