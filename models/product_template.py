# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    medical_condition = fields.Char(string="Couse")
