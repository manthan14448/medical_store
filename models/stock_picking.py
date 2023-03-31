from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # when click button_validate it write deliverd name and data
    def button_validate(self):
        res = super().button_validate()
        if self.sale_id:
            self.sale_id.write({
                'commitment_date': fields.Datetime.today(),
                'delivery_signed_by':self.env.uid
            })
        return res
