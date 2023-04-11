from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    # delivery_status = fields.Selection(default='full', readonly=False)
    delivery_signed_by = fields.Many2one(comodel_name='res.users', string="Delivery By", copy=False, readonly=True)

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_delivery_status(self):
        super()._compute_delivery_status()
        for order in self:
            if order.delivery_status == 'full':
                # CREATE INVOICE
                context = {
                    'active_model': 'sale.order',
                    'active_ids': order.order_line.ids,
                    'active_id': order.id,
                }
                payment = self.env['sale.advance.payment.inv'].with_context(context).create({
                    'advance_payment_method': 'delivered'
                })
                # INVOIC DONE STAGE
                payment.create_invoices()
                order.invoice_ids[0].action_post()
                # Payment.transection go to done stage
                if order.invoice_ids[0].transaction_ids:
                    order.invoice_ids[0].transaction_ids.sudo().write({'state': 'done'})
                # INVOICE PAYMENT STATE GO ACCOUNT.PAYMENT Pcod ID
                context = {
                    'active_model': 'account.move',
                    'active_ids': order.invoice_ids.ids,
                    'active_id': order.invoice_ids[0].id,
                }
                payment_register = self.env['account.payment.register'].with_context(context).create({})
                payment_register.action_create_payments()
                #
