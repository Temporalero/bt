#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_affiliated = fields.Boolean(
        string="Is Affiliated?",
        default=False
    )
    type_membership = fields.Selection(
        [
            ('silver', 'Silver'),
            ('gold', 'Gold'),
            ('platinum', 'Platinum'),
        ],
        string="Type Menbership"
    )

# loyalty.program
