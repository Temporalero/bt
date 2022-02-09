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
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la Temporada que intenta registrar ya existe.'),
    ]


class Productlast(models.Model):
    _name = 'product.last'
    _description = 'Lasts'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la Horma que intenta registrar ya existe.'),
    ]


class ProductStyle(models.Model):
    _name = 'product.style'
    _description = 'Styles'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre del Estilo que intenta registrar ya existe.'),
    ]


class ProductSole(models.Model):
    _name = 'product.sole'
    _description = 'Soles'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la Suela que intenta registrar ya existe.'),
    ]


class ProductColor(models.Model):
    _name = 'product.color'
    _description = 'Colors'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre del Color que intenta registrar ya existe.'),
    ]


class ProductBaseFinish(models.Model):
    _name = 'product.base.finish'
    _description = 'Base Finish'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre del Acabado Base que intenta registrar ya existe.'),
    ]


class ProductNivel(models.Model):
    _name = 'product.level'
    _description = 'Product Level'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre del Nivel que intenta registrar ya existe.'),
    ]


class ProductFamily(models.Model):
    _name = 'product.family'
    _description = 'Product Family'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la Familia que intenta registrar ya existe.'),
    ]


class ProductStencil(models.Model):
    _name = 'product.stencil'
    _description = 'Product Template'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la Plantilla que intenta registrar ya existe.'),
    ]


class ProductLinig(models.Model):
    _name = 'product.lining'
    _description = 'Product Linig'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre del Recubrimiento que intenta registrar ya existe.'),
    ]


class ProductUpper(models.Model):
    _name = 'product.upper'
    _description = 'Product Upper'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El Nombre que intenta registrar ya existe.'),
    ]


class ProductGroup(models.Model):
    _name = 'product.group'
    _description = 'Product Group'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la Familia que intenta registrar ya existe.'),
    ]


class ProductConcept(models.Model):
    _name = 'product.concept'
    _description = 'Product Concept'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(
        string="Name",
        required=True
    )
    group_id = fields.Many2one(
        'product.group',
        string="Grupo Concepto",
    )

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
        'El nombre de la Familia que intenta registrar ya existe.'),
    ]
