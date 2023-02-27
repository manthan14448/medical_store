from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers import main


class TempTest(http.Controller):
    @http.route('/shop/bodypart', website=True, auth='public')
    def advance_search(self, **kw):
        tdata = request.env['product.public.category'].search([])
        values = {
            'tdata': tdata
        }
        return request.render("medical_store.shop_templet", values)

    @http.route('/shop/bodypart/<int:bodypart>', website=True, auth='public')
    def advance_search_redirect(self, bodypart=None, **kw):
        category = request.env['product.public.category'].browse(bodypart)
        url = f'/shop/category/{category.name}-{bodypart}'
        return request.redirect(url)
