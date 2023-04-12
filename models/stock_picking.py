from odoo import fields, models, _
from datetime import datetime,timedelta


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    cancelreason = fields.Char(string="Cancel Reason",readonly=True)

    # when click button_validate it write deliverd name and data
    def button_validate(self):
        res = super().button_validate()
        if self.sale_id:
            self.sale_id.write({
                'commitment_date': fields.Datetime.today(),
                'delivery_signed_by':self.env.uid
            })
        return res

    #use for reopen delivery
    def action_reopen(self):
        self.ensure_one()
        delivery_done = self.sale_id.picking_ids.filtered(lambda self: self.state == 'done')
        if delivery_done:
            return self.called_action_reopen(delivery_done)
            
        delivery_pending = self.sale_id.picking_ids.filtered(lambda self: self.state != 'cancel')
        if delivery_pending:
            return self.called_action_reopen(delivery_pending)

        else:
            stockcopy = self.copy()
            stockcopy.state = 'confirmed'
            stockcopy.date_deadline = datetime.now() + timedelta(days=3)
            stockcopy.move_ids_without_package.quantity_done = stockcopy.move_ids_without_package.product_uom_qty
            return self.called_action_reopen(stockcopy)
    
    #use for calling view in stock if alredy delivery done then it open not creating another data its open 
    # existing model data but if data state in cancel then it create new data   
    def called_action_reopen(self, res_id):
        view_id = self.env.ref('stock.view_picking_form').id
        return {
            'name': _('Open picking form'),
            'res_model': 'stock.picking',
            'view_mode': 'form',
            'view_id': view_id,
            'type': 'ir.actions.act_window',
            'res_id': res_id.id,
        }
    
    def action_cancel(self):
        for stock in self.filtered(lambda rec: rec.state != 'cancel'):
            wizard = self.env['cancel.delivery'].create({
                'delivery_id': stock.id,
            })
            return {
                'name': _('Test Wizard'),
                'type': 'ir.actions.act_window',
                'res_model': 'cancel.delivery',
                'view_mode': 'form',
                'res_id': wizard.id,
                'target': 'new'
            }
