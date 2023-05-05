# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(selection_add=[('cod', 'COD')], ondelete={'cod': 'set default'})

    @api.depends('code')
    def _compute_view_configuration_fields(self):
        super()._compute_view_configuration_fields()
        self.filtered(lambda p: p.code == 'cod').show_credentials_page = False

    def _compute_feature_support_fields(self):
        super()._compute_feature_support_fields()
        self.filtered(lambda p: p.code == 'cod').update({
            'support_fees': True,
            'support_manual_capture': True,
            'support_refund': 'partial',
            'support_tokenization': True,
        })
