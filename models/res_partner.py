# -*- coding: utf-8 -*-
from odoo import fields, models
 

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    Rank = fields.Many2one("hospital.doctor.rank",name="Doctor Rank", tracking=True)
    premium = fields.Boolean('premium')
    images_ids = fields.Many2many('doctor.image','doctor_id', string='images')
    expertIn = fields.Many2many('product.public.category', string="Expert In", tracking=True)

    def _read_out__doctor_image(self):
        return self.image_1920

class HospitalDoctorRank(models.Model):
    _name = 'hospital.doctor.rank'
    _description = 'Doctor Rank'

    name = fields.Char(string="Doctor Rank", required=True)
    note = fields.Text(string=" ", help="A short text for Rank Information")

class HospitaDoctorImage(models.Model):
    _name = 'doctor.image'
    _description = 'Doctor Images'

    doctor_id = fields.Many2one('res.partner', string='doctor')
    images = fields.Binary('images')
