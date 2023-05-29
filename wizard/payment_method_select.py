# -*- coding: utf-8 -*-
from odoo import fields, models, _


class PaymentMethodSelect.py(models.TransientModel):
    _name = 'payment.method.select'
    _description = 'Payment Method Select'

    invoice_id = fields.Many2one('stock.picking', string='delivery')
    cancelreason = fields.Char(string='Cancel Reason')

    def action_done(self):
        records = self.env['stock.picking'].browse(self.delivery_id.id)
        for rec in records:
            rec.write({'cancelreason': self.cancelreason, 'state': 'cancel'})
