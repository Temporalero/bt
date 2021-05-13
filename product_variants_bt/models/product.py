#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product'

    brand_id = fields.Many2one(
        'product.brand',
        string="Make",
        help="Manufacturers"
    )

