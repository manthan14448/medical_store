from odoo import fields, models, _


class CancelDelivery(models.TransientModel):
    _name = 'cancel.delivery'

    delivery_id = fields.Many2one('stock.picking', string='delivery')
    cancelreason = fields.Char(string='Cancel Reason')

    def action_done(self):
        records = self.env['stock.picking'].browse(self.delivery_id.id)
        for rec in records:
            rec.write({'cancelreason': self.cancelreason, 'state': 'cancel'})
