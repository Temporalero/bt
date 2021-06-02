#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class ProductSeason(models.Model):
    _name = 'product.season'
    _description = 'Seasons'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class Productlast(models.Model):
    _name = 'product.last'
    _description = 'Lasts'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductStyle(models.Model):
    _name = 'product.style'
    _description = 'Styles'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductSole(models.Model):
    _name = 'product.sole'
    _description = 'Soles'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductColor(models.Model):
    _name = 'product.color'
    _description = 'Colors'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductBaseFinish(models.Model):
    _name = 'product.base.finish'
    _description = 'Base Finish'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductClassification(models.Model):
    _name = 'product.classification'
    _description = 'Product Classification'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductFamily(models.Model):
    _name = 'product.family'
    _description = 'Product Family'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductStencil(models.Model):
    _name = 'product.stencil'
    _description = 'Product Stencil'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )
    

class ProductLinig(models.Model):
    _name = 'product.lining'
    _description = 'Product Linig'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )


class ProductUpper(models.Model):
    _name = 'product.upper'
    _description = 'Product Upper'
    _rec_name = 'name'
    _order = 'name'
    
    name = fields.Char(
        string="Name"
    )
