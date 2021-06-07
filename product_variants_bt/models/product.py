#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
import random
import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product'



    @api.depends('brand_id', 'default_code')
    def _compute_reference(self):
        make = self.brand_id
        product = False
        if make and not self.default_code:
            while product == False:
                number = random.randint(100000, 999999)
                code = str(make.abbreviation) + str(number)
                product = self.env['product.template'].search(
                    [('default_code', '=', code)]
                )
                if not product:
                    self.default_code = code
                else:
                    product = False



    default_code = fields.Char(
        string="Referencia Interna",
        compute=_compute_reference
    )
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
    classification_id = fields.Many2one(
        'product.classification',
        ondelete='restrict',
        string="Classification"
    )
    brand_id = fields.Many2one(
        'product.brand',
        string="Make",
        required=True,
        ondelete='restrict',
        help="Manufacturers"
    )
    season_id = fields.Many2one(
        'product.season',
        string="Season",
        ondelete='restrict',
        help="Season in which the product was launched"
    )
    last_id = fields.Many2one(
        'product.last',
        string="Last",
        ondelete='restrict'
    )
    style_id = fields.Many2one(
        'product.style',
        string="Style",
        ondelete='restrict'
    )
    sole_id = fields.Many2one(
        'product.sole',
        string="Sole",
        ondelete='restrict'
    )
    base_color_id = fields.Many2one(
        'product.color',
        string="Base Color",
        ondelete='restrict'
    )
    base_finish_id = fields.Many2one(
        'product.base.finish',
        string="Base finish",
        ondelete='restrict'
    )
    family_id = fields.Many2one(
        'product.family',
        string="Family",
        required=True,
        ondelete='restrict'
    )
    edge_color_id = fields.Many2one(
        'product.color',
        string="Edge Color",
        ondelete='restrict'
    )
    stencil_id = fields.Many2one(
        'product.stencil',
        string="Template",
        ondelete='restrict'
    )
    height = fields.Integer(
        string="Height"
    )
    logo_color = fields.Selection(
        [('golder', 'Golder'), ('silver', 'Silver')],
        string="Logo Color",
        help="Template Logo Color"
    )
    lining_id = fields.Many2one(
        'product.lining',
        string="Linig",
        ondelete='restrict'
    )
    upper_id = fields.Many2one(
        'product.upper',
        string="Upper",
        ondelete='restrict'
    )


