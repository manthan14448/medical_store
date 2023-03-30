from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers import main


class filter_router_medical(http.Controller):
    @http.route('/shop/bodypart', website=True, auth='public')
    def advance_search(self, **kw):
        return request.render("medical_store.shop_templet")

    @http.route(['/shop/bodypart/<int:bodypart>', '/bodypart/<int:bodypart>'], website=True, auth='public')
    def advance_search_redirect(self, bodypart=None, **kw):
        category = request.env['product.public.category'].browse(bodypart)
        url = f'/shop/category/{category.name}-{bodypart}'
        return request.redirect(url)

class PaymentDemoController(http.Controller):
    @http.route('/payment/cod/simulate_payment', type='json', auth='public')
    def cod_simulate_payment(self, **data):
        value = data['reference']
        if value:
            rec = request.env['payment.transaction'].search([('reference', '=', value)])
            rec.sudo().write({'state': 'delivery'})
            rec.sudo().sale_order_ids.action_confirm()

    @http.route('/delivery/status', type='http', auth="public", website=True, sitemap=False)
    def shop_delivery_confirmation(self, **post):
        return request.render('medical_store.delivery_status')
