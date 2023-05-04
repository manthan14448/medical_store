from odoo import models


class DoctorDetails(models.Model):
    _name = "doctor.details"
    _description = 'use for fetch doctor detail from user'

    def _find_doctor_near_by(self, product_cat_id):
        return self.env['res.partner'].sudo().search_read([
                ('expertIn', 'in', product_cat_id), ('function', '=', 'Doctor')],
                ['id', 'name', 'Rank', 'phone', 'email', 'contact_address', 'image_medium', 'website'])
