# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    #created button on account called Cash Payment when click it create paymenet mode in cash
    def is_invoice(self, include_receipts=False):
        account = super().is_invoice()
        return self  
        
    def action_register_cash_payment(self):
        context = {
            'active_model': 'account.move',
            'active_ids':self.ids[0],
        }
        payment_register = self.env['account.payment.register'].with_context(context).create({
                'journal_id': self.env['account.journal'].search([('type', '=', 'cash')], limit=1).id,
            })
        payment_register.action_create_payments()

    def direct_send_mail_to_user(self):
        self.ensure_one()
        template = self.env.ref(self._get_mail_template(), raise_if_not_found=False)
        print(template)
        # context = {
        #     'is_email':True,
                # 'composer': self.env['mail.compose.message'].create({'composition_mode': 'comment'}),
        #     'invoice_ids':self.id,
        #     'template_id': template
        # }
        invoice_send = self.env['account.invoice.send'].with_context({'active_model': 'account.move',
                                                                    'active_ids': self.ids}).create({'template_id': template.id,})
        invoice_send.composer_id.with_context(no_new_invoice=True,
                                        mail_notify_author=self.env.user.partner_id,
                                        mailing_document_based=True,
                                        )._action_send_mail()
class AccountJournal(models.Model):
    _inherit = "account.journal"

    type = fields.Selection(
        selection_add=[('cod', 'COD')], ondelete={'cod': 'cascade'})
