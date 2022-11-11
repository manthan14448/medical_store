# -*- coding: utf-8 -*-
import string
from odoo import fields, models


class ProductPublicBodyPart(models.Model):
    _name = "product.public.body.part"
    _inherit = ["website.seo.metadata"]
    _description = "Public Body Part"
    _order = "sequence, name"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(
        help="Gives the sequence order when displaying a list of body part.")


class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    public_body_parts_ids = fields.Many2many(
        'product.public.body.part',  string='Public Body Parts', help='Public Body Parts')
    medical_condition = fields.Char(string="Couse")

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'

    name = fields.Char(string="Name", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], default='male', string="Gender")
    user_id = fields.Many2one('res.users', string='Related User')
    