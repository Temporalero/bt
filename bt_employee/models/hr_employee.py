#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'

    daily_salary = fields.Float(
        string="Daily Salary",
        digits=(12,2),
        help="Daily Salary Employee"
    )
    integrated_daily_wage = fields.Float(
        string="Integrated daily wage",
        digits=(12,2),
        help="Integrated daily wage Employee"
    )
    monthly_salary = fields.Float(
        string="Monthly salary",
        digits=(12,2),
        help="Monthly salary Employee"
    )
    business_name = fields.Char(
        string="Business name",
        help="Assigned business name"
    )
    attendance_bonus = fields.Float(
        string="Attendance Bonus",
        help="Attendance Bonus"
    )
    punctuality_voucher = fields.Float(
        string="Punctuality Voucher",
        help="Punctuality Voucher"
    )
    pantry_vouchers = fields.Float(
        string="Pantry Vouchers",
        help="Pantry Vouchers"
    )
    curp = fields.Char(
        string="CURP"
    )
    rfc = fields.Char(
        string="RFC"
    )
    imss_no = fields.Char(
        string="N° IMSS"
    )
    infonavit_credit_no = fields.Char(
        string="N° Credit Infonavit"
    )
    discount_factor = fields.Char(
        string="Discount Factor",
        help="Discount Factor"
    )
