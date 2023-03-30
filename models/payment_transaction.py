
from odoo import fields, models


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    state = fields.Selection(selection_add=[('delivery', 'Delivery')], ondelete={'delivery': 'set default'})
