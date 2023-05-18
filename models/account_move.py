# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    #created button on account called Cash Payment when click it create paymenet mode in cash
    def action_register_cash_payment(self):
        context = {
            'active_model': 'account.move',
            'active_ids':self.ids[0],
        }
        payment_register = self.env['account.payment.register'].with_context(context).create({
                'journal_id': self.env['account.journal'].search([('type', '=', 'cash')], limit=1).id,
            })
        payment_register.action_create_payments()

class AccountJournal(models.Model):
    _inherit = "account.journal"

    type = fields.Selection(
        selection_add=[('cod', 'COD')], ondelete={'cod': 'cascade'})
