#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ProductSeason(models.Model):
    _name = 'product.season'
    _description = 'Season'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class Productlast(models.Model):
    _name = 'product.last'
    _description = 'Last'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductStyle(models.Model):
    _name = 'product.style'
    _description = 'Style'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )
