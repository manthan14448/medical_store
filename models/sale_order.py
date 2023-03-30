from odoo import fields, models,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    delivery_status = fields.Selection(default='full',readonly=False)

    def action_confirm(self):
        rec = super().action_confirm()
        breakpoint()
        return rec
