#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'


    credit_limit = fields.Float(
        string="Credid Limit",
        digits=(12,2),
        help="Credit limit for rate"
    )

