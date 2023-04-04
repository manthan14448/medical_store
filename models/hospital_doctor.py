from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Many2one('res.partner', string='Doctor Name')
    Rank = fields.Many2one("hospital.doctor.rank",name="Doctor Rank", tracking=True)
    image_1920 = fields.Image("Image", related='name.image_1920')  # required=True
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], string="Gender")
    expertIn = fields.Many2many('product.public.category', string="Expert In", tracking=True)

class HospitalDoctorrANK(models.Model):
    _name = 'hospital.doctor.rank'
    _description = 'Doctor Rank'

    name = fields.Char(string="Doctor Rank",required=True)
    note = fields.Text(string=" ", help="A short text for Rank Information")

