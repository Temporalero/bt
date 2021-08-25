#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.onchange('expected_date')
    def _onchange_commitment_date(self):
        today = fields.Datetime.now()
        expired_date = fields.Datetime.from_string(today) + relativedelta(months=1)
        self.commitment_date = expired_date

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        total_balance = self.env['account.move'].search([
            ('partner_id', '=', res.partner_id.id),
            ('amount_residual_signed', '>', 0),
        ])
        amount = 0
        credit = 0
        if res.amount_total > res.partner_id.credit_limit:
            raise UserError('El Pedido Supera el Limite de Credito del Cliente')
        elif total_balance != '' or total_balance != False or total_balance != None:
            for balance in total_balance:
                amount += balance.amount_residual_signed
            credit = res.partner_id.credit_limit - amount
            if res.amount_total > credit:
                raise UserError('El Pedido Supera el Limite de Credito del Cliente')

        return res


    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        amount = 0
        credit = 0
        partner = None
        if vals.get('partner_id'):
            partner_id = vals.get('partner_id')
            partner = self.env['res.partner'].browse([partner_id])
            total_balance = self.env['account.move'].search([
                ('partner_id', '=', partner_id),
                ('amount_residual_signed', '>', 0),
            ])
            if self.amount_total > partner.credit_limit:
                raise UserError('El Pedido Supera el Limite de Credito del Cliente')
            elif total_balance != '' or total_balance != False or total_balance != None:
                for balance in total_balance:
                    amount += balance.amount_residual_signed
                credit = partner.credit_limit - amount
                if self.amount_total > credit:
                    raise UserError('El Pedido Supera el Limite de Credito del Cliente')
        else:
            total_balance = self.env['account.move'].search([
                ('partner_id', '=', self.partner_id.id),
                ('amount_residual_signed', '>', 0),
            ])
            if self.amount_total > self.partner_id.credit_limit:
                raise UserError('El Pedido Supera el Limite de Credito del Cliente')
            elif total_balance != '' or total_balance != False or total_balance != None:
                for balance in total_balance:
                    amount += balance.amount_residual_signed
                credit = self.partner_id.credit_limit - amount
                if self.amount_total > credit:
                    raise UserError('El Pedido Supera el Limite de Credito del Cliente')

        return res
