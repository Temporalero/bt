#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Manufacturers'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string="Make", required=True)
    image = fields.Image(string="Logo", max_width=128, max_height=128)
    abbreviation = fields.Char(string="Abbreviation", required=True, size=5)
    active = fields.Boolean(string="Active.?", default=True)


    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la marca que intenta registrar ya existe.'),
        ('abbre_uniq', 'unique (abbreviation)',
        'La Abreviatura de la marca que intenta registrar ya existe.'),
    ]

