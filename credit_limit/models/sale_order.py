#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)

        return res


    def write(self, vals):
        res = super(SaleOrder, self).write(vals)

        return res
